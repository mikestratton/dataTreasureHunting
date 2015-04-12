#!/usr/bin/python
import re
file=open("HAWAII_GOV_readout_ANSI.txt","r+")
wordcount={}

for word in file.read().split():

    #remove alphanumeric characters and underscores
    #word = re.sub('[^\w]', '', word)
    
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        
for k,v in wordcount.items():
    print(k,v)
    #print(word,wordcount)
file.close();
