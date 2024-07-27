from Friday.core.lib import Core
from Friday.core.stt_lib import SpeechToText, WakeUp

from argpi import ArgumentDescription, Arguments

import sys, os, time

class Friday:
    def __init__(self):
        self.core = Core()

        self.memory = self.core.Memory(self.core.Soul(), self.core.FileSystem.CONFIG)
        self.speech = self.memory.Speech(self.core.FileSystem.CONFIG)
        self.filesystem = self.core.FileSystem(self.speech)
        self.server = self.core.NLP_server(self.filesystem.CONFIG)

        self.wakeup = WakeUp("Friday", self.speech)
        self.stt = SpeechToText(self.filesystem.CONFIG, self.speech)
        self.comprehension = self.memory.Comprehension(self.speech, self.core.Soul())

        os.chdir(self.filesystem.CONFIG)

    @property
    def check_or_get_designation(self) -> str:
        # get designation_path = CONFIG/designation.txt
        designation_path = os.path.join(self.filesystem.CONFIG, 'designation.txt')
        # if path doesnt exist
        if not os.path.exists(designation_path):
            # hear designation
            designation = self.stt.ask_designation(listening_label="Friday is listening..")
            designation = self.stt.process_model_ouptut(designation)
            designation = self.comprehension.resolve_with_nlp(designation)

            if designation == None:
                self.speech.speak_as_thread("NLP server is not online!", wait=True)
                sys.exit(1)

            with open(designation_path, "w+") as desig_ref:
                desig_ref.write(designation)
        else:
            with open(designation_path, "r+") as desig_ref:
                designation = desig_ref.read().replace('\n', '')
        
        return designation

    @property
    def boot_server(self):
        # check and update file system
        self.speech.speak_as_thread("Checking file systems")
        self.filesystem.check_and_update_files

        # check and create server
        self.speech.speak_as_thread("Checking server environment")
        self.server.create_env
        # start server
        self.speech.speak_as_thread("Starting server")
        self.server.start
    
    @property
    def standby(self):
        self.speech.speak_as_thread("Booting up.")
        time.sleep(2)
        self.speech.speak_as_thread("All systems Online!")
        # do perpetually
        while True:
            inter = self.wakeup.standby(resting_label="Friday is online.")
            
            if inter.get:
                # if standby is bypassed, listen
                command = self.stt.listen(phrase_time_limit=5, listening_label="I am listening...").lower()


                # print(command)

                # if couldn't hear, continue standby
                if command == "":
                    continue
                # else
                else:
                    # first, process it to get the clear text
                    # the output from model is wierd
                    command = self.stt.process_model_ouptut(command)
                    # second, confer with the nlu server
                    command = self.comprehension.resolve_with_nlp(command=command)

                    # if server error
                    if command == None:
                        to_speak = [
                            "NLP server is not running or has been closed."
                            "Cannot process command."
                            "please run NLP server."
                        ]
                        self.speech.extend(to_speak)
                        self.speech.speak_till_end
                        continue
                    
                    # check commands
                    index = None
                    for com in self.comprehension.clist:
                        if com.lower() in command:
                            index = self.comprehension.clist.index(com)
                            break
                    
                    # if it matches no command:
                    if index == None:
                        continue
                    else:
                        self.comprehension.pathway(clist_index=index, comprehended_command=command)
        
class FridayArguments:
    def __init__(self):
        # capture arguments given
        self.arguments = Arguments().__capture__()

        # set arguments to check
        ## server
        self.arguments.__add__(
            "server",
            ArgumentDescription()
                .name("server")
                .description("start NLP server")
                .shorthand("-s")
        )

        # analyse
        self.arguments.__analyse__()
    
    @property
    def get(self):
        return self.arguments

def main():
    friday = Friday()
    arguments = FridayArguments().get

    if arguments.__there__("server"):
        friday.boot_server
        sys.exit(0)
    
    # if first time setup, or whatever
    desgination = friday.check_or_get_designation

    # change designation in comprehension
    friday.comprehension.designation = desgination

    # run standby
    friday.standby