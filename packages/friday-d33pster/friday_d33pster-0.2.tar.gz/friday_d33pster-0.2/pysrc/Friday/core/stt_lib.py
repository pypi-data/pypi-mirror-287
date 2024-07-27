import speech_recognition, threading, sys, requests
from os.path import join
from time import sleep as pause

from Friday.utils.terminal import Updater
from Friday.utils.types import OnlyTrue

from Friday.core.lib import Core

class SpeechToText:
    def __init__(self, configuration_dir: str, speech: 'Core.Memory.Speech'):
        self.speech = speech
        self.configuration_dir = configuration_dir
        self.__recognizer = speech_recognition.Recognizer()
        self.__mic = speech_recognition.Microphone()

        # terminal updater
        self.updater = Updater()
    
    @property
    def recognizer(self) -> speech_recognition.Recognizer:
        return self.__recognizer
    
    @property
    def mic(self) -> speech_recognition.Microphone:
        return self.__mic
    
    
    def process_model_ouptut(self, output: str) -> str:
        return output.split(":")[1].replace('\n', '').replace('}', '').replace('\"', '').strip()
    
    def listen(self, phrase_time_limit: int = 1, listening_label: str = "listening..", listening_acknowledgement: str = "I am listening..", acknowledge: bool = True) -> str:
        with self.mic as source:

            if acknowledge:
                self.speech.speak_as_thread(listening_acknowledgement)

            self.updater.refresh
            self.updater.message = " " + listening_label
            self.updater.update()

            try:
                audio = self.recognizer.listen(source, phrase_time_limit=phrase_time_limit)
            except KeyboardInterrupt:
                sys.exit(0)
            
            try:
                text = self.recognizer.recognize_vosk(audio).lower()
                return text
            except speech_recognition.UnknownValueError:
                self.speech.speak_as_thread("I did not understand that!")
                return ""
            except speech_recognition.RequestError as e:
                self.updater.message = " " + e + "at STT.listen()"
                self.updater.print
                self.speech.speak_as_thread("Speech Recognition request Error. Exiting!", wait=True)
                sys.exit(1)
    
    def ask_designation(self, phrase_time_limit: int = 3, listening_label:str = "listening..") -> str:
        self.speech.speak_as_thread("How may I address you?", wait=True)
        reply = self.listen(phrase_time_limit=phrase_time_limit, listening_label=listening_label, acknowledge=False)

        while reply == "":
            reply = self.listen(phrase_time_limit=phrase_time_limit, listening_label=listening_label, acknowledge=False)
        
        return reply
            

class WakeUp:
    def __init__(self, wake_up_word: str, speech: 'Core.Memory.Speech'):
        self.speech = speech
        self.wakeup_word = wake_up_word
        self.__mic = speech_recognition.Microphone()
        self.__recognizer = speech_recognition.Recognizer()
        self.updater = Updater()
    
    @property
    def mic(self):
        return self.__mic
    
    @property
    def recognizer(self):
        return self.__recognizer
    
    def standby(self, resting_label: str, phrase_time_limit: int = 5, cannot_understand_label: str = "Sorry! I didnt quite get that") -> OnlyTrue:
        """This function is responsible for waiting and listening for a wake up word, If wake up word is said and identified
        It returns a `OnlyTrue` class that which only returns True.

        As said earlier, this method only returns true, else runs perpetually.
        `see documentation on **OnlyTrue** class for more info.`
        """
        self.updater.message = " " + resting_label
        self.updater.update()
        while True:
            with self.mic as source:
                self.updater.refresh
                self.updater.message = " " + resting_label
                self.updater.update()

                try:
                    audio = self.recognizer.listen(source, phrase_time_limit=phrase_time_limit)
                except KeyboardInterrupt:
                    sys.exit(0)

                try:
                    text = self.recognizer.recognize_vosk(audio).lower()
                except speech_recognition.UnknownValueError:
                    self.speech.speak_as_thread(cannot_understand_label, wait=True)
                    # pause for 1 sec
                    pause(1)
                    continue
                except speech_recognition.RequestError as e:
                    self.updater.message = " " + e + " @ WAKEUP_STANDBY"
                    self.updater.print
                    self.speech.speak_as_thread("GTTS API request error. Exiting!", wait=True)
                    sys.exit(1)
                
                if self.wakeup_word.lower() in text:
                    return OnlyTrue
                else:
                    continue