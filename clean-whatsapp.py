import nltk
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
links = []

### CLEANING WHATSAPP FILES FROM YOUTUBE LINKS, SYMBOLS, FILE EXTENSIONS ETC
files = os.listdir("whatsapp-corpus/")

for f in files:
    list_sentences = {}
    list_replace = {}
    encoded_messages = []
    messages = open("whatsapp-corpus/" + f,'r').readlines()

    for message in messages:
        encoded_messages.append(unicode(message,errors='ignore'))

    messages = encoded_messages

    # extracting links from messages I have sent using regex and saving them in a seperate file
    for message in messages[1:len(messages):2]:
        url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[\w.,@?^=%&:/~+#-][\w@?^=%&/~+#-]))+'
        find = re.findall(url, message)
        if find:
            links.append(str(find) + '\n')
    
    # extracting links sent to me using regex and removing them
    for message in messages:
        url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]))+'
        find = re.findall(url, message)
        if find:    # only do this for question lines... OkNouf can reply links
            i = messages.index(message)
            new = re.sub(url, '.', message)
            # if new == '.': then delete the line and the next one
            message = new
            messages.pop(i)
            messages.insert(i,message)

    # extracting file extensions and removing them
    for message in messages:
        tag = "[-\w]+.(?:jpg|gif|png|mp4|pdf|opus)+(.*?)\>"
        extension = re.findall(tag, message)
        if extension:
            i = messages.index(message)
            new = re.sub(tag, '', message)
            message = new
            messages.pop(i)
            messages.insert(i,message)

    # extracting date and time stamps
    for message in messages:
        tag = "\[(.*?)\: "
        find = re.findall(tag, message)
        if find:
            #print find
            i = messages.index(message)
            new = re.sub(tag, '', message)
            message = new
            messages.pop(i)
            messages.insert(i,message)

    # Using NLTK, extracting questions sent to me
    for message in messages[::2]:
        list_sentences[messages.index(message)] = nltk.sent_tokenize(message)

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
    #replacing those sentences with just the question asked
    for index in list_replace.items():
        #print index[0]
        messages.pop(index[0])
        messages.insert(index[0],index[1]+ '\n')
    #rewriting file with cleaned version
    with open("whatsapp-corpus/" + f, 'w') as file:
        file.writelines( messages )
        print "finished cleaning up"
        
#saving links extracted to another file 
with open("links/whatsapp-links.txt", 'w') as file:
    file.writelines( links )
