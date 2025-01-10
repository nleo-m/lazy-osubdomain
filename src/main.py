from handlers import *
from bs4 import BeautifulSoup
import argparse


def get_args():
    parser = argparse.ArgumentParser(prog="Lazy o'subdomain")
    parser.add_argument("-d", "--domain", required=True, help="Domain to hunt")
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=1,
        help="How long in seconds to sleep between requests, default is 1",
    )
    parser.add_argument("-mp", "--max-pages", type=int, help="Max pages to go through")
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        help="Set Verbosity level, use -v or -vv",
    )
    parser.add_argument(
        "-c",
        "--check-status",
        action="store_true",
        help="Check status code of each domain",
    )

    args = parser.parse_args()
    return args


args = get_args()

g = Google(args)
g.show_banner()
g.find_subdomains()
