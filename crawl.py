from xml.etree.ElementTree import TreeBuilder
from lxml import html
from urllib.parse import urlparse
import requests

def get_urls_from_string(page_content, base_url):
    urls = []
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url=base_url)
    for elem in tree.iter():
        if elem.tag == "a":
            url = elem.get("href")
            urls.append(url)
    return urls

def normalize_url(url):
    parsed_url = urlparse(url)
    netloc_path = "{}{}".format(parsed_url.netloc, parsed_url.path)
    lowercased = netloc_path.lower()
    if len(lowercased) < 1:
        return lowercased
    last_slash_removed = lowercased if lowercased[-1] != "/" else lowercased[:-1]
    return last_slash_removed

def crawl_page(base_url, current_url, pages):
    normalized_url = normalize_url(current_url)
    
    if normalized_url not in pages:
        pages[normalized_url] = 0
    
    if urlparse(base_url).netloc != urlparse(current_url).netloc:
        pages[normalized_url] = None
        return pages
    
    if pages[normalized_url] is None:
        return pages
    
    if pages[normalized_url] > 0:
        pages[normalized_url] +=1
        return pages

    resp = requests.get(current_url)
    
    try:
        validate_response(resp,current_url)
    except Exception as e:
        print(e)
        pages[normalized_url] = None 
        return pages
    pages[normalized_url] +=1
    
    urls = get_urls_from_string(resp.content, base_url)

    for url in urls:
        crawl_page(base_url, url, pages)
    return pages

def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception(
            "{} didn't result in a 200 response code, got {}".format(
                url, resp.status_code
            )
        )

    # If the content type isn't HTML skip it
    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception("{} didn't result in an HTML response".format(url))
    