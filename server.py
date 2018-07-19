# -*- coding: UTF-8 -*-
from bottle import Bottle, run, static_file, request, abort
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
import sys
import os

print("Nouf.io--")

### FUNCTION DEFINITIONS 
# assigning words given a vector point. Basically drawing it on euclidean graph
def vec(s):
    return nlp.vocab[s].vector

# cosine similarity between two vectors (two words)
def cosine(v1, v2):
    if(norm(v1) > 0 and norm(v2) > 0):
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

# returning closest word
def spacy_closest(token_list, vec_to_check, n=10):
    return sorted(token_list, key=lambda x: cosine(vec_to_check, vec(x)), reverse=True)[:n]

# returning vector point for sentence. Taking the average of the vector points for each word in the sentence
def sentvec(s):
    sent = nlp(s)
    return meanv([w.vector for w in sent])

# average vector distance
def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0])
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean

# returning closest sentence 
def spacy_closest_sent(space, input_str, n=10):
    input_vec = sentvec(input_str)
    return sorted(space, key=lambda x: cosine(np.mean([w.vector for w in x], axis=0), input_vec), reverse=True)[:n]

# custom function to call for every analysis
def analyzeInput(user_question):
    # question analysis
    new = []
    #user_question = unicode(user_question, 'utf-8')
    for sent in spacy_closest_sent(questions, user_question):
        new.append(sent.text)
    # response printing
    now = new[0]
    if now:
        #print "original question: ", now
        find = [item for item in questions_str if now in item]
        #print "options: ", find
        #index = questions_str.index[now]
        # print index
        # print find[0][1]
        return find[0][1]
        #print answers[index]
        del new[:]


### INITIALIZATIONS
print("-- nouf.io initializing")
questions = []
questions_str = []
answers = []
answers_str = []
new = []


### PROGRAM FLOW
# load spacy library and file
nlp = spacy.load('en_core_web_lg')
files = os.listdir("testing/")

for f in files:
    #document = open("corpus/me.txt",'r').readlines()
    document = open("testing/" + f,'r').readlines()
    #print("-- file loaded")

    # spacy load: questions + answers
    i = 0
    for line in document[::2]:
        sentence = line
        sentence_spacy = nlp(sentence.decode('utf8'))
        questions.append(sentence_spacy)
        if i < len(document)-1:
            sentence_next = document[i+1]
            #questions_str[unicode(sentence, "utf-8")] = sentence_next
            questions_str.append((unicode(sentence, "utf-8"), (unicode(sentence_next, "utf-8"))))
            i+=2

print("-- files loaded")

### QUESTIONCYCLE - terminal testing 
# user_input = ""
# while(user_input != 'Q'):
#     user_input = raw_input("Ask Nouf.io something: ")
#     # print(type(user_input))
#     # user_input = str(user_input)
#     if user_input == "quit":
#         break
#     else:
#         analyzeInput(user_input)

### INITIALIZING SERVER
app = Bottle()
# socket connection
@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    #always running socket in while loop until you close client
    while True:
        try:
            #receive socket - receiving input/question from user and sending it to server to conduct vector math 
            message = wsock.receive()
            if message:
                print "User: ", message
                # analyzing vector points for sentence 
                answer = analyzeInput(message)
                print "Nouf.io: ", answer
                #after analyzing closest vector point, it sends socket with the answer to the client 
                wsock.send(answer)
        except WebSocketError:
            break

#serving html file
@app.route('/')
def server_static():
    return static_file('landing.html', root='/Users/noufaljowaysir/github/ok-nouf/static/')

#serving all files in folder 'static'
@app.route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/Users/noufaljowaysir/github/ok-nouf/static/')

#attaching socket to server
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
server = WSGIServer(("localhost", 8050), app,
                    handler_class=WebSocketHandler)
print("-- server started")
server.serve_forever()
