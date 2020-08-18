from chalice import Chalice
import csv
import requests
import xml.etree.ElementTree as ET


def loadRSS():
    # url of rss feed
    url = 'https://www.nhc.noaa.gov/rss_examples/index-at-20130605.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

app = Chalice(app_name='detect_hurricane')



def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:

            # special checking for namespace object nhc:Cyclone
            if child.tag == '{http://www.nhc.noaa.gov}Cyclone':
                for subItem in child.findall(".//"):
                    key = subItem.tag[25:]
                    news[key] = subItem.text
        if len(news) > 0:
            newsitems.append(news)

    return newsitems


@app.route('/')
def index():
    loadRSS()
    newsitems = parseXML('topnewsfeed.xml')
    print(newsitems)
    if len(newsitems) > 0:
        return newsitems[0]
    return {'type': 'CLEAR'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
