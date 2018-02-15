import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
   
try:
    print('Google thinks you said:\n' +r.recognize_google(audio))

except:
    pass

