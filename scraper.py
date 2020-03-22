#!/usr/bin/env python3
import argparse
import requests
import re
from html.parser import HTMLParser
from urllib.parse import urljoin


__author__ = 'luisfff29'

# Regex to find urls, emails, and phones
pattern_url = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
    '[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pattern_email = re.compile(
    r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
pattern_phone = re.compile(
    r'1?[( ]*[2-9][0-8][0-9][) .-]+[2-9][0-9]{2}[. -]+[0-9]{4}')


# Create argparse
def parser_argparse():
    parser = argparse.ArgumentParser(
        description='Input link to start scrapping')
    parser.add_argument('url', help='link of a single web page')
    return parser


# Parsing HTML with HTMLParser Module
class MyHTMLParser(HTMLParser):

    tags_list = []

    def handle_starttag(self, tag, attrs):
        for (attr, content) in attrs:
            if tag in ['a', 'img'] and attr in ['href', 'src']:
                self.tags_list.append(content)
        return self.tags_list


def main():
    parser = parser_argparse()
    args = parser.parse_args()

    # Read response data of url given in argparse
    r = requests.get(args.url).text
    parser = MyHTMLParser()
    # Find more urls inside 'a' and 'img' attributes
    parser.feed(r)

    print('\nURLS:\n')
    list_urls = pattern_url.findall(r)
    # Concat http regex urls with attr urls
    for link in parser.tags_list:
        if link.startswith('/'):
            list_urls.append(urljoin(args.url, link))
    # Print all urls sorted and no-duplicates
    for x in sorted(set(list_urls)):
        print(x)

    print('\nEMAILS:\n')
    # Print all emails
    list_emails = pattern_email.findall(r)
    if list_emails:
        for x in sorted(set(list_emails)):
            print(x)
    else:
        print('None')

    print('\nPHONE NUMBERS:\n')
    # Print all phone numbers
    list_phones = pattern_phone.findall(r)
    if list_phones:
        for x in sorted(set(list_phones)):
            print(x)
    else:
        print('None')


if __name__ == '__main__':
    main()
