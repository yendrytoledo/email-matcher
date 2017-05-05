import requests


class HttpHandler():
    def __init__(self, url):
        print("Setting up the url: " + url + "...")

        if not url.startswith("http:") or not url.startswith("https:"):
            url = "http://" + url
        self.url = url
        try:
            self.raw_response = self.make_http_request()
            self.did_load_correctly = True
        except Exception:
            self.did_load_correctly = False

    def make_http_request(self):
        # TODO: Error handling
        # TODO: Caching logic
        # TODO: Retrying logic

        print("\t Downloading website info...")
        return requests.get(self.url).text

    def did_website_load_correctly(self):
        return self.did_load_correctly
