import sys
import nltk
import operator
from nltk.corpus import stopwords
import re
import os
reload(sys)
sys.setdefaultencoding('utf-8')

### USING NLTK, ANALYZING FREQUENCY OF WORDS IN MY MESSAGES
frequency = {}
files = os.listdir("corpus/")

# stopwords - don't look for these words for frequency analysis
stopwords = set(nltk.corpus.stopwords.words('english')) | set((u'hehe', u'hmm', u'lol', u'lols', u'ill', u'haha', u'doesnt', u'ooo', u'anywhoo', u'kinda',u'might', u'didnt', u'also',
u'cause',u'thats', u'wanna',u'hes',u'well',u'still',u'ohh',u'lemme',u'since',u'lets',u'hows',u'okie',u'havent',u'cant',u'ive',u'dont',u'wanna' ))

for f in files:
    messages = open ("corpus/" + f, "r").readlines()
    
    # analyze messages sent by me 
    for message in messages[1:len(messages):2]:
        #convert word to lowercase and find words that contain between 3-15 letters 
        lowercase = message.lower()
        words = re.findall(r'\b[a-z]{3,15}\b', lowercase)
        # analyze frequency and add the word and its level of frequency to a dictionary 
        for word in words:
            if word not in stopwords:
                count = frequency.get(word,0)
                frequency[word] = count + 1
                
# print and sort dictionary from lowest to highest frequency value
for key, value in sorted(frequency.iteritems(), key=lambda (k,v): (v,k)):
    if value > 75:
        print "%s: %s" % (key, value)
