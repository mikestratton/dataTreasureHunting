"""Script to gather data from a starter toolkit url."""
import sys
import urllib.request
import json
import codecs

from pprint import pprint

from collections import namedtuple


URL = {'NY.GOV'     : 'https://data.ny.gov/data.json',
       'OREGON.GOV' : 'https://data.oregon.gov/data.json',
       'HAWAII.GOV' : 'https://data.hawaii.gov/data.json'}

def main():
    '''.'''
        
    json_object = get_json_from_url( URL['NY.GOV'] )
    
    assert(json_object['conformsTo'] == 'https://project-open-data.cio.gov/v1.1/schema')    
    
    with open('visual_of_combined.txt','w') as output:
        for idx,dataset in enumerate(json_object['dataset']):
            if 'keyword' in dataset.keys():
                keywords = ' '.join(str(x) for x in dataset['keyword'])
            if 'theme' in dataset.keys():
                theme = ' '.join(str(x) for x in dataset['theme'])
            if 'title' in dataset.keys():
                title = str(dataset['title'])
            if 'description' in dataset.keys():
                description = str(dataset['description'])
                
            dataset_essentials = (keywords,theme,title,description)
            combined = ' '.join(dataset_essentials)                    #<<<<<<<<<<<<<<<<<<<< combined is a string containing potential keywords

            ############################################################################
            #     Insert code/function, or call function, to get word count here
            
            ############################################################################
            #combined.encode('utf-8', errors = 'ignore')
            
            output.write(str(idx) + '\n')
            try:
                output.write(combined + '\n')
            except UnicodeEncodeError:
                pass
            output.write('***************************\n')
            
    

def get_json_from_url(url):
    '''.'''
    response = urllib.request.urlopen(url)
    reader = codecs.getreader('utf-8')
    json_object = json.load(reader(response))
    #str_response = response.readall().decode('utf-8')
    #json_object = json.loads(str_response)
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