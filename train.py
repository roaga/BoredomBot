from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os
from csv import reader

# Create a new instance of a ChatBot
bot = ChatBot(
    'BoreBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

# Read training data from file
lists = []
with open('trainingdata.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        lists.append(row)

# Train the bot
trainer = ListTrainer(bot)
for list in lists:
    trainer.train(list)