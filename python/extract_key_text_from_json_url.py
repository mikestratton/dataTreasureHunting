"""Script to gather data from a starter toolkit url."""
import sys
import urllib.request
import json
import codecs

from pprint import pprint



URL = "http://data.gov.au/api/3/action/package_show?id=polar-environmental-data-layers"

def main():
    """Main entry point for the script."""
    #get_raw_text(URL)
    get_json(URL)

    
    
    
    
    
    
def get_text_from_url(url):
    '''.'''
    response = urllib.request.urlopen(url)
    html = response.read()
    with open('text.txt','w') as output:
        html = str(html)
        output.write(html)
    
def get_json(url):
    '''.'''
    response = urllib.request.urlopen(url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    
    pprint(data["result"]["notes"])
    
    
    
if __name__ == '__main__':
    sys.exit(main())