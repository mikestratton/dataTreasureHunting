#!/usr/bin/python
import re
file=open("id59748.txt","r+")
wordcount={}

for word in file.read().split():

    word = re.sub('[^\w]', '', word)
    
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        
for k,v in wordcount.items():
    sorted(word, key=lambda total: total[1])
    print(k,v)
    #(word,wordcount)
file.close();
