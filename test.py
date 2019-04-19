import os
from searchword import *

path = os.getcwd() + '/notebook/' + 'word.txt'
autopath=os.getcwd()+'/auto/'+'autotranslate.txt'

wordlist=[]
fp = open(path, 'r')
wordlist = fp.readlines()
fp.close()

translatelist=[]
for i in wordlist:
    words=i.split('——')
    translatelist.append(words[0])
del(translatelist[0])

fp=open(autopath,'w')
for i in translatelist:
    fp.write(i+'——'+translate(i)+'\n')
fp.close()
