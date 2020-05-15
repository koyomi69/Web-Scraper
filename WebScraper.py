from bs4 import BeautifulSoup
import requests
import urllib
import sys
from urllib.parse import urljoin

links = []


def web_crawl(url):
    res = requests.get(url)
    data = res.text
    soup = BeautifulSoup(data, 'html.parser')
    check = ''

    if url.startswith('https'):
        check = url[12:]
    elif url.startswith('http'):
        check = url[11:]

    for link in soup.find_all('a'):
        link_url = link.get('href')
        link_s = str(link_url)

        if link_s is not None and 'http' not in link_s:
            link_s = urllib.parse.urljoin(str(url), link_s)

        if check not in link_s:
            continue

        if 'mailto:' in link_s:
            continue

        links.append(link_s)

    write_file(links)

    for inc_one in links:
        print(inc_one)


def write_file(inks):
    with open('select2.txt', 'a') as f:
        f.writelines(str(inks) + '\n')
        f.write('\n')


def sub_links():
    for i in range(1, len(links), 1):
        a = str(links[i])
        web_crawl(a)

    for inc_two in links:
        print(inc_two)


crawl_link = sys.argv[1]

web_crawl(crawl_link)
sub_links()
