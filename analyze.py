import sys
import nltk
import operator
from nltk.corpus import stopwords
import re
import os
reload(sys)
sys.setdefaultencoding('utf-8')

frequency = {}

files = os.listdir("corpus/")

stopwords = set(nltk.corpus.stopwords.words('english')) | set((u'hehe', u'hmm', u'lol', u'lols', u'ill', u'haha', u'doesnt', u'ooo', u'anywhoo', u'kinda',u'might', u'didnt', u'also',
u'cause',u'thats', u'wanna',u'hes',u'well',u'still',u'ohh',u'lemme',u'since',u'lets',u'hows',u'okie',u'havent',u'cant',u'ive',u'dont',u'wanna' ))

#print stopwords

for f in files:
    messages = open ("corpus/" + f, "r").readlines()
    #print len(messages)

    for message in messages[1:len(messages):2]:
        #print message
        lowercase = message.lower()
        words = re.findall(r'\b[a-z]{3,15}\b', lowercase)

        for word in words:
            if word not in stopwords:
                #print word
                count = frequency.get(word,0)
                frequency[word] = count + 1

for key, value in sorted(frequency.iteritems(), key=lambda (k,v): (v,k)):
    if value > 75:
        print "%s: %s" % (key, value)

# for words in words:
#     if frequency[words] > 99:
#         print words, frequency[words]

# nums = frequency.values()
# words = frequency.keys()
#
# m = max(nums)
#
# for word in words:
# #     if frequency[words] > 99:
#     if frequency[word] == m:
#         print word, m
