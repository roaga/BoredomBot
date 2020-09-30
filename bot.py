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
            'maximum_similarity_threshold': 0.51
        }
    ],
    database_uri='sqlite:///database.db'
)

# Start program
print("I'm guessing you're bored...")
# The following loop will execute each time the user enters input in the terminal
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break