import aiml
import pyttsx3
import sys
import os
	
NAME = ''
GENDER = ''
BRAIN_LOAD_COMMAND = ''
BRAIN_FILEPATH = ''
BRAIN_BUILD_XML_FILEPATH = ''
AIML_K = aiml.Kernel()



def LOAD_AI_BOT_BRAIN():
	'''
	Load AI BOT BRAIN
	for offline interaction
	'''

	# To increase the startup speed of the bot it is
	# possible to save the parsed aiml files as a
	# dump. This code checks if a dump exists and
	# otherwise loads the aiml from the XML files
	# and saves the brain dump.

	if os.path.exists(BRAIN_FILEPATH):
		AIML_K.loadBrain(BRAIN_FILEPATH)
		print("LOADED AI BRAIN: " + BRAIN_FILEPATH)

	else:
		print("BUILDING AIML BRAIN FROM BRAIN MAP")
		AIML_K.bootstrap(learnFiles=BRAIN_BUILD_XML_FILEPATH, commands=BRAIN_LOAD_COMMAND)
		AIML_K.saveBrain(BRAIN_FILEPATH)
		print("CREATED AI BRAIN: " + BRAIN_FILEPATH)

def AI_BOT_RESPONSE(CMD):


	# Endless loop which passes the input to the bot and prints
	# its response
	try:
		response = AIML_K.respond(CMD)
		# print(f"{self.NAME}  --> {response}") # Response Format -> F.R.I.D.A.Y --> I am good
		return response

	except:
		return None

def TALK(SPEECH):
	'''
	Pass String to generate Audio from Speaker
	for AI response
	'''
	pyttsx3.speak(SPEECH)

LOAD_AI_BOT_BRAIN()