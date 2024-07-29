import pandas as pd
from fastwarc import WarcRecordType
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
from bs4 import BeautifulSoup
import html
import gzip
from urllib.parse import urlparse
import os
import logging
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
from fastwarc.warc import ArchiveIterator as FastWarcIterator
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def extract_content(html_content):
    try:
        soup = BeautifulSoup(html_content, 'lxml')
        title = html.unescape(soup.title.string.strip()) if soup.title and soup.title.string else None
        for script in soup(['script', 'style']):
            script.decompose()
        text = '\n'.join(soup.stripped_strings)
        return {'title': title, 'text_content': text}
    except Exception as e:
        logging.error(f"Error extracting content: {e}")
    return {'title': None, 'text_content': None}

def normalize_url(url):
    """
    Normalizes a URL by stripping common variants to determine if URLs are the same.

    Parameters:
    url (str): The URL to normalize.

    Returns:
    str: Normalized URL.
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.rstrip('/').split('/')
    if len(path) > 1 and path[-1] == 'index':
        path = path[:-1]
    normalized_path = '/'.join(path)
    return f"{parsed_url.scheme}://{parsed_url.netloc}{normalized_path}"

def fail_qa_check(text_content, url):
    """
    Checks if a webpage fails QA based on the given criteria.

    Parameters:
    text_content (str): The text content of the webpage.
    url (str): The URL of the webpage.

    Returns:
    bool: True if the webpage fails QA, False otherwise.
    """
    error_indicators = [
        "404", "network error", "site cannot be reached", "domain for sale", "domain expired",
        "domain not in use", "page no longer available", "page not found", "hello world",
        "lorem ipsum", "content totally unrelated"
    ]
    if any(indicator in text_content.lower() for indicator in error_indicators):
        return True
    if not text_content.strip() or text_content.lower() in ["index"]:
        return True
    if "login" in text_content.lower() and len(text_content.strip()) < 100:
        return True
    if "flash player" in text_content.lower():
        return True
    known_domain_sellers = ["hostgator.sg", "hostasean.sg", "webhost.com.sg"]
    if any(seller in url for seller in known_domain_sellers):
        return False
    return False

def deduplicate_records(records):
    """
    Deduplicates records based on URL rules.

    Parameters:
    records (list): List of records to deduplicate.

    Returns:
    list: Deduplicated list of records.
    """
    seen_urls = {}
    deduplicated_records = []
    for record in records:
        normalized_url = normalize_url(record['url'])
        if normalized_url in seen_urls:
            seen_urls[normalized_url]['web_text_content'] += "\n" + record['web_text_content']
        else:
            seen_urls[normalized_url] = record
            deduplicated_records.append(record)
    return deduplicated_records

def get_warc_version(file_path):
    with gzip.open(file_path, 'rb') as f:
        for line in f:
            if line.startswith(b'WARC/'):
                return line.decode('utf-8').strip()
    return None
def decode_payload(raw_payload):
    try:
        # Attempt to decode assuming it's a gzip-compressed payload
        return gzip.decompress(raw_payload).decode('utf-8', errors='ignore')
    except (OSError, UnicodeDecodeError) as e:
        logging.error(f"Failed to decode gzip payload: {e}")
        try:
            # Attempt to decode assuming it's a plain UTF-8 encoded payload
            return raw_payload.decode('utf-8', errors='ignore')
        except UnicodeDecodeError as e:
            logging.error(f"Failed to decode raw payload as UTF-8: {e}")
            return None
def parse_warc_fastwarc(file_path):
    records = []
    try:
        with gzip.open(file_path, 'rb') as stream:
            archive_iterator = FastWarcIterator(stream, record_types=WarcRecordType.response, auto_decode='gzip')
            for record in archive_iterator:
                try:
                    http_headers = record.http_headers
                    if not http_headers or http_headers.status_code != 200:
                        logging.debug(f"No html files found. Record headers: {record.rec_headers.headers}")
                        logging.debug(f"Skipped non-HTML content type: {http_headers.status_code}")
                        continue
                    content_type = http_headers.get('Content-Type', '')
                    print(content_type)
                    if 'text/html' in content_type:
                        raw_payload = record.reader.read()
                        # print(raw_payload)
                        payload = decode_payload(raw_payload)
                        # print(payload)
                        if payload is None:
                            continue

                        logging.debug(f"Record payload: {payload[:100]}")  # Print first 100 characters of payload

                        if not payload.strip().startswith('<'):
                            logging.info(f"Skipped non-HTML content in file {file_path}, record {record}")
                            continue

                        content = extract_content(payload)
                        url = record.headers.get('WARC-Target-URI', '')
                        if content['text_content'] and not fail_qa_check(content['text_content'], url):
                            records.append({
                                'filename': os.path.basename(file_path),
                                'title': content['title'],
                                'web_text_content': content['text_content'],
                                'url': url
                            })
                except Exception as e:
                    logging.error(f"Error processing record in file {file_path}: {e}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
    logging.info(f"Parsed {len(records)} records from file {file_path}")
    return records

def process_warc_files(folder_path, max_workers=3):
    """
    Processes all WARC files in a given folder using multithreading.

    Parameters:
    folder_path (str): Path to the folder containing WARC files.
    max_workers (int): Maximum number of worker threads.

    Returns:
    pd.DataFrame: DataFrame containing the extracted data from all WARC files.
    """
    files = [os.path.join(root, file) 
             for root, _, files in os.walk(folder_path) 
             for file in files if file.endswith('.warc.gz')]
    
    total_files = len(files)
    logging.info(f"Total files to process: {total_files}")
    max_workers = multiprocessing.cpu_count()-1

    data = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(parse_warc_fastwarc, file_path): file_path for file_path in files}
        
        with tqdm(total=total_files, desc="Processing WARC files") as pbar:
            for future in as_completed(futures):
                file_path = futures[future]
                try:
                    result = future.result()
                    data.extend(result)
                    pbar.update(1)
                    pbar.set_postfix({"File": os.path.basename(file_path), "Records": len(result)})
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")
                    pbar.update(1)
    
    deduplicated_data = deduplicate_records(data)
    return pd.DataFrame(deduplicated_data)