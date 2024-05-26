#!/usr/bin/env python3

#  An I/O-bound program: a common problem: downloading content over the network. For our example, you will be downloading web pages from a few sites, 
# but it really could be any network traffic. It’s just easier to visualize and set up with web pages.

import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")




# This code is from https://realpython.com/python-concurrency/