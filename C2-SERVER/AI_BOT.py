import aiml
import pyttsx3
import sys
import os

class AI:
	
	NAME = ''
	GENDER = ''
	BRAIN_LOAD_COMMAND = ''
	BRAIN_FILEPATH = ''
	BRAIN_BUILD_XML_FILEPATH = ''
	AIML_K = aiml.Kernel()
	
	def __init__(self):
		'''
		Initial AI Initialize
		'''
		self.AIML_K = aiml.Kernel()
		
		# LOAD AI BOT BRAIN FOR OFFLINE INTERACTION
		self.LOAD_AI_BOT_BRAIN()

	# def AI_BOT_RESPONSE_(CMD):
	# 	return self.AI_BOT_RESPONSE(CMD)


	def LOAD_AI_BOT_BRAIN(self):
		'''
		Load AI BOT BRAIN
		for offline interaction
		'''

		# To increase the startup speed of the bot it is
		# possible to save the parsed aiml files as a
		# dump. This code checks if a dump exists and
		# otherwise loads the aiml from the XML files
		# and saves the brain dump.

		if os.path.exists(self.BRAIN_FILEPATH):
			self.AIML_K.loadBrain(self.BRAIN_FILEPATH)
			print("LOADED AI BRAIN: " + self.BRAIN_FILEPATH)

		else:
			print("BUILDING AIML BRAIN FROM BRAIN MAP")
			self.AIML_K.bootstrap(learnFiles=self.BRAIN_BUILD_XML_FILEPATH, commands=self.BRAIN_LOAD_COMMAND)
			self.AIML_K.saveBrain(self.BRAIN_FILEPATH)
			print("CREATED AI BRAIN: " + self.BRAIN_FILEPATH)

	def AI_BOT_RESPONSE(self, CMD):


		# Endless loop which passes the input to the bot and prints
		# its response
		try:
			response = self.AIML_K.respond(CMD)
			# print(f"{self.NAME}  --> {response}") # Response Format -> F.R.I.D.A.Y --> I am good
			return response

		except:
			return None

	def TALK(self, SPEECH):
		'''
		Pass String to generate Audio from Speaker
		for AI response
		'''
		pyttsx3.speak(SPEECH)

