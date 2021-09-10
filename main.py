from urllib.parse import quote_plus
import pyttsx3
import random
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio) 
    
    engine.runAndWait() 
    
questions = open("questions.txt", "r")

allquestions = questions.read().split(":")

j = -1
# print(allquestions[1])
total_percentage = []
print(len(allquestions))
for i in allquestions:
    j+=1

    question_to_speak = i
    print(question_to_speak)
    speak(question_to_speak)
    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
    correct_match = 0
    query = takeCommand()
    # print(f"query: {query}")
    for i in query.split(" "):
        global total_match
        
        answers = open("answers.txt", "r")
        answers_read = answers.read().split(":")[j].split(" ")
        total_match = len(answers_read)
        # print(f"correct answers list: {answers_read}")
        # print(f"your spoken word: {i}")
        if i.lower() in answers_read:
            correct_match+=1
            
    percentage = round(correct_match/total_match * 100)
    speak(f"{percentage}% correct answer in this question! now coming to next one")
    total_percentage.append(percentage)
totalone = len(allquestions) * 100
total_percentage = sum(total_percentage)
total_pre = int(round((total_percentage/totalone) * 100))

print(total_pre)
if percentage>70:
    speak(f"Hey you have learned perfectly with a total percentage of {total_pre}%, nothing to worry about tution teacher")
    print(f"Hey you have learned perfectly with a total percentage of {total_pre}%, nothing to worry about tution teacher")
if percentage<50 and percentage>30:
    speak(f"Bro you have learned but not at that extent because your total percentage is only {total_pre}%, just revise it once")
    print(f"Bro you have learned but not at that extent because your total percentage is only {total_pre}%, just revise it once")
if percentage<30:
    speak(f"Bro! You have to thorougly learn it, you haven't learned it perfectly because your percentage is only {total_pre}")
    print(f"Bro! You have to thorougly learn it, you haven't learned it perfectly because your percentage is only {total_pre}")


