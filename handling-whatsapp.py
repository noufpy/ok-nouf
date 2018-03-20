import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

files = os.listdir("whatsapp-corpus/")

# EXTRACTING ONLY ONE-ON-ONE CONVERSATIONS WITH ME

for f in files:
    messages = open ("whatsapp-corpus/" + f, "r").readlines()
    senders = []
    msg = ''
    i = 0

    # if len(messages) > 1:
    #     for m in messages:
    #         # finding names for file
    #         title = '\](.*?)\:'
    #         who = re.findall(title, m)
    #         for name in who:
    #             index = who.index(name)
    #             new = name.lstrip()
    #             name = new
    #             who.pop(index)
    #             who.insert(index,name)
    #             if name not in senders:
    #                 senders.append(name)

    # concacting starts here
    while i < len(messages)-1:
        title = '\](.*?)\:'
        sender = re.findall(title, messages[i])
        msg += re.sub('\n', ' ', messages[i])
        while sender == re.findall(title, messages[i+1]) or re.findall(title, messages[i+1]) == []:
            msg += ". " + re.sub('\n', ' ', messages[i+1])
            i += 1
            if i == len(messages)-1:
                break
        msg += "\n"
        i += 1
    with open("whatsapp-corpus/" + f,'w') as f:
        f.write(msg)
        print "concatenation done"
