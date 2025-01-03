from abc import ABC

class Handler(ABC):
    def __init__(self):
        self.url_regex = r'https?://[a-zA-Z0-9.-]+'
        self.subdomains = []
        self.domain = ""

    def show_banner(self):
        print('''Lazy o'subdomain''')
    
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
        print("\033[93m" + f"Unique subdomains found: {len(self.subdomains)}\n")

        for s in self.subdomains:
            print('\033[92m' + s)