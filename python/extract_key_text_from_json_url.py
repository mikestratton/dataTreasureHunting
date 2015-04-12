"""Script to gather data from a starter toolkit url."""
import sys
import urllib.request
import json
import codecs
import re
import operator

from socket import timeout
from pprint import pprint
from collections import namedtuple
from urllib.error import HTTPError,URLError

ignore_words_str = '''the,be,to,of,and,a,in,that,have,I,it,for,not,on,with,he,as,you,do,at,this,but,his,by,
                    from,they,we,say,her,she,or,an,will,my,one,all,would,there,their,what,so,up,out,if,
                    about,who,get,which,go,me,when,make,can,like,time,no,just,him,know,take,person,into,
                    year,your,good,some,could,them,see,other,than,then,now,look,only,come,its,over,think,
                    also,back,after,use,two,how,our,work,first,well,way,even,new,want,because,any,these,give,
                    day,most,us,is'''
                    
ignore_words = ignore_words_str.split(',')                    

URL = {'NY_GOV'     : 'https://data.ny.gov/data.json',
       'OREGON_GOV' : 'https://data.oregon.gov/data.json',
       'HAWAII_GOV' : 'https://data.hawaii.gov/data.json'}

def main():
    '''.'''
        
    for key,url in URL.items():    
    
        json_object = get_json_from_url( url )
        assert(json_object['conformsTo'] == 'https://project-open-data.cio.gov/v1.1/schema')
        '''filename = key + '_readout.txt' '''
        filename = key + '_keywords.txt'
    
        with open(filename,'w',encoding='utf-8') as output:
            
            for idx,dataset in enumerate(json_object['dataset']):
                keywords = ''
                theme = ''
                title = ''
                description = ''
                landing_url = ''
                if 'keyword' in dataset.keys():
                    keywords = ' '.join(str(x) for x in dataset['keyword'])
                if 'theme' in dataset.keys():
                    theme = ' '.join(str(x) for x in dataset['theme'])
                if 'title' in dataset.keys():
                    title = str(dataset['title'])
                if 'description' in dataset.keys():
                    description = str(dataset['description'])
                
                '''if 'landingPage' in dataset.keys():
                    landing_url = dataset['landingPage']
                landing_url_json = (landing_url.split('/d/')[0] + '/api/views/' +
                                   landing_url.split('/d/')[1] + '/rows.json?accessType=DOWNLOAD')
                combined = get_text_from_url(landing_url_json)
                combined = re.sub(r'[^a-zA-Z]',r' ', combined)'''
                
                dataset_essentials = (keywords,theme,title,description)
                combined = ' '.join(dataset_essentials) # combined is a string containing potential keywords
                
                atypical_hyphen = r'[\u2010]'
                common_hyphen = r'-'
                combined = re.sub(atypical_hyphen, common_hyphen, combined)
                
                ############################################################################
                wordcount={}
                
                for word in combined.split():
                    
                    word = word.lower()
                    word = re.sub('[^\w]', '', word)
                    
                    if word not in ignore_words:
                        if word not in wordcount:
                            wordcount[word] = 1
                        else:
                            wordcount[word] += 1
                
                sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)    
                        
                output.write(str(idx) + ' ' + str(title) + '\n')
                for item in sorted_wordcount:
                    output.write(str(item[0]) + ' ' + str(item[1]))
                    output.write('\n')
                output.write('***************************\n')        
                #sys.exit(1)
                        
                
                
                ############################################################################
                
                '''output.write(str(idx) + '\n')            
                try:
                    output.write(combined + '\n')
                except UnicodeEncodeError:
                    print('UnicodeEncodeError was passed by')
                    pass
                output.write('***************************\n')'''
            
    

def get_json_from_url(url):
    '''.'''
    try:
        response = urllib.request.urlopen(url, timeout=10)
    except (HTTPError, URLError) as error:
        #logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
        print('Data not retrieved because %s\nURL: %s', error, url)
    except timeout:
        #logging.error('socket timed out - URL %s', url)
        print('socket timed out - URL %s', url)
    else:
        #logging.info('Access successful.')
        print('Access successful.')
        
    reader = codecs.getreader('utf-8')
    json_object = json.load(reader(response))
    #str_response = response.readall().decode('utf-8')
    #json_object = json.loads(str_response)
    return json_object
  
  
def get_text_from_url(url):
    '''.'''
    try:
        response = urllib.request.urlopen(url, timeout=10)
    except (HTTPError, URLError) as error:
        #logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
        print('Data not retrieved because %s\nURL: %s', error, url)
    except timeout:
        #logging.error('socket timed out - URL %s', url)
        print('socket timed out - URL %s', url)
    else:
        #logging.info('Access successful.')
        print('Access successful.')
        
    html = response.read().decode('utf-8')
    return html
    #with open('text.txt','w') as output:
        #html = str(html)
        #output.write(html)    
       
if __name__ == '__main__':
    sys.exit(main())