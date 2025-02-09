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

# Функция записи результата в файл
def write_file(search_method, start_time, finish_time):
    print(f"Время выполнения {search_method} метода - {finish_time - start_time:4f}.\n")

    with open("ResultsGetRequests.txt", 'a') as result_file:
        result_file.write(
            f"Время выполнения {search_method} метода - {finish_time - start_time:4f}.\n")


class RequestsManager:

    def make_request(self, url_diapason):
        """Выполняет GET-запрос к указанному URL."""
        status_codes = []

        url_num = 0

        try:
            for index, url in enumerate(url_diapason):
                response = requests.get(url)
                response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
                print(f"Запрос к {url} вернул статус код: {response.status_code}")
                status_codes.append(response.status_code)
                url_num = url_diapason[index + 1] if index < len(url_diapason) - 1 else 0
            return status_codes
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {url_num}: {e}")
            return None