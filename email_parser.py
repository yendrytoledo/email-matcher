import sys
from utils.email_detector import EmailDetector
from utils.http_handler import HttpHandler
from utils.website_crawler import WebsiteCrawler

if len(sys.argv) != 2:
    print "Usage: $ email_parser HTTP_URL"
    sys.exit()

emails = set()

website_url = sys.argv[1]
http_handler = HttpHandler(website_url)
html_response = http_handler.raw_response
website_crawler = WebsiteCrawler(html_response, website_url)
website_crawler.feed(html_response)

for website in website_crawler.get_websites():
    # TODO: Implement multithreading
    http_handler = HttpHandler(website)
    if not http_handler.did_website_load_correctly():
        continue
    html_response = http_handler.raw_response
    email_detector = EmailDetector(html_response)
    possible_emails = email_detector.parse_possible_emails()
    print "Found these emails", possible_emails
    emails.update(possible_emails)

print "\nEmails found in domain:", website_url
for string in emails:
    print "\t\t - Email found: " + string
