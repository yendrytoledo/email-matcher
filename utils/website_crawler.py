from HTMLParser import HTMLParser
import urllib


class WebsiteCrawler(HTMLParser):
    def __init__(self, raw_html, website_url):
        HTMLParser.__init__(self)
        print("Crawling possible websites...")
        self.website_set = set()
        self.website_url = website_url
        self.raw_html = raw_html

        self.website_set.add(website_url)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    if self.website_url not in value:
                        continue
                    value = self.normalize_url(value)
                    self.website_set.add(value)

    def normalize_url(self, value):
        value = str(value)
        value = self.remove_schema(value)
        value = self.handle_slash_beginning(value)
        value = self.quote_url(value)
        value = self.remove_double_slashes(value)
        return value

    @staticmethod
    def quote_url(value):
        return urllib.quote_plus(value, safe="%/:=&?~#+!$,;'@()*[]")

    def handle_slash_beginning(self, value):
        if value.startswith('//'):
            value = value[2:]
        if value.startswith('/') or value.startswith('#'):
            value = self.website_url + value
        return value

    def remove_double_slashes(self, value):
        if '//' not in value:
            return value
        value = value.replace('//', '/')
        return self.remove_double_slashes(value)

    @staticmethod
    def remove_schema(value):
        return value.replace('http://', '').replace('https://', '')

    def get_websites(self):
        return self.website_set
