
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading




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



trainer = ListTrainer(bot)

trainer.train(["Hi",
    "how can i help you?",
    "what is your name",
    "my name is bot ",
    "i'm created by risers",
    "what you can do?",
    "i can answer all Your queries about DIEMS",
    "Hello",
    "Hi there!",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",])
trainer.train(["What is CAP?",
    "Centralized Admission Process" ,
    "CAP Seats means",
    "The seats filled in through the centralized process of admission carried out by the Competent Authority",
    "Facilitation Centre (FC) means?",
    "A center where the facilities like filling online forms, verification of documents and grievances resolving are provided",
    "Deogiri Institute of Engineering and Management Studies is authorized Facilitation Centre (FC) for First Year Engineering Admission.",
    "ARC means",
    "ARC means Admission Reporting Centre where candidate must verify his/her original documents and accept the seat allotted by paying the required fees",
    "What are the Basic Eligibility Criteria for admission to First year Engineering",
    "Candidate should be Indian National and Passed HSC or its equivalent examination ",
    "marks and subjects",
    " Physics and Mathematics as compulsory subjects along with one of the Chemistry or Biotechnology or Biology or Technical Vocational subject or Computer Science or Information Technology or Informatics Practices or Agriculture or Engineering Graphics or Business Studies and obtained at least 45 % /134 marks and at least 40 %/ 119marks, in case of Backward Class categories, Economically",
    "HOW TO APPLY for admission in college?",
     "you have to coplete the councelling process first, for more information go to the official site of DIEMS",
    "what are the COLLEGE ADMISSION REQUIREMENTS?",
    "you have to allocate the college by college allotment process,visit for more at https://www.dietms.org/",
    "WHAT IF A STUDENT FAILS TO REGISTER FOR THE SELECTION ROUNDS BEFORE THE DEADLINE?",
    "you can take the admission at the college level without selection round",
    "what are the facilities provided by the college?",
    "High Speed Internet Connectivity, Computer Centre, Auditorium, Library, E-Journals,Medical Facility, Sports, Cafeteria.",
    "how are the faculties?",
    "Highly experienced, dedicated and motivating Faculty Members are here!",
     "is any scholership is offered by college?",
    "yes, All scholarships, free ships offered by the Government are available.",
    "what are the programs are offered by the institute?",
    "State of art laboratories for Civil, Mechanical, Electronics, Computer, Drawing Hall, Electrical, Sprawling Workshop & Tools.",
    "where can the out of city students can live there?",
    "Well furnished independent hostels for boys & girls in the campus providing all amenities are there!.",
    "how can i contact to the isntitute?",
    "you can mail on admin@dietms.org or call on 0240-2367546",
    "when the institute is founded?",
    "in 2009-2010",
    "tell the details about institute/DIEMS",
    "DIEMS is very prestigious college under dbatu, visit dietms.org for more details.",
    "why should i take admission in diems?",
    "DIEMS provides excellent academic results and placements and trainings since 2009 and much more facilities are here.",
    "address of DIEMS",
    "Deogiri Institute of Engineering and Management Studies, Railway Station Road, Aurangabad – 431005.",
    "what is the vision of institute",
    "Nation building by creating opportunities for rural and urban students through excellence in education and research in the field of Engineering and Management.",
    "what is the mission of institute?",
    "To prepare the students to face global challenges by equipping them with requisite technical expertise and developing entrepreneurship skills among them.",
    "objective of the institute?",
    "To achieve excellence in academic, overall development of students, and To support for placement and entrepreneurship development.",
    "what are the varies commities are there?",
    "1. Anti Ragging Committee 2.Committee For SC/ST 3.Grievance Redressal  Committee 4.Internal Complaints Committee",
    "Objectives of industry cells",
    "To organize in-plant training for the students and provide internships for students in industries",
    " what are the institutional values?",
    "Discipline,COMMITMENT,RESPONSIBLITY,EXCELLENCE,INTEGRITY,HONESTY",

    "what is the internal assessment criteria of first and secon semester?",
    " go to the site and download the criteria ->https://www.dietms.org/first-year-engineering-2/",
    "cousrse outcome of first year",
    "to get teh details about it, visit our site https://www.dietms.org/first-year-engineering-2/",
    "list of the faculties in computer science(CSE department)",
    "visit the site for more details https://www.dietms.org/computer-science-and-engineering/",
     "what are the program outcomes of mechanical engineering?",
    "Mechanical engineering graduates would be able to excel in the field of mechanical engineering",
    "list of faculties in mechanical engineering department",
    "visit https://www.dietms.org/mechanical-engineering/ for details about faculties",
    "what is TATA ready engineer program in mechanical engineering?",
    "this program provides the industrial skill development platform for mechanical students.",
    "what are the program outcomes of civil engineering?",
    "Within four years of graduation, students will be well prepared for the industrial problems and become job ready.",
    "list of civil engineering faculties",
    "https://www.dietms.org/civil-engineering/ visit the site",
    "what is the rate of placement?",
    "DIEMS provides the great opportunities of training and placements, the maximumpackage of the campus placement goes to 11LPA.",
    "what is IQAC methodology?",
    "Academic Plan,schedule,Feedback from Stakeholders of each course Result analysis. Incorporating CRT for final year students.",
    "what is the PBL about?",
     "its Promoting Project Based Learning Methodology through Continuous Assessment.",
    "what are the e-learning resources provided by the college? ",
    "to find all the e-resources provided by the college, go to the site https://www.dietms.org/e-resources/",

])
main=Tk()

main.geometry("600x650")
main.title("risers")
img=PhotoImage(file="img_1.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

def takequery():
    sr = s.Recognizer()

    sr.pause_threshold=1
    print("your bot is listening.....")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language="eng-in")
            print(query)

            textF.delete(0, END)
            textF.insert(0, query)
            Ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognise")

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
msgs.pack(side=LEFT,fill=BOTH,pady=20)
frame.pack()

textF=Entry(main,font=("Cooper Black",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Send",font=("Arial Rounded MT Bold",20), command=Ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)
def repeatl():
    while True:
        takequery()
t=threading.Thread(target=repeatl)

t.start()
main.mainloop()
