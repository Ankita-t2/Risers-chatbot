from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
#engine.setProperty('voice',voices.id)
for voice in voices:
   engine.setProperty('voice', voice.id)
def speak(word):
     engine.say(word)
     engine.runAndWait()
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
#answer = bot.get_response("Good morning")
#print("Talk to bot")
#while True:
#   query=input()
 #   if query=='exit':
 #       break
  #  answer= bot.get_response(query)
   # print("bot :",answer)
main=Tk()

main.geometry("500x650")
main.title("risers")
img=PhotoImage(file="img.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
def Ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : "+query)
    print(type(Ask_from_bot))
    msgs.insert(END,"bot :"+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textF=Entry(main,font=("verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="ask from bot",font=("vardana",20), command=Ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)
main.mainloop()
