from bs4 import BeautifulSoup
import requests
import re
import feedparser


rss_generic_free_link = "http://%s.craigslist.org/search/zip?query=%s&format=rss"
SUMMARY_LIMIT = 150

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


# Get the html for a specific webpage

def getItemHTML( url ):
    resp = requests.get(url)
    data = resp.text
    return data

# Parse the url with BeautifulSoup and return the relevant data

def getItemData( url ):
    data = getItemHTML( url )
    soup = BeautifulSoup(data)                                #if theres nothing in the array no pic
    mapwrap = soup.find_all(href=re.compile("maps.google.com"))    #if theres nothing in the array, no map
    if(len(mapwrap) > 0):
        mapwrap = mapwrap[0].get('href')
    else:
        mapwrap = None
    replylink = soup.find(id="replylink")
    emailRequest = requests.get("http://norfolk.craigslist.com" + replylink.get('href'))
    emailRequestData = emailRequest.text
    emailSoup = BeautifulSoup(emailRequestData)
    replyEmail = emailSoup.find_all(class_="anonemail")[0].text
    addressArray = soup.findAll("div", { "class" : "mapaddress" })
    if len(addressArray) > 0:
        address = addressArray[0].text
    else:
        address = None
    returnData = { }
    returnData['map'] = mapwrap
    returnData['replyemail'] = replyEmail
    returnData['address'] = address
    return returnData

if __name__ == "__main__":
	print(getItemData('http://norfolk.craigslist.org/zip/4888365762.html'))