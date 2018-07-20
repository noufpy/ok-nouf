import json
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
senders = []
new_files = []

files = os.listdir("messages/")

### CLEANING UP FACEBOOK MESSAGE CONVOS
# first, extracting one-on-one conversations from corpus
for f in files:
    data = json.load(open("messages/" + f))
    messages = data["threads"][0]["messages"]
    
    # analyzing how many messages in each convo
    if len(messages) > 1:
        for m in messages:
            who = messages[messages.index(m)]["sender"]
            if who not in senders:
                senders.append(who)

    #if senders contain only two people (one is me) then extract file 
    if len(senders) == 2:
        for sender in senders:
            if senders[0] == "Nouf Aljowaysir" or senders[1] == "Nouf Aljowaysir":
                #print f
                #print senders
                del senders[:]
                new_files.append(f)
            else:
                #print f
                #print "No conversations with Nouf here"
                del senders[:]
    else:
        #print f
        #print "This is a group conversation"
        del senders[:]

print new_files

# second, cleaning up extracted files and creating a new corpus 
for f in new_files:
    data = json.load(open("messages/" + f))
    messages = data["threads"][0]["messages"]
    msg = ''
    i = len(messages) - 1

    while i > -1:
        # making Nouf messages on even numbers and other sender is on odd numbers. Concatening messages if from the same sender
    	who = messages[i]["sender"]
        if messages[len(messages)-1]["sender"] == "Nouf Aljowaysir" and i == len(messages)-1:
            msg += "\n" + re.sub('\n', ' ', messages[i]["message"])
        else:
            msg += re.sub('\n', ' ', messages[i]["message"])
        if who not in senders and who != "Nouf Aljowaysir":
            senders.append(who)
    	# if the next one(s) is(are) from the same sender, concatenate
    	if i > 0:
    		while messages[i-1]["sender"] == who:
    			msg += ". " + re.sub('\n', ' ', messages[i-1]["message"])
    			i -= 1
    			if i == 0:
    				break
    	msg += "\n"
    	i -= 1
    #print(msg)
    # rewriting messages into new corpus
    with open('./corpus/' + str(senders[0]) + '.txt','w') as f:
        f.write(msg)
        del senders[:]
#print senders
