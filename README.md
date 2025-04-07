# Lazyos | Lazy Osint Subdomains

This tool is designed to enumerate subdomains using OSINT.  
This is still under development and currently, only Google is supported.

<div align="center">
  <img src="/public/assets/preview.jpeg" width="100%" />
</div>

## Installation

1. Install pipenv if not already installed
   `pip install pipenv`

Do not use pip install -r requirements.txt unless you are converting the project to use pip and virtualenv

2. Install dependencies
   `pipenv install`

3. Activate the environment
   `pipenv shell`

## Usage

````
usage: Lazy o'subdomain [-h] -d DOMAIN [-t TIMEOUT] [-mp MAX_PAGES] [-v] [-c]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain to hunt
  -t TIMEOUT, --timeout TIMEOUT
                        How long in seconds to sleep between requests, default is 1
  -mp MAX_PAGES, --max-pages MAX_PAGES
                        Max pages to go through
  -v                    Set Verbosity level, use -v or -vv
  -c, --check-status    Check status code of each domain```
````
