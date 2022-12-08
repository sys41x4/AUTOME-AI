#import library

from threading import TIMEOUT_MAX
import speech_recognition as sr
import json

# Initialize recognizer class (for recognizing the speech)

class audio:
    get_flac_data=''
    sample_rate=0

    def __init__(self, frame_data, sample_rate, sample_width):
        ''''''
    def get_segment(self, start_ms=None, end_ms=None):
        ''''''

    def get_raw_data(self, convert_rate=None, convert_width=None):
        ''''''

    def get_flac_data(self, convert_rate=None, convert_width=None):
        return get_flac_data

    def get_wav_data(self, convert_rate=None, convert_width=None):
        ''''''

    def get_aiff_data(self, convert_rate=None, convert_width=None):
        ''''''


r = sr.Recognizer()

def speech_2_text():
# Reading Microphone as source
# listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source, phrase_time_limit=6)
        audio.get_flac_data=audio_text.get_flac_data()
        audio.sample_rate=audio_text.sample_rate
        #print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        print(r.recognize_google(audio_text))
        try:
            # using google speech recognition
            command = r.recognize_google(audio)


#            print("Text: "+command)
            return (command)
        except:
            #print("Sorry, I did not get that")
            return ("NONE")

while True:
    print(speech_2_text())