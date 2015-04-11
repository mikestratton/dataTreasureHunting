#!/usr/bin/python
file=open("id59748.txt","r+")
wordcount={}

for word in file.read().split():

    newstr = word.replace("something", "")
    
    if newstr not in wordcount:
        wordcount[newstr] = 1
    else:
        wordcount[newstr] += 1
print (newstr,wordcount)
file.close();
