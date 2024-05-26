#!/usr/bin/env python3

import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: # we use 5 threads
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

# Explanations:
# ThreadPoolExecutor = Thread + Pool + Executor.

# Thread is just a train of thought. 
# The Pool portion is where it starts to get interesting. This object is going to create a pool of threads, each of which can run concurrently. 
# Finally, the Executor is the part that’s going to control how and when each of the threads in the pool will run. It will execute the request in the pool.