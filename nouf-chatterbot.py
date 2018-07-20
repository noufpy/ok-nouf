#-*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

files = os.listdir("corpus/")

### CHATTERBOT - untrained instance of chatbot
# initializing chat bot 
nouf = ChatBot(
   "Nouf",
   storage_adapter="chatterbot.storage.SQLStorageAdapter",
   logic_adapters=[
        {
           "chatterbot.logic.MathematicalEvaluation",
           "chatterbot.logic.TimeLogicAdapter",
           'import_path': 'chatterbot.logic.BestMatch'
           'default_response': 'I am sorry, but I do not contain this in my memory'
       },
       {
           'import_path': 'chatterbot.logic.LowConfidenceAdapter',
           'threshold': 0.80,
           'default_response': 'lol'
       }
   ],
   input_adapter="chatterbot.input.TerminalAdapter",
   output_adapter="chatterbot.output.TerminalAdapter"
)

# setting trainer for chatbot as list style 
nouf.set_trainer(ListTrainer)

# training chatbot on my data
for f in files:
    data = open('corpus/' + f,'r').readlines()
    nouf.train(
        data
    )
   
# chatbot waiting for questions and giving responses
while True:
   try:

       bot_input = nouf.get_response(None)
       # print ('chatterbot.output.TerminalAdapter')

   # Press ctrl-c or ctrl-d on the keyboard to exit
   except (KeyboardInterrupt, EOFError, SystemExit):
       break
