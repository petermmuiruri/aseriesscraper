import urllib.request
import re
import sys

if len(sys.argv) != 2:
    raise ValueError("Please provide a url link")


user_agent  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
headers     = {'User-Agent':user_agent}

def download_page(url):
    request     = urllib.request.Request(url, None, headers)
    response    = urllib.request.urlopen(request)
    data        = response.read()
    return data.decode('utf-8')

def extract_links(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)

if __name__ == '__main__':
    target_url=sys.argv[1]

    pageOfInterest  = download_page(target_url)
    links           = extract_links(pageOfInterest)

    for link in links:
        pageOfInterest.__dir__(
        print(link)
