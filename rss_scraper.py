import feedparser

rss_generic_free_link = "http://%s.craigslist.org/search/zip?query=%s&format=rss"


def get_rss(site, term=""):
	rss_link = rss_generic_free_link % (site, term)
	return feedparser.parse(rss_link)

def parse_item(item):
	result = {}
	result['url'] = item['dc_source']
	result['title'] = item['title']
	result['summary'] = item['summary']
	result['picture'] = None
	if item.get('enc_enclosure'):
		result['picture'] = item['enc_enclosure'].get('resource')
	return result

def parse_item_list(rss):
	return map(parse_item, rss.entries)

def parse_rss_feed(site, term=""):
	rss = get_rss(site, term)
	return parse_item_list(rss)

if __name__ == "__main__":
	parse_rss_feed()