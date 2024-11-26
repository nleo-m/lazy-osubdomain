from .abstract import Handler
from bs4 import BeautifulSoup
import math
import requests
import re
import time


class GoogleHandler(Handler):
    def __init__(self, domain, offset = 1000):
        super().__init__()
        self.domain = domain
        self.offset = offset
    
    def find_subdomains(self):
        total_pages = self.get_total_pages()

        for page in range(0, total_pages):
            time.sleep(2)
            page = self.get_parsed_page(page)
            self.get_page_urls(page)

        self.show_results()



    def get_total_pages(self):
        r = requests.get(f"https://www.google.com/search?q=site:*.{self.domain}&num=1", headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'})
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find("div", id='result-stats').get_text().replace(".", "").replace(",", "")
        num_results = re.search(r"\d+", results)
        total_pages = math.floor(int(num_results.group(0)) / self.offset)

        return total_pages

    def get_parsed_page(self, page = 1):
        print(page * self.offset)
        r = requests.get(f"https://www.google.com/search?q=site:*.{self.domain}&start={page * self.offset}&num={self.offset}", headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'})
        soup = BeautifulSoup(r.content, 'html.parser')

        return soup
    
    def get_page_urls(self, page):
        a_elements = page.find_all("a")
        urls = [u.get("href") for u in a_elements if isinstance(u.get("href"), str)]

        for u in urls:
            match = re.search(self.url_regex, u)

            if not match:
                continue

            match = match.group(0)

            if self.domain not in match:
                continue
            
            if match not in self.subdomains:
                self.subdomains.append(match)