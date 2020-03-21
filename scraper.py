#!/usr/bin/env python
import argparse

__author__ = 'luisfff29'


def parser_argparse():
    parser = argparse.ArgumentParser(
        description='Input link to start scrapping')
    parser.add_argument('url', help='link of a single web page')
    return parser


def main():
    parser = parser_argparse()
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
