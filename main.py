from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Risers")
convo = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(bot)
trainer.train(convo)
answer = bot.get_response("Good morning")
print(answer)

