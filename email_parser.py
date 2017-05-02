import sys
from utils.email_detector import EmailDetector
from utils.http_handler import HttpHandler

if len(sys.argv) != 2:
    print "Usage: $ email_parser HTTP_URL"
    sys.exit()

http_handler = HttpHandler(sys.argv[1])
email_detector = EmailDetector(http_handler.raw_response)
emails = email_detector.parse_possible_emails()

for string in emails:
    print "\t - Email found: " + string
