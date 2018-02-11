# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer



# Create a new instance of a ChatBot
bot = ChatBot(
    "Nouf",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        # "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)
bot.set_trainer(ChatterBotCorpusTrainer)
# print("Type something to begin...")
# conversation = open('conversations/me.yml','r').readlines()
#print(conversation)

bot.train(
    "chatterbot.corpus.english.me"
)

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)
        # print ('chatterbot.output.TerminalAdapter')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
