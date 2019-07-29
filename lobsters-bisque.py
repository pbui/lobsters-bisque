#!/usr/bin/env python3

import feedparser
import requests

# Constants

LOBSTERS_FEED_URL       = 'https://lobste.rs/rss'
LOBSTERS_MINIMUM_SCORE  = 5

# Functions

def fetch_article_score(url):
    response = requests.get(url + '.json')
    return response.json()['score']

def fetch_all_articles(url=LOBSTERS_FEED_URL):
    feed = feedparser.parse(url)

    for entry in feed.entries:
        yield {
            'title'    : entry.title,
            'author'   : entry.author.split('@')[0],
            'link'     : entry.comments,
            'published': entry.published,
            'timestamp': entry.published_parsed,
            'guid'     : entry.guid,
            'score'    : fetch_article_score(entry.comments),
        }

def write_articles_feed(articles):
    print('''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>Lobsters</title>
<link>https://lobste.rs</link>
<description></description>''')

    for article in sorted(articles, key=lambda a: a['timestamp'], reverse=True):
        print('''<item>
<title>{article_title}</title>
<author>{article_author}</author>
<link>{article_link}</link>
<guid isPermaLink="false">{article_guid}</guid>
<pubDate>{article_published}</pubDate>
</item>'''.format(article_title     = article['title'],
                  article_author    = article['author'],
                  article_link      = article['link'],
                  article_guid      = article['guid'],
                  article_published = article['published']))
    print('''</channel>
</rss>''')

# Main Execution

if __name__ == '__main__':
    write_articles_feed(a for a in fetch_all_articles() if a['score'] > LOBSTERS_MINIMUM_SCORE)
