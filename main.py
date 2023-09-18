import feedparser

feed_url = input('Input the URL of the feed: ')
fp = feedparser.parse(feed_url)

try:
    print(fp['feed']['title'])
except KeyError as e:
    print('Error parsing feed title. Double check the feed URL')

try:
    for entry in fp.entries:
        print()
        print(f'** {entry.title} **')
        print(entry.description)
        print(entry.link)
        print('*****')
        print()
except KeyError as e:
    print('Error parsing entries. Double check the feed URL')
