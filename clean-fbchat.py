import nltk
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
links = []

files = os.listdir("corpus/")

### CLEANING FACEBOOK MESSAGES FROM YOUTUBE LINKS, SYMBOLS, FILE EXTENSIONS ETC 
for f in files:
    list_sentences = {}
    list_replace = {}
    encoded_messages = []
    messages = open("corpus/" + f,'r').readlines()

    for message in messages:
        encoded_messages.append(unicode(message,errors='ignore'))

    messages = encoded_messages

    # extracting links from messages I have sent using regex and saving them in a seperate file
    for message in messages[1:len(messages):2]:
        url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        find = re.findall(url, message)
        if find:
            links.append(str(find) + '\n')
    
    # extracting links sent to me using regex and removing them
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

    # cleaning up random apostrophes, spaces, etc
    for message in messages:
        apostrophe = message.replace('&#039;', "'")
        spaces = apostrophe.replace('.  ', "")
        heart = spaces.replace('&lt;', "<")
        quote = heart.replace('&quot;', "'")
        at = quote.replace('&#064;', "@")
        question = at.replace('?.', "?")
        # sad = space.replace(':(.', ":(")
        # smiley = sad.replace(':).', ":)")
        if question:
            i = messages.index(message)
            message = question
            messages.pop(i)
            messages.insert(i,message)

    # cleaning up html tags
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

    # Using NLTK, extracting questions sent to me
    for message in messages[::2]:
        #print message
        list_sentences[messages.index(message)] = nltk.sent_tokenize(message)

    for sentences in list_sentences.items():
        for sentence in sentences[1]:
            words = nltk.word_tokenize(sentence)
            num = words.count('?')
            if num > 1:
                words.remove('?')

            for word in words:
                if word == '?' and sentences[0] not in list_replace:
                    #print sentence
                    #list_replace.append(sentence)
                    list_replace[sentences[0]] = sentence + " "
                elif word == '?' and sentences[0] in list_replace:
                    list_replace[sentences[0]] += sentence + " "
    # replacing those sentences with just the question asked
    for index in list_replace.items():
        messages.pop(index[0])
        messages.insert(index[0],index[1]+ '\n')
    #print messages
    # print "finished cleaning up file: " + str(f)
    # print messages
    # rewriting file with cleaned version
    with open("corpus/" + f, 'w') as file:
        file.writelines( messages )

# saving links extracted to another file
with open("links/links.txt", 'w') as file:
    file.writelines( links )
