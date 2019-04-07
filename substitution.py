from bigram import bigram
import string
import operator
import re
import math
import random
from collections import Counter
def get_war_and_peace():
	count=0
	lines=open("Bigram.txt",'rb')
	line=lines.readline().strip()
	dict1={}
	while(line):
		two=line.split(':')[0]
		two=two.replace('ENT','\n')
		value=line.split(':')[1]
		dict1[two]=value
		#print two, value
		line=lines.readline().strip('\n')
	return dict1

def firstguess(input1):
	monograms=['e','t','a','o','i','n','s','h','r','l','d','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
	#print len(monograms)
	cnt=Counter()
	for i in input1:
		if i!=' ':
			cnt[i]+=1
	cnt=sorted(cnt.items(), key=operator.itemgetter(1),reverse=True)
        #print cnt
	letters={}
	c=0
	for i in cnt:
		letters[i[0]]=monograms[c]
		c+=1
	print letters
	for i in range(26-len(cnt)):
		for j in monograms:
			#print j
			if j not in letters:
				for k in monograms:
					if k not in input1:
						letters[j]=k
						continue
        print letters
	return letters


def score(input1, bigramWarP):
	#input1=open("testOutput.txt",'rb').read()
	#input1="".join(re.findall("[a-z]+ ",input1))
	finalscore=1
	inputBigram=bigram(input1)
	#print inputBigram
	k=[]
	for j in inputBigram:
		k.append(j)
	for i in k:
		if i in bigramWarP:
			#print i
			
			multiplier=math.log(float(inputBigram[i])*float(inputBigram[i]),2)*(math.log(float(bigramWarP[i]),2))
			if multiplier!=0:
				finalscore*=multiplier
			#print finalscore
			#print finalscore
		else:
			finalscore/=4
		#finalscore/=5
	#print finalscore
	return finalscore


def substiution():
    #wordlist=words()
    bigramInput=bigram("testInput.txt")
    bigramWarP=get_war_and_peace()
    #print bigramWarP['nv']
    letters=string.ascii_lowercase
    lettersDict={}
    for i in letters:
    	lettersDict[i]=i
    Input=open("testInput.txt",'rb').read()
    Input=" ".join(Input.split())
    Input="".join(re.findall('^[a-z]+ | [a-z]+|[a-z]+',Input))
    #print Input
    Input=re.sub('[^a-z] +','',Input)
 
    output=''
    for i in Input:
        if i in string.ascii_lowercase:
	    	   output+=(lettersDict[i])
        else:
            output+=" "
    #print output
    keys=[]
    keys.append(lettersDict)
    finalScore=score(output, bigramWarP)
    output1=''
    bestScore=finalScore
    finalOutput=''
    #lettersDict=firstguess(Input)
    for f in range(1000000):
    	lettersDict1={}
    	strings=""
    	#for k,v in lettersDict1.items():
    	#	strings+=v
    	#while strings in keys:
	r1=random.choice(string.ascii_lowercase)
	r2=random.choice(string.ascii_lowercase)
	#while(r1==r2):
		#r2=random.choice(string.ascii_lowercase)
	k1=lettersDict[r1]
	k2=lettersDict[r2]
	for i in lettersDict:
		if i==r1:
			lettersDict1[i]=lettersDict[r2]
		elif i==r2:
			lettersDict1[i]=lettersDict[r1]
		else:
			lettersDict1[i]=lettersDict[i]
    		#strings=""
    		#for k,v in lettersDict1.items():
    			#strings+=v
    	#keys.append(strings)
    	output=''

        for i in Input:
            if i in string.ascii_lowercase:
                output+=(lettersDict1[i])
            else:
                output+=" "
    	#print output	
        score1=score(output, bigramWarP)
	#if f%500==0:
		#print output1
    	if score1>finalScore:
    		lettersDict=lettersDict1
    		output1=output
    		finalScore=score1
		#print output1
    		#print finalScore
    		#print output
    		if score1>bestScore:
    			finalOutput=output
    			bestScore=score1
    			#print f
    			print "Iteration:", f
    			print "Output:", finalOutput
    			print bestScore
			print 
			#print lettersDict

    	elif score1>0:
			#print rand
			if random.randint(0,int(finalScore/score1)*5)==1:
				lettersDict=lettersDict1
				output1=output
				finalScore=score1
				#print 'true'
			#else:
				#print 'fail'
    	#print int(finalScore/score1)

    	#print output
    	#print score1

    #print output1
    #print finalScore



	#for i in range(10000):    

def main():
	substiution()

if __name__=="__main__":
		main()
