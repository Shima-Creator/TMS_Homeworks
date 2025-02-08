import multiprocessing
import threading

import requests
import time

URLS = [
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.wikipedia.org",
        "https://www.microsoft.com",
        "https://www.apple.com",
        "https://www.bbc.com",
        "https://www.nytimes.com",
        "https://www.cnn.com",
        "https://www.reddit.com",
        "https://www.stackoverflow.com",
        "https://github.com",
        "https://www.yahoo.com",
        "https://www.bing.com",
        "https://www.paypal.com",
        "https://www.netflix.com",
        "https://www.office.com",
        "https://www.salesforce.com",
        "https://www.adobe.com",
        "https://www.cloudflare.com",
        "https://www.ibm.com",
    ]

def write_file(search_method, start_time, finish_time):
    print(f"Время выполнения {search_method} метода - {finish_time - start_time:4f}.\n")

    with open("ResultsGetRequests.txt", 'a') as result_file:
        result_file.write(
            f"Время выполнения {search_method} метода - {finish_time - start_time:4f}.\n")






