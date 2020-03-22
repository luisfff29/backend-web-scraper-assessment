Today you'll see a command line program to scrape a single web page, extracting any URLs, email addresses, and phone numbers it contains.

This program used the following libraries:

1. [argparse](https://docs.python.org/2/library/argparse.html) library to parse a URL passed in as a command line argument.
2. [requests](https://requests.readthedocs.io/en/master/user/quickstart/) library to retrieve the text of the webpage at the specified URL.
3. [re](https://docs.python.org/2/library/re.html) library to look for email addresses, URLs, and phone numbers included in the page.
4. [HTMLParser](https://docs.python.org/2/library/htmlparser.html) library to explicitly recognize A and IMG tags, and access their HREF and SRC attributes.
5. [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) library to construct a full (“absolute”) URL by combining a “base URL” with another URL.

## Note on parsing HTML

In general, regular expressions are not well suited for parsing HTML. In this case, the patterns used were from the following links:

- [urlregex.com](http://urlregex.com/)
- [emailregex.com](http://emailregex.com/)
- [phoneregex.com](http://phoneregex.com/)

## Output

Your scraper doesn't have to conform to a specific output format, but running it with a command like:

> `$ python scraper.py http://kenzie.academy/`

Should output some reasonably formatted text listing the URLs, email addresses, and phone numbers found in the page.
