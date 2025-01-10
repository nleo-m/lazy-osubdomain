from abc import ABC
import requests


class Handler(ABC):
    def __init__(self, args):
        self.url_regex = r"https?://[a-zA-Z0-9.-]+"
        self.subdomains = []
        self.domain = args.domain
        self.verbosity = args.v
        self.timeout = int(args.timeout)
        self.max_pages = args.max_pages
        self.check_status = args.check_status

    def show_banner(self):
        print("""     Lazyos\n=================\n""")

    @classmethod
    def find_subdomains(self):
        pass

    @classmethod
    def get_total_pages(self):
        pass

    @classmethod
    def get_page(self, page):
        pass

    @classmethod
    def get_page_urls(self, page):
        pass

    def check_domains(self):
        self.log("Checking status code of the found domains")
        checked_subdomains = []

        for domain in self.subdomains:
            try:
                request = requests.get(domain)

                self.log(f"Domain {domain} responded with {request.status_code}", 2)

                checked_subdomains.append(
                    {
                        "name": domain,
                        "status_code": f"{request.status_code} {request.reason}",
                    }
                )
            except Exception as e:
                checked_subdomains.append(
                    {"name": domain, "status_code": "Unknown error"}
                )
            finally:
                self.subdomains = checked_subdomains

    def log(self, message, verbosity_level=1):
        if self.verbosity >= verbosity_level:
            print(message)

    def show_results(self):
        print("\n\033[93m" + f"Unique subdomains found: {len(self.subdomains)}\n")

        for s in self.subdomains:
            if self.check_status:
                print("\033[92m" + s["name"], "." * 10, s["status_code"])
            else:
                print("\033[92m" + s)

        print("\033[39m")
