#Ovozli yordamchi Jarvis

import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

#barcha so'zlar jamlanmasi



opts = {
    "alias" : ("jarvis", "jarvis", "jar", "jorvis", "jarviz", "jorviz", "yarvis", "", "jorvez" ,"jarvez", "jarves"),
    "tbr" : ('aytingchi', "ko'rsatingchi", "ko'rsat", "korsat", "necha", "korsat", "aytchi", "nechi", "nechchi"),
    "cmds" : {
       "ctime" : ("xozirgi vaqt", "soat necha", "xozir vaqt"),
       "radio" : ("muzikani qo'y", "radioni yoq", "radiyoni qo'sh") ,
       "stupid1" : ('latifa aytib ber', "meni kuldir", "Latifa aytishni bilasanmi")
    }
}


# Funksiyalar
def speak(what):
    print(what)
    speek_engine.say(what)
    speek_engine.runAndWait()
    speek_engine.stop()



def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="uz-UZ").lower()
        print("[log] Aytildi: " + voice)
        
        if voice.startswith(opts["alias"]):
            # Jarvisga murojat
            cmd = voice

            for x in opts["alias"]:
                cmd = cmd.replace(x, "").strip()


            for x in opts["tbr"]:
                cmd = cmd.replace(x, "").strip()


            # Tekshiramiz va ishlatamiz
            cmd = recognizer_cmd(cmd)
            execute_cmd(['cmd'])
    except sr.UnknownValueError:
        print("[log] Tushunarsiz gap!") 

    except sr.RequestError as e:
        print("[log] Tushunarsiz gap!, Internetni tekshiring!")  

def recognizer_cmd(cmd):
    RC = {'cmd' : "", "percent" : 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC["percent"]:
                RC["cmd"] = c
                RC["percent"] = vrt
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        #vatni ko'rsat
        now = datetime.datetime.now()
        speak('Hozirgi vaqt ' + str(now.hour) + ":" + str(now.minute))

    # elif cmd == 'radio':
    #     #Radioni yoqish
    #     os.system("D:\\musics\\golden-hour.mp4")

    elif cmd == 'stupid1':
        #Yemagan xazil
        speak("Bitta afandi PyDev kanaliga obuna bo'lmagan ekan! proyektlari o'chib ketibdi, xa xa  xax")

# ovoz
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)


speek_engine = pyttsx3.init()

#Faqatgina biz yozgan ovozlarni!

voices = speek_engine.getProperty('voices')
speek_engine.setProperty('voice', voices[0].id)


# forced cmd test

speak('Salom Sardor')
speak("Qalesan, yaxshimisan")


stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)