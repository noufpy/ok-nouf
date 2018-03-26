#-*- coding: utf-8 -*-
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

files = os.listdir("corpus/")

# conv = open('./corpus/chat.txt','r').readlines()
# me = open('./corpus/me.txt','r').readlines()

# Create a new instance of a ChatBot
# nouf = ChatBot(
#    "Nouf",
#    storage_adapter="chatterbot.storage.SQLStorageAdapter",
#    logic_adapters=[
#        {
#             'import_path': 'chatterbot.logic.BestMatch'
#         },
#         {
#             'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#             'threshold': 0.90,
#             'default_response': 'I am sorry, but I do not understand.'
#         }
#    ],
#    input_adapter="chatterbot.input.TerminalAdapter",
#    output_adapter="chatterbot.output.TerminalAdapter",
#    #database="../database.db"
# )

nouf = ChatBot(
   "Nouf",
   storage_adapter="chatterbot.storage.SQLStorageAdapter",
   logic_adapters=[
        {
           #"chatterbot.logic.MathematicalEvaluation",
           # "chatterbot.logic.TimeLogicAdapter",
           #"chatterbot.logic.BestMatch"
           'import_path': 'chatterbot.logic.BestMatch'
           #'default_response': 'I am sorry, but I do not contain this in my memory'
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
#nouf.set_trainer(ChatterBotCorpusTrainer)
nouf.set_trainer(ListTrainer)

for f in files:
    data = open('corpus/' + f,'r').readlines()
    nouf.train(
        data
    )

# nouf.train(
# conv
#     #"chatterbot.corpus.english.testing"
#     #"./data/convert.txt",
# )
#
# nouf.train(
#     me
#     #"chatterbot.corpus.english.me"
#     #"./data/convert.txt",
# )

while True:
   try:

       bot_input = nouf.get_response(None)
       # print ('chatterbot.output.TerminalAdapter')

   # Press ctrl-c or ctrl-d on the keyboard to exit
   except (KeyboardInterrupt, EOFError, SystemExit):
       break
