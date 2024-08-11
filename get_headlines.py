############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############
from rss_parser import RSSParser
from requests import get

google_news_url = "https://news.google.com/news/rss"


def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    res = get(rss_url)
    rss = RSSParser.parse(res.text)
    return [item.title.content for item in rss.channel.items]


print(get_headlines(google_news_url))
