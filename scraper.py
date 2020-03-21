#!/usr/bin/env python
import argparse
import requests
import re


__author__ = 'luisfff29'


pattern_url = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
    '[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


def parser_argparse():
    parser = argparse.ArgumentParser(
        description='Input link to start scrapping')
    parser.add_argument('url', help='link of a single web page')
    return parser


def main():
    parser = parser_argparse()
    args = parser.parse_args()
    print(args)

    r = requests.get(args.url).text
    list_urls = re.findall(pattern_url, r)
    for x in sorted(set(list_urls)):
        print(x)


if __name__ == '__main__':
    main()
