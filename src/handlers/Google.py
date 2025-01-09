from .Abstract import Handler
from bs4 import BeautifulSoup
import math
import requests
import re
import time


class Google(Handler):
    def __init__(self, args):
        super().__init__(args)

        self.offset = 100
        self.base_url = "https://www.google.com"

    def find_subdomains(self):
        self.log("Searching for subdomains in Google", 0)

        total_pages = self.get_total_pages() if not self.max_pages else self.max_pages

        self.log(f"Going through {total_pages} pages")

        for page in range(0, total_pages):
            time.sleep(self.timeout)
            page = self.get_parsed_page(page)
            self.get_page_urls(page)

        self.show_results()

    def get_total_pages(self):
        self.log("Getting total number of pages to go through", 2)

        r = requests.get(
            f"{self.base_url}/search?q=site:*.{self.domain}&num=1",
            headers={
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
            },
        )

        soup = BeautifulSoup(r.content, "lxml")
        results = (
            soup.find("div", id="result-stats")
            .get_text()
            .replace(".", "")
            .replace(",", "")
        )
        num_results = re.search(r"\d+", results)
        total_pages = math.floor(int(num_results.group(0)) / self.offset)

        self.log(f"Going through {total_pages} pages")

        return total_pages

    def get_parsed_page(self, page=1):
        r = requests.get(
            f"{self.base_url}/search?q=site:*.{self.domain}&start={page * self.offset}&num={self.offset}",
            headers={
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
            },
        )

        self.log(f"Page {page} responded with {r.status_code}", 2)

        soup = BeautifulSoup(r.content, "lxml")

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
