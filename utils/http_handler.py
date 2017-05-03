import requests


class HttpHandler():
    def __init__(self, url):
        print("Setting up the url: " + url + "...")

        if "http:" not in url:
            url = "http://" + url
        self.url = url
        self.raw_response = self.make_http_request()

    def make_http_request(self):
        # TODO: Error handling
        # TODO: Caching logic
        # TODO: Retrying logic

        print("\t Downloading website info...")
        try:
            return requests.get(self.url).text
        except Exception:
            return ""
