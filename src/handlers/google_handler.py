from .abstract import Handler
from bs4 import BeautifulSoup
import requests
import re


class GoogleHandler(Handler):
    def __init__(self, domain):
        super().__init__()
        self.domain = domain
    
    def find_subdomains(self):
        page = self.get_parsed_page()

        self.get_page_urls(page)

        self.show_results()

    def get_total_pages(self):
        pass

    def get_parsed_page(self, page = 10):
        r = requests.get(f"https://www.google.com/search?q=site:*.{self.domain}")
        soup = BeautifulSoup(r.content, 'html.parser')

        return soup
    
    def get_page_urls(self, page):
        a_elements = page.find_all("a")
        urls = [u.get("href") for u in a_elements if u.get('href') and u.get('href').startswith("/url?")]

        for u in urls:
            match = re.search(self.url_regex, u)
            
            if not match:
                continue

            match = match.group(0)
            
            if match not in self.subdomains:
                self.subdomains.append(match)