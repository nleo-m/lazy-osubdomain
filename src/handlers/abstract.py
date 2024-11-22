# get number of pages
# while page < numOfPages
# req get page > use start=10**0 param in google
# parse page content
# find all page urls
# for url in urls
# if url not in foundSubdomains
# add url to foundSubdomains

from abc import ABC

class Handler(ABC):
    def __init__(self):
        self.url_regex = r'https?://[a-zA-Z0-9.-]+'
        self.subdomains = []
        self.domain = ""
    
    @classmethod
    def find_subdomains(self):
        pass

    @classmethod
    def get_total_pages(self):
        pass

    @classmethod
    def get_parsed_page(self, page):
        pass
    
    @classmethod
    def get_page_urls(self, page):
        pass

    def show_results(self):   
        for s in self.subdomains:
            print(s)