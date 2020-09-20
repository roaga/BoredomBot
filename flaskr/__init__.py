from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
from chatterbot import ChatBot

# Create a new instance of a ChatBot
bot = ChatBot(
    'BoreBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            'default_response': ("Perhaps you should do a little more thinking and" 
                                " be more targeted in figuring out your own mind and purpose."),
            'maximum_similarity_threshold': 0.70
        }
    ],
    database_uri='sqlite:///../database.db'
)

# Start program
print("I'm guessing you're bored...")
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
 
 
if __name__ == "__main__":
    app.run()