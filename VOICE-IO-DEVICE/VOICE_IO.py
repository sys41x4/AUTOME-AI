import os, subprocess
import sys
import re
import time
import json
import toml
from playsound import playsound
import pyttsx3
from threading import Thread, Event
import speech_recognition as sr


import http.client, urllib.parse
from ping3 import ping


# LOCAL MODULE IMPORTS #
from AI_BOT import AI

# OFFLINE VOICE RECOGNITION
# https://cmusphinx.github.io/wiki/
# https://snowboy.kitt.ai/

#################



class AI__DATA:
    '''
        AI Information
    '''

    NAME = ''
    GENDER = ''
    TRIGGER_WORDS = ''
    AI_TRIGGER_SOUND_FILEPATH=''
    SYSTEM_COMMANDS = ''
    def __init__(self):
        '''
        INITIAL ASSESSMENT
        '''

    def start(self):
        '''
        START TRIGGER
        '''

AI = AI__DATA()

class CLIENT__DATA:
    '''
        YOUR INFORMATION TO USE
    '''

    UUID=''
    EMAIL=''
    FULL_NAME = ''
    USERNAME=''
    PASSWORD=''

    DEVICE_ID=''
    DEVICE_PUBLIC_KEY=''
    DEVICE_PRIVATE_KEY='' 
    

    def __init__(self):
        '''
        LOAD USER IDENTIFIERS
        '''
    def start(self):
        '''
        '''

CLIENT_DATA = CLIENT__DATA()

class CRYPTO:
    '''
    CRYPTOGRAPHY Functions
    '''

    def __init__(self):
        '''
            INITIAL ASSESSMENT
        '''

    def start(self):
        '''
        START FUNCTION
        '''

    def str2json(self, DATA):
        return json.loads(DATA)

CRYPTOGRAPHY = CRYPTO()

class SERVER__COMMUNICATION:
    '''
        CLASS to Communicate with the hosted
        Command & Control Server
    '''
    VOICE_RECOGNITION_ENDPOINT = ''
    AI_COMMUNICATION_ENDPOINT=''
    SERVER_COMMUNICATION_ENDPOINTS = []

    def __init__(self):
        '''
        INITIAL ASSIGNMENT
        '''

        # print(self.SERVER_COMMUNICATION_ENDPOINT)
        # print(self.SERVER_COMMUNICATION_ENDPOINTS)

    def start(self):
        self.SERVER_COMMUNICATION_ENDPOINTS = re.findall(r'(http|https|ftp):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', self.VOICE_RECOGNITION_ENDPOINT+" "+self.AI_COMMUNICATION_ENDPOINT)

    def VOICE_RECOGNITION_CONNECTION_TESTING(self, DOMAIN_ADDRESS=None):
        if(DOMAIN_ADDRESS==None):

            # DOMAIN_ADDRESS=self.SERVER_IP
            DOMAIN_ADDRESS=SERVER_COMMUNICATION_ENDPOINTS[0][1]
        return 1 # Temporary Resolution
        
        if (ping(DOMAIN_ADDRESS)!=False):
        # if (ping(DOMAIN_ADDRESS)==True or ping(DOMAIN_ADDRESS)==0.0):
            return 1
        else:
            print("VOICE RECOGNITION SERVER NOT REACHABLE")
            return 0

    def AI_CONNECTION_TESTING(self, DOMAIN_ADDRESS=None):
        if(DOMAIN_ADDRESS==None):

            # DOMAIN_ADDRESS=self.SERVER_IP
            DOMAIN_ADDRESS=SERVER_COMMUNICATION_ENDPOINTS[1][1]
        return 1 # Temporary Resolution
        if (ping(DOMAIN_ADDRESS)!=False):
        # if (ping(DOMAIN_ADDRESS)==True or ping(DOMAIN_ADDRESS)==0.0):
            return 1
        else:
            print("AI SERVER NOT REACHABLE")
            return 0

    def HTTP_CONNECTION_HANDLER(self, PROTOCOL, REQUEST_TYPE, domain, subdirectory_location, TIMEOUT=10):

        if PROTOCOL.lower()=='https':
            conn = http.client.HTTPSConnection(domain, timeout=TIMEOUT)
        elif PROTOCOL.lower()=='http':
            conn = http.client.HTTPConnection(domain, timeout=TIMEOUT)

        if REQUEST_TYPE.upper()=="GET":
            conn.request("GET", subdirectory_location)
            
        response = conn.getresponse()
        # response.close()
        conn.close()

        return {"code":response.code, "status":response.status, "data":response.read().decode()}

    def VOICE_RECOGNITION_COMMUNICATE(self, DATA):
        try:
            return CRYPTOGRAPHY.str2json(self.HTTP_CONNECTION_HANDLER(self.SERVER_COMMUNICATION_ENDPOINTS[0][0], "GET", self.SERVER_COMMUNICATION_ENDPOINTS[0][1], self.SERVER_COMMUNICATION_ENDPOINTS[0][2]+"/"+urllib.parse.quote(DATA))["data"])
        except:
            return None

        return None

    def AI_COMMUNICATE(self, DATA):

        try:
            return CRYPTOGRAPHY.str2json(self.HTTP_CONNECTION_HANDLER(self.SERVER_COMMUNICATION_ENDPOINTS[1][0], "GET", self.SERVER_COMMUNICATION_ENDPOINTS[1][1], self.SERVER_COMMUNICATION_ENDPOINTS[1][2]+"/"+urllib.parse.quote(DATA))["data"])
        except:
            return None

        return None

    def PUSH(self, PROTOCOL, DATA):
        '''
        '''
        # if PROTOCOL=="HTTP":
        #     self.HTTP_PUSH(DATA)


SERVER_COMMUNICATION = SERVER__COMMUNICATION()
          




# class AUDIO_CONTROLS:

#     PHRASE_TIME_LIMIT = 4 # IN SECONDS | RECOGNIZER WILL WAIT UNTIL PHRASE_TIME_LIMIT SECONDS


#     def __init__(self):
#         '''
#         '''


    # def 

class SPEECH__RECOGNIZER:

    PHRASE_TIME_LIMIT = 4

    def __init__(self):
        '''
            INITIALIZE RECOGNIZER
        '''

        # self.r = sr.Recognizer()
    def start(self):
        self.r = sr.Recognizer()

    def SPEECH_2_TEXT(self):
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
        # if (SERVER_COMMUNICATION.CONNECTION_TESTING(SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[0][1])):
        with sr.Microphone() as source:
        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source, phrase_time_limit=self.PHRASE_TIME_LIMIT)
            #print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            
            try:
                # using google speech recognition | with DEMO KEY inbuilt
                command = self.r.recognize_google(audio)
                return (command)
            except:
                return None
        

SPEECH_RECOGNIZER = SPEECH__RECOGNIZER()
# def filter_command():

#     #while True:
#     # USE Dual Recognization
#     # 0: AI NAME CALL
#     # 1: Command to provide

#     recognized_text = speech_recognizer.speech_2_text().upper() # For recognizing the voice to perform task


#     print(f"{commands_creater.user_name()} --> {command}")

#     ai_name_calling_lst = commands_creater.AI_name_calling_lst() # AI Names list

#     # Sample Command -> Hey Friday, on port three

#     if recognized_text:
        
#         # If text Got recognized and is not None
#         # then it will be passed to the hosted Server that
#         # controls the HOME Controller Board and CHAT BOT Bindings

#         # If not connected to the Internet then the offline chatbot features will be used

DIRECT_COMMAND = None

class USER__CONTROLS:
    # DIRECT_COMMAND = None
    PHRASE_TIME_LIMIT = 4

    RECOGNIZE_COMMAND_ = ''

    def __init__(self):
        '''
        Initialize USER CONTROLS
        '''
        # Thread.__init__(self)
        self.r = sr.Recognizer()
        # self.GET_RESPONSE()
    def start(self):
        '''
        START TRIGGER
        '''
    def SPEECH_2_TEXT(self, TIMEOUT=PHRASE_TIME_LIMIT):
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
        # if (SERVER_COMMUNICATION.CONNECTION_TESTING(SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[0][1])):
        with sr.Microphone() as source:
        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source, phrase_time_limit=TIMEOUT)
            #print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            
            try:
                # using google speech recognition | with DEMO KEY inbuilt
                command = self.r.recognize_google(audio)
                return (command)
            except:
                return None

    def RECOGNIZE_COMMAND(self, TIMEOUT=PHRASE_TIME_LIMIT):
        
        global DIRECT_COMMAND

        if (DIRECT_COMMAND==None):

            if (SERVER_COMMUNICATION.VOICE_RECOGNITION_CONNECTION_TESTING(SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[0][1])):
                return self.SPEECH_2_TEXT(TIMEOUT)

            # IF DOMAIN is not rechable then it will sleep for PHRASE_TIME_LIMIT SECONDS and return None
            time.sleep(TIMEOUT)
            return None

        CMD = DIRECT_COMMAND
        DIRECT_COMMAND = None
        return CMD

    def COMMUNICATE_AI(self, DATA):
        if (SERVER_COMMUNICATION.VOICE_RECOGNITION_CONNECTION_TESTING(SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[1][1])):
            return SERVER_COMMUNICATION.AI_COMMUNICATE(DATA)

        # IF DOMAIN is not rechable then it will sleep for PHRASE_TIME_LIMIT SECONDS and return None
        time.sleep(2)
        return None

    def TRIGGER_AI(self, TIMEOUT=3):
        # AI communication only work if
        # the communication start with 
        # OK <AI_NAME> | HELLO <AI_NAME> | ...
        try:
            VOICE_RECOGNITION_TEXT = self.RECOGNIZE_COMMAND(TIMEOUT)

            if (VOICE_RECOGNITION_TEXT):
                # print(VOICE_RECOGNITION_TEXT)
                for WORD in AI.TRIGGER_WORDS:
                    if (VOICE_RECOGNITION_TEXT.upper().startswith(WORD+" "+AI.NAME)):
                        # print(WORD)
                        self.GET_RESPONSE()
        except KeyboardInterrupt:
            self.GET_RESPONSE()

    def SYSTEM_COMMAND_EXECUTION(self, DATA):
        if DATA.upper()=="LEAVE ME PLEASE":
            self.exit()

        # elif DATA.upper()=="TURN ON BEDROOM LIGHT":
        #     return {"RESPONSE":"BEDROOM LIGHT TURNED ON"}

        # elif DATA.upper()=="TURN OFF BEDROOM LIGHT":
        #     return {"RESPONSE":"BEDROOM LIGHT TURNED OFF"}

        # elif DATA.upper()=="GET HUMIDITY STATUS":
        #     return {"RESPONSE":"DATA FETCHED SUCCESSFULLLY", "CONTROLLER_RESPONSE":"HUMIDITY: 37% [28°C]"}

        for speech in AI.SYSTEM_COMMANDS:
            if DATA.upper()==speech.upper():
                subprocess.Popen(AI.SYSTEM_COMMANDS[speech])
                return {"RESPONSE":"COMMAND EXECUTED SUCCESSFULLY"}
        return 0


    def GET_RESPONSE(self, TIMEOUT=PHRASE_TIME_LIMIT):
        try:
            # Play Click Sound For AI Trigger Response
            self.PLAY_SOUND(AI.AI_TRIGGER_SOUND_FILEPATH)
            VOICE_RECOGNITION_TEXT = self.RECOGNIZE_COMMAND(TIMEOUT)

            if (VOICE_RECOGNITION_TEXT):
                print(CLIENT_DATA.FULL_NAME, ">>>", VOICE_RECOGNITION_TEXT)
                AI_RESPONSE_DATA=self.SYSTEM_COMMAND_EXECUTION(VOICE_RECOGNITION_TEXT)
                if(AI_RESPONSE_DATA==0):
                    AI_RESPONSE_DATA = self.COMMUNICATE_AI(VOICE_RECOGNITION_TEXT)

                if(AI_RESPONSE_DATA):
                    print(AI.NAME, "::", AI_RESPONSE_DATA['RESPONSE']) # Response Format -> AI :: I am good
                    self.SPEAK(AI_RESPONSE_DATA["RESPONSE"])
                    try:

                        if(AI_RESPONSE_DATA["CONTROLLER_RESPONSE"]):
                            # print(AI_RESPONSE_DATA["CONTROLLER_RESPONSE"])
                            for i in range(5):
                                time.sleep(1)
                                HOME_CONTROLLER_RESPONSE = CRYPTOGRAPHY.str2json(SERVER_COMMUNICATION.HTTP_CONNECTION_HANDLER(SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[1][0], "GET", SERVER_COMMUNICATION.SERVER_COMMUNICATION_ENDPOINTS[1][1], "/fetch_home_controller_response")['data'])
                                if (HOME_CONTROLLER_RESPONSE["STATUS"]!=0):
                                    print(HOME_CONTROLLER_RESPONSE["RESPONSE"])
                                    break

                        # ##### IF INFORMATION IS NOT AVAILABLE
                        # ##### WITHIN 5 or MENTIONED SECONDS
                        # ##### THEN THE BELOW LINE WILL BE PRINTED
                        # if(HOME_CONTROLLER_RESPONSE["STATUS"]==0):
                        #     print("HOME CONTROLLER UNAVAILABLE OR HAS NOT BEEN CONFIGURED PROPERLY")

                    except:
                        pass

        except KeyboardInterrupt:
            self.exit()

    def PLAY_SOUND(self, FILEPATH):
        '''
            PlAY SOUND FILES
        '''
        playsound(FILEPATH, False)

    def SPEAK(self, SPEECH):
        '''
        Pass String to generate Audio from Speaker
        for AI response
        '''
        pyttsx3.speak(SPEECH)

    def exit(self):
        print(AI.NAME, ":: FAREWELL :)")
        self.SPEAK("farewell")
        sys.exit()

USER_CONTROLS = USER__CONTROLS()

class STARTUP:

    CORE_CONFIG_FILE_PATH = ".config"

    # DEVICE_CONFIG_FILE_PATH = "DEVICE.config"
    # AI_CONFIG_FILE_PATH = "AI.config"
    # SYSTEM_COMMANDS_FILE_PATH = "SYSTEM_COMMANDS.json"

    def __init__(self):
        '''
            Initialize startup data
        '''
        
        CORE_CONFIG_FILE_DATA = self.TOML_READ_DEVICE_CONFIG(self.CORE_CONFIG_FILE_PATH)
        DEVICE_CONFIG_DATA = self.TOML_READ_DEVICE_CONFIG(CORE_CONFIG_FILE_DATA["CONFIG_FILE_PATHS"]["DEVICE_CONFIG_FILE_PATH"])
        AI_CONFIG_DATA = self.TOML_READ_DEVICE_CONFIG(CORE_CONFIG_FILE_DATA["CONFIG_FILE_PATHS"]["AI_CONFIG_FILE_PATH"])
        SYSTEM_COMMANDS_DATA = self.JSON_READ_DEVICE_CONFIG(CORE_CONFIG_FILE_DATA["CONFIG_FILE_PATHS"]["SYSTEM_COMMANDS_FILE_PATH"])

        # LOAD DEVICE IDENTIFIER DATA #
        # print("LOADING")
        try:
            CLIENT_DATA.DEVICE_ID = DEVICE_CONFIG_DATA["DEVICE_IDENTIFIER"]["DEVICE_ID"]

            with open(DEVICE_CONFIG_DATA["DEVICE_IDENTIFIER"]["PRIVATE_KEY_PATH"], 'r') as f:
                CLIENT_DATA.DEVICE_PRIVATE_KEY = f.read()


            with open(DEVICE_CONFIG_DATA["DEVICE_IDENTIFIER"]["PUBLIC_KEY_PATH"], 'r') as f:
                CLIENT_DATA.DEVICE_PUBLIC_KEY = f.read()

            print("DEVICE IDENTIFIER DATA LOADED SUCCESSFULLY")

        except:
            print("!!! ERROR OCCURED DURING STARTUP : [DEVICE IDENTIFIER DATA LOADING FAILED] !!!")

        # LOAD CLIENT IDENTIFIER DATA #

        try:
            # LOAD CLIENT DATA
            CLIENT_DATA.UUID = DEVICE_CONFIG_DATA["USER_IDENTIFIER"]["UUID"]
            CLIENT_DATA.EMAIL = DEVICE_CONFIG_DATA["USER_IDENTIFIER"]["EMAIL"]
            CLIENT_DATA.FULL_NAME = DEVICE_CONFIG_DATA["USER_IDENTIFIER"]["FULL_NAME"]
            CLIENT_DATA.USERNAME = DEVICE_CONFIG_DATA["USER_IDENTIFIER"]["USERNAME"]
            CLIENT_DATA.PASSWORD = DEVICE_CONFIG_DATA["USER_IDENTIFIER"]["PASSWORD"]


            print("USER : ", CLIENT_DATA.FULL_NAME, "[", CLIENT_DATA.USERNAME, "]")

            print("CLIENT IDENTIFIER DATA LOADED SUCCESSFULLY")
        except:
            print("!!! ERROR OCCURED DURING STARTUP : [CLIENT IDENTIFIER DATA LOADING FAILED] !!!")


        # LOAD SERVER COMMUNICATION INFO #

        try:
            SERVER_COMMUNICATION.VOICE_RECOGNITION_ENDPOINT = DEVICE_CONFIG_DATA["COMMUNICATION_SERVER_INFO"]["VOICE_RECOGNITION_ENDPOINT"]
            SERVER_COMMUNICATION.AI_COMMUNICATION_ENDPOINT = DEVICE_CONFIG_DATA["COMMUNICATION_SERVER_INFO"]["AI_COMMUNICATION_ENDPOINT"]
            # SERVER_COMMUNICATION.AI_COMMUNICATION_ENDPOINTS = re.findall(r'(http|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', DEVICE_CONFIG_DATA["COMMUNICATION_SERVER_INFO"]["VOICE_RECOGNITION_ENDPOINT"]+" "+DEVICE_CONFIG_DATA["COMMUNICATION_SERVER_INFO"]["AI_COMMUNICATION_ENDPOINT"])
            print("SERVER COMMUNICATION DATA LOADED SUCCESSFULLY")

        except:
            print("!!! ERROR OCCURED DURING STARTUP : [SERVER COMMUNICATION DATA LOADING FAILED] !!!")


        # LOAD AI COMMUNICATION INFO #

        try:
            
            AI.NAME = AI_CONFIG_DATA["AI_CORE"]["NAME"]
            AI.GENDER = AI_CONFIG_DATA["AI_CORE"]["GENDER"]
            AI.TRIGGER_WORDS = AI_CONFIG_DATA["AI_CORE"]["TRIGGER_WORDS"]
            AI.SYSTEM_COMMANDS = SYSTEM_COMMANDS_DATA
            AI.AI_TRIGGER_SOUND_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["AI_TRIGGER_SOUND_FILEPATH"]

            print("AI NAME :", AI.NAME)
            print("AI MANUAL TRIGGER : CTRL+C")
            print("AI VOICE TRIGGER : ")
            for AI_TRIGGER_WORD in AI.TRIGGER_WORDS:print("\t", AI_TRIGGER_WORD, AI.NAME)
            # AI.BRAIN_LOAD_COMMAND = AI_CONFIG_DATA["AI_CORE"]["BRAIN_LOAD_COMMAND"]
            # AI.BRAIN_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_FILEPATH"]
            # AI.BRAIN_BUILD_XML_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_BUILD_XML_FILEPATH"]


            print("AI CORE LOADED SUCCESSFULLY")

        except:
            print("!!! ERROR OCCURED DURING STARTUP : [AI CORE LOADING FAILED] !!!")

        # INITIALIZE DATA HANDLER SUPPORTS #
        CLIENT_DATA.start()
        SERVER_COMMUNICATION.start()
        AI.start()

        SPEECH_RECOGNIZER.start()
        # USER_CONTROLS()


        

    def TOML_READ_DEVICE_CONFIG(self, FILE_PATH):
        '''
        READ DEVICE CONFIG FILE
        FOR INITIAL VALUE ASSIGNMENT
        
        CONSIDERING: FILE STRUCTURE TYPE : TOML
        '''

        with open(FILE_PATH, 'r') as f:
            DATA = toml.loads(f.read())

        return DATA

    def JSON_READ_DEVICE_CONFIG(self, FILE_PATH):
        '''
        READ DEVICE CONFIG FILE
        FOR INITIAL VALUE ASSIGNMENT
        
        CONSIDERING: FILE STRUCTURE TYPE : JSON
        '''

        with open(FILE_PATH,'r') as f:
            DATA=json.loads(f.read())

        return DATA


def main():
    # Initialize Startup 
    print("-"*30)
    STARTUP()
    print("-"*30)
    # USER_CONTROLS()
    # global DIRECT_COMMAND


    while True:
        
        # USER_CONTROLS()
        USER_CONTROLS.TRIGGER_AI()
        # print(CLIENT_DATA.FULL_NAME+" >>> ")
        # manual_input_value = input()
        
        # if (manual_input_value=="EXIT"):
        #     break
        # # USER_CONTROLS.DIRECT_COMMAND = manual_input_value

        # DIRECT_COMMAND = manual_input_value
        # user_controls_thread = USER_CONTROLS_THREAD()

        # user_controls_thread = USER_CONTROLS_THREAD()

        # # Start user_controls thread
        # user_controls_thread.start()
        # print(CLIENT_DATA.FULL_NAME+" >>> ")
        # user_controls_thread.exit()

            # After every thing finished the Threads will end



        # user_controls_thread.exit()



    

if __name__=="__main__":
    main()