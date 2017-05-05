import re


class EmailDetector:
    def __init__(self, raw_html):
        print("\t Parsing strings...")
        self.raw_html = self.format_html(raw_html)

    @staticmethod
    def format_html(string):
        return string.replace("\n", "").replace(">", ">\n")

    def parse_possible_emails(self):
        print "\t Getting email matches..."
        matches = re.findall(r'[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', self.raw_html)
        return self.eliminate_duplicates(matches)

    @staticmethod
    def eliminate_duplicates(matches):
        return set(matches)
