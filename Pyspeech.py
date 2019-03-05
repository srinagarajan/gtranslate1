# This is speech recognition program

import speech_recognition as sr
from googletrans import Translator
import webbrowser, os

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Speak a sentence...")
	audio = r.listen(source)
	print("Got it. Thanks....")

f = open('home1.html','w')

message1 = """<html><head><title>Translated....</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head><body>"""

# Detect the language being spoken from the audio
# This will have to be address later...

try:
	textsource = r.recognize_google(audio, language = "en-IN")
	print(f" Text from the source audio : {textsource}")
except:
	pass

# From the recorded audio source, print the text and then transalate to English
translator = Translator()

try:
	transtextT = translator.translate(textsource, dest='ta').text
	print(f"Translated text in Tamil : {transtextT}")
except:
	pass
 
try:
	transtextE = translator.translate(textsource, dest='kn').text
	print(f"Translated text in Kannada : {transtextE}")
except:
	pass

try:
	transtextH = translator.translate(textsource, dest='hi').text
	print(f"Translated text in Hindi : {transtextH}")
except:
	pass

message2 = """<div align="center"><p><i><u> Transl8r</u></i></p></div> \
<div> Text From source audio: <b> {} </b></div>""".format(textsource)

message3 = """<div> <br>Translations... <br> \

<table><tr align="center"><td> Language </td><td> Translated Text </td></tr> \
<tr align="center"><td> Tamil </td><td><b>{} </b></tr> \
<tr align="center"><td> Kannada </td><td><b>{} </b></tr> \
<tr align="center"><td> Hindi </td><td><b>{} </b></tr> \

</b></table></div>""".format(transtextT, transtextE, transtextH)
message4 = """</body></html>"""


message = message1+message2+message3+message4

f.write(message)
f.close()

# Open the html in a browser
webbrowser.open('file://' + os.path.realpath("/Volumes/Data/Pyprojects/Pyspeech/home1.html"))
