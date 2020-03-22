#!/usr/bin/env python3
import argparse
import requests
import re
from html.parser import HTMLParser


__author__ = 'luisfff29'


pattern_url = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
    '[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pattern_email = re.compile(
    r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
pattern_phone = re.compile(
    r'1?[( ]*[2-9][0-8][0-9][) .-]+[2-9][0-9]{2}[. -]+[0-9]{4}')


def parser_argparse():
    parser = argparse.ArgumentParser(
        description='Input link to start scrapping')
    parser.add_argument('url', help='link of a single web page')
    return parser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags_list = []
        for (attr, content) in attrs:
            if tag in ['a', 'img'] and attr in ['href', 'src']:
                tags_list.append(content)
        return tags_list[]


def main():
    parser = parser_argparse()
    args = parser.parse_args()
    print(args)

    r = requests.get(args.url).text
    parser = MyHTMLParser()
    parser.feed(r)
    # print('\nURLS:\n')
    # list_urls = pattern_url.findall(r)
    # for x in sorted(set(list_urls)):
    #     print(x)

    # list_emails = pattern_email.findall(r)
    # print('\nEMAILS:\n')
    # if list_emails:
    #     for x in sorted(set(list_emails)):
    #         print(x)
    # else:
    #     print('None')

    # list_phones = pattern_phone.findall(r)
    # print('\nPHONE NUMBERS:\n')
    # if list_phones:
    #     for x in sorted(set(list_phones)):
    #         print(x)
    # else:
    #     print('None')


if __name__ == '__main__':
    main()
