try:
    import sys
    import subprocess
    import urllib
    import os
    import json
    import time
    import shutil
    from urllib.request import Request, urlopen
except:
    print("Cant import modules. Please retry.")


def Clear():
    os.system('cls')


os.system('cls' if os.name == 'nt' else 'clear')


def check(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


net = check("http://google.com")
net1 = check("http://yahoo.com")

if net == True or net1 == True:
    pass
else:
    os.system("say 'Not connected to the internet. Please try again'")
    print("Not connected to the internet. Please try again")
    sys.exit()

try:
    import pyttsx3
    import speech_recognition as sr
except:
    try:
        print("Importing modules please wait. \n")
        import pipwinx

        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyttsx3'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'SpeechRecognition'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyaudio'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord-webhook'])
        import pyttsx3
        import speech_recognition as sr
        from discord_webhook import DiscordWebhook
        import pyaudio
        import pipwin
    except:
        os.system("say 'Error importing modules. Please try again.'")
        print("Error importing modules. Please try again")
try:
    cwd = os.getcwd()
    questions_path = os.path.join(cwd, "questions.question")

    f = open(questions_path, "r")
    questions = f.readlines()
except:
    os.system("Error loading question files. Please try again")
    print("Error loading question files. Please try again.")
    sys.exit()

try:
    config_path = os.path.join(cwd, "config.json")

    with open(config_path, "r") as jsonfile:

        data = json.load(jsonfile)

    form_name = data['form_name']
    num_of_questions = data['num_of_questions']
    speaking_time = data['speaking_time']
    webhook = data['webhook']
except:
    os.system("Error loading config files. Please try again")
    print("Error loading config files. Please try again.")
    sys.exit()

r = sr.Recognizer()
engine = pyttsx3.init()
answers = []

def speak(say):
    engine.say(say)
    engine.runAndWait()
    engine.stop()


def sleep(time):
    time.sleep(time)



def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak
def ListeningAudio():
    while (1):



        try:

        # use the microphone as source for input.
            with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)


                audio2 = r.listen(source2)


                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()


                SpeakText(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured in listening audio")



# To make the code look neater and eaiser to type

speak("You are filling the Form " + str(form_name))
speak("You will be given " + str(speaking_time) + " seconds for each question")

speak("There are" + str(num_of_questions) + "questions")




answer_folder_text = os.path.join(cwd, "AnswersText")
os.mkdir(answer_folder_text, 0o777)

def ask_questions():
    for i in range(num_of_questions):
        speak("Question" + str(i + 1))
        speak(questions[i])
        with sr.Microphone() as source:

            r.adjust_for_ambient_noise(source, duration=0.2)

            audio = r.listen(source)
            answer = r.recognize_google(audio)
            #Writing the text
            answer_path_text = "answer" + str(i)
            answer_path_text = os.path.join(answer_folder_text, answer_path_text + ".txt")
            answer_file_text = open(str(answer_path_text), "w")
            answer_file_text.write(answer)

ask_questions()

