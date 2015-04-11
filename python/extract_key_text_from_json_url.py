"""Script to gather data from a starter toolkit url."""
import sys
import urllib.request
import json
import codecs

from pprint import pprint



URL = {'NY.GOV'     : 'https://data.ny.gov/data.json',
       'OREGON.GOV' : 'https://data.oregon.gov/data.json',
       'HAWAII.GOV' : 'https://data.hawaii.gov/data.json'}

def main():
    '''.'''
    
    
    
    json_object = get_json_from_url( URL['NY.GOV'] )
    
    assert(json_object['conformsTo'] == 'https://project-open-data.cio.gov/v1.1/schema')
    
    with open('titles.txt','w') as output:
        for dataset in json_object['dataset']:
            #output.write(dataset['title'] + '\n')
            
    

def get_json_from_url(url):
    '''.'''
    response = urllib.request.urlopen(url)
    reader = codecs.getreader('utf-8')
    json_object = json.load(reader(response))
    return json_object
  
  
def get_text_from_url(url):
    '''.'''
    response = urllib.request.urlopen(url)
    html = response.read()
    with open('text.txt','w') as output:
        html = str(html)
        output.write(html)    
       
if __name__ == '__main__':
    sys.exit(main())