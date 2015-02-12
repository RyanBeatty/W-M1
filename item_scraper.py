from bs4 import BeautifulSoup
import requests
import re


# Get the html for a specific webpage

def getItemHTML( url ):
    resp = requests.get("http://" + url)
    data = resp.text
    return data

# Parse the url with BeautifulSoup and return the relevant data

def getItemData( url ):
    data = getItemHTML( url )
    soup = BeautifulSoup(data)
    title = soup.title.string
    description = soup.find(id="postingbody").text
    picwrap = soup.find_all("img")                                 #if theres nothing in the array no pic
    mapwrap = soup.find_all(href=re.compile("maps.google.com"))    #if theres nothing in the array, no map
    returnData = { }
    returnData['title'] = title
    returnData['description'] = description
    returnData['pictures'] = picwrap
    returnData['map'] = mapwrap
    return returnData


def main():
    arr = getItemData("norfolk.craigslist.org/zip/4888401135.html")


if __name__ == "__main__":
    main()