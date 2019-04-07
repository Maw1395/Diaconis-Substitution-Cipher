from collections import Counter
import operator
from math import log
import re
def bigram(inputfile,outputfile=None):
    try:
    	warP=open(inputfile,'rb').read()
    except:
	warP=inputfile
    warP=" ".join(warP.split())
    warP="".join(re.findall('^[a-z]+ | [a-z]+|[a-z]+',warP))
    #print warP
    cnt=Counter()
    for i in range(len(warP)-1):
	    first=warP[i]
	    second=warP[i+1]
    	    cnt[first + second] += 1
    cnt=cnt.most_common()
    dictionary={}
    for i in cnt:
            frequency=(i[1])#*1.0/(len(warP)-1))
            log1=frequency
            dictionary[i[0]]=log1
    dictionary1=sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    #print dictionary
    if outputfile!=None:
        bi=open(outputfile,'wb')
        for i in dictionary1:
                string = i[0] + ":" + str(i[1]) + "\n"
                bi.write(string)	
    return dictionary
def main():
    bigram("war-and-peace.txt", "Bigram.txt")
    
if __name__=="__main__":
    main()
