import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

files = os.listdir("whatsapp-corpus/")

### CLEANING UP WHATSAPP CONVOS
for f in files:
    messages = open ("whatsapp-corpus/" + f, "r").readlines()
    senders = []
    msg = ''
    i = 0

    # concatenating starts here
    while i < len(messages)-1:
        # extract sender using regex
        title = '\](.*?)\:'
        sender = re.findall(title, messages[i])
        #replace line breaks in messages with ' '
        msg += re.sub('\n', ' ', messages[i])
        #if sender sends more than one message in a row then concatenate messages together
        while sender == re.findall(title, messages[i+1]) or re.findall(title, messages[i+1]) == []:
            msg += ". " + re.sub('\n', ' ', messages[i+1])
            i += 1
            if i == len(messages)-1:
                break
        msg += "\n"
        i += 1
    #rewrite file with newly cleaned messages    
    with open("whatsapp-corpus/" + f,'w') as f:
        f.write(msg)
        print "concatenation done"
