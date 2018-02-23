import nltk
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

list_sentences = {}
list_replace = {}
links = []

messages = open('./corpus/chat.txt','r').readlines()

encoded_messages = []

for message in messages:
    encoded_messages.append(unicode(message,errors='ignore'))

messages = encoded_messages

# CLEANING UP LINKS
# SAVING MY OWN LINKS IN A SEPARATE FILE

for message in messages[1:len(messages):2]:
    url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    find = re.findall(url, message)
    if find:
        links.append(find)
#print links

for message in messages:
    url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    find = re.findall(url, message)
    if find:    # only do this for question lines... OkNouf can reply links
        i = messages.index(message)
        new = re.sub(url, '.', message)
        # if new == '.': then delete the line and the next one
        message = new
        messages.pop(i)
        messages.insert(i,message)

# CLEANING UP HTML TAGS

for message in messages:
    tag = """</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[\^'">\s]+))?)+\s*|\s*)/?>"""
    find = re.findall(tag, message)
    if find:
        #print find
        i = messages.index(message)
        new = re.sub(tag, '.', message)
        message = new
        messages.pop(i)
        messages.insert(i,message)

# FINDING QUESTIONS

for message in messages[::2]:
    #print message
    list_sentences[messages.index(message)] = nltk.sent_tokenize(message)
    #list_sentences.append(nltk.sent_tokenize(message))

#print list_sentences

for sentences in list_sentences.items():
    #print sentences[1]
    for sentence in sentences[1]:
        words = nltk.word_tokenize(sentence)
        num = words.count('?')
        if num > 1:
            words.remove('?')
        #print words
        #print num
        for word in words:
            if word == '?' and sentences[0] not in list_replace:
                #print sentence
                #list_replace.append(sentence)
                list_replace[sentences[0]] = sentence + " "
            elif word == '?' and sentences[0] in list_replace:
                list_replace[sentences[0]] += sentence + " "
#print list_replace

for index in list_replace.items():
    #print index[0]
    messages.pop(index[0])
    messages.insert(index[0],index[1]+ '\n')
#print messages

with open('./corpus/chat.txt', 'w') as file:
    file.writelines( messages )
