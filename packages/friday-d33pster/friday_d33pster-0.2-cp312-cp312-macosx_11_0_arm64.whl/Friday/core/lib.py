
import requests, sys, zipfile, webbrowser, stat, threading
from os.path import expanduser, join, basename, exists
from os import makedirs, unlink, chmod, system as run
from tqdm import tqdm
from colorama import Fore
from wrapper_bar.wrapper import Wrapper
from datetime import datetime

from ..rust import gtts
from Friday.utils.terminal import Updater


SERVER_ENV_CREATION = """
#!/usr/bin/env bash

env=\"{}\"

# get conda base
conda_base=$(conda info --base)
# create source obj
source_obj="$conda_base/etc/profile.d/conda.sh"
# activate conda command
source $source_obj

env_list=$(conda env list)
# echo $env_list

# if present, exit 0
if echo "$env_list" | grep -q "^$env "; then
    exit 0
else
    # create the env
    conda create -n "$env" python=3.9 -y
    # activate it
    conda activate "$env"
    # install rasa
    pip install rasa
    exit 0
fi
"""

SERVER_START = """
#!/usr/bin/env bash

ENV_NAME=\"{}\"

# get conda base
conda_base=$(conda info --base)
# create source obj
source_obj="$conda_base/etc/profile.d/conda.sh"
# activate conda command
source $source_obj

conda activate "$ENV_NAME"

export SQLALCHEMY_SILENCE_UBER_WARNING=1
cd ~/.friday/bot
rasa run
"""

class Core:
    def __init__(self):
        pass
    
    class NLP_server:
        def __init__(self, config_dir:str, default_name: str = "nlp_server_"):
            self.config = config_dir
            self.server_start_commands = SERVER_START.format(default_name)
            self.server_env_create_commands = SERVER_ENV_CREATION.format(default_name)
        
        @property
        def create_env(self):
            with open(join(self.config, 'create_server.sh'), 'w+') as server:
                server.write(self.server_env_create_commands)
            
            # give it perms
            chmod(join(self.config, 'create_server.sh'),
                stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |  # rwx user
                stat.S_IRGRP | stat.S_IXGRP |                 # rx group
                stat.S_IROTH | stat.S_IXOTH)                  # rx other
            
            # define thread function
            def create_server_thread(path: str):
                run(path)
            
            # call it
            thread = threading.Thread(target=create_server_thread, args=(join(self.config, 'create_server.sh'),))
            thread.start()
            thread.join()
        
        @property
        def start(self):
            with open(join(self.config, 'start_server.sh'), 'w+') as server:
                server.write(self.server_start_commands)
            
            # give it perms
            chmod(join(self.config, 'start_server.sh'),
                stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |  # rwx user
                stat.S_IRGRP | stat.S_IXGRP |                 # rx group
                stat.S_IROTH | stat.S_IXOTH)                  # rx other
            
            run(join(self.config, 'start_server.sh'))

    class Soul:
        def __init__(self):
            self.__name = "Friday"
            self.__version = "0.2"
            self.__version_in_words = "O point 2"
        
        @property
        def name(self) -> str:
            return self.__name
        
        @property
        def version(self) -> str:
            return self.__version
        
        @property
        def version_in_words(self) -> str:
            return self.__version_in_words

    class FileSystem:
        CONFIG = join(expanduser('~'), '.friday')
        def __init__(self, speech: 'Core.Memory.Speech'):
            # speech
            self.speech = speech
            # User Home directory
            self.user_home = expanduser('~')
            # Configurations folder
            self.config_folder = self.CONFIG
            # make the config folder, if already present, leave it be
            makedirs(self.config_folder, exist_ok=True)
            # downloads folder
            self.downloads_folder = join(self.config_folder, 'downloads')
            # make the downloads folder, if already present, leave it be
            makedirs(self.downloads_folder, exist_ok=True)
        
        @property
        def getConfigurations(self):
            return self.Configurations()

        @property
        def check_and_update_files(self):
            # Begin - model/

            # if config_dir/model/ not present
            if not exists(join(self.config_folder, 'model')):
                # find asset_url for 'model.zip'
                asset_url_model = None # initialize to None
                # find if there is some asset named model.zip
                for asset in self.getConfigurations.response['assets']:
                    if asset['name'] == 'model.zip':
                        # if found, get the download url
                        asset_url_model = asset['browser_download_url']
                        # and break
                        break
                # ultimately if not found, exit
                if not asset_url_model:
                    # print(f"{Fore.RED}Failed to download stt model!{Fore.RESET} Check latest release for download link and instructions.")
                    self.speech.speak_as_thread("Failed to download STT model!", wait=True)
                    self.speech.speak_as_thread("Check latest release for download link and instructions!", wait=True)
                    sys.exit(1)
                # download and get the filename
                self.speech.speak_as_thread("Downloading STT model vosk")
                filename = self.Downloader(asset_url_model, self.downloads_folder).simulate
                # print status
                # print(f" {Fore.BLUE}downloaded{Fore.RESET}: {filename} to {join(self.downloads_folder, filename)}.")
                self.speech.speak_as_thread("Downloaded")
                # check if the zip file is intact
                if not zipfile.is_zipfile(join(self.downloads_folder, 'model.zip')):
                    # if not a zip file then, print error and exit
                    # print(f"{Fore.RED}Failed{Fore.RESET} to extract \'model.zip\'. Unable to identify zip data.")
                    self.speech.speak_as_thread("Failed to extract model dot zip", wait=True)
                    self.speech.speak_as_thread("unable to identify zip data", wait=True)
                    sys.exit(1)
                # initialise a wrapper bar object
                wrap = Wrapper()
                # define codes
                pythoncodes = [
                    f"""with zipfile.ZipFile(join(\'{self.downloads_folder}\', \'model.zip\'), \'r\') as zip_ref:
    zip_ref.extractall(\'{self.config_folder}\')"""
                ]
                # define dependencies
                dependencies = [
                    """import zipfile""",
                    """from os.path import join"""
                ]
                # simulate progress bar
                self.speech.speak_as_thread("Extracting model dot zip")
                wrap.pyShellWrapper(pythoncodes, dependencies, "Extracting", 0.05, 70, 'ElapsedTime')
                # delete the download
                unlink(join(self.downloads_folder, 'model.zip'))
                # print status
                # print(f" extracted: \'model.zip\' to  {join(self.downloads_folder, 'model')}")          
                self.speech.speak_as_thread("Extracted")  
            else:
                self.speech.speak_as_thread("vosk model ready!")
                
            # Begin - bot/

            # if config_dir/bot/ not present
            if not exists(join(self.config_folder, 'bot')):
                # find asset url for 'bot.zip'
                asset_url_bot = None # initialise to None
                # find if asset['name'] == 'bot.zip' is present or not
                for asset in self.getConfigurations.response['assets']:
                    if asset['name'] == 'bot.zip':
                        # if found, get the download url
                        asset_url_bot = asset['browser_download_url']
                        # and break out of the loop
                        break
                
                # ultimately if not found, exit
                if not asset_url_bot:
                    self.speech.speak_as_thread("Failed to download NLP bot needed for command comprehension!", wait=True)
                    self.speech.speak_as_thread("Check latest release for download link and instructions!", wait=True)
                    # self.speech.speak_till_end
                    # print(f"{Fore.RED}Failed to download audios needed for smooth functioning!{Fore.RESET} Check latest release for download link and instructions.")
                    sys.exit(1)
                # download and get the filename
                self.speech.speak_as_thread("Downloading NLP bot")
                # self.speech.speak
                filename = self.Downloader(asset_url_bot, self.downloads_folder).simulate
                # print status
                self.speech.speak_as_thread("Downloaded")
                # check if the zip file is intact
                if not zipfile.is_zipfile(join(self.downloads_folder, 'bot.zip')):
                    # if not a zip file then, print error and exit
                    self.speech.speak_as_thread("Failed to extract bot dot zip.", wait=True)
                    self.speech.speak_as_thread("Unable to identify zip data.")
                    sys.exit(1)
                # initialise a wrapper bar object
                wrap = Wrapper()
                # define codes
                pythoncodes = [
                    f"""with zipfile.ZipFile(join(\'{self.downloads_folder}\', \'bot.zip\'), \'r\') as zip_ref:
    zip_ref.extractall(\'{self.config_folder}\')"""
                ]
                # define dependencies
                dependencies = [
                    """import zipfile""",
                    """from os.path import join"""
                ]
                # simulate progress bar
                self.speech.speak_as_thread("Extracting bot dot zip")
                wrap.pyShellWrapper(pythoncodes, dependencies, "Extracting", 0.01, 70, 'ElapsedTime')
                self.speech.speak_as_thread("Extracted")
                # delete the download
                unlink(join(self.downloads_folder, 'bot.zip'))
            else:
                self.speech.speak_as_thread("Natural Language Processing systems... in place!")
        
        class Configurations:
            def __init__(self):
                # github api url for Friday.
                self.__github_api_url = "https://api.github.com/repos/d33pster/Friday/releases/latest"
                # response of api_url
                self.__response_api_url = requests.get(self.__github_api_url)
                # raise errors if any for response
                self.__response_api_url.raise_for_status()
                # convert the response to json
                self.__response_api_url_json = self.__response_api_url.json()
            
            # property for returning api_url
            @property
            def github_api_url(self):
                # return api_url
                return self.__github_api_url
            
            # property for returning response in json
            @property
            def response(self):
                return self.__response_api_url_json
    
        class Downloader:
            def __init__(self, url: str, download_dir: str):
                # set class variables
                self.download_url = url
                self.downloads_folder = download_dir
                # make downloads folder, if present, no problem
                makedirs(self.downloads_folder, exist_ok=True)
                # get filename
                self.filename = join(self.downloads_folder, basename(self.download_url))
            
            @property
            def simulate(self):
                # get response on the download_url
                response = requests.get(self.download_url, stream=True)
                # get total size of the file
                total_size = int(response.headers.get('content-length', 0))
                # define block size
                block_size = 1024 # 1kb

                # make a progress bar and wrap download around it
                with open(self.filename, 'wb') as file_ref, tqdm (
                    desc=basename(self.filename), # title of bar
                    total=total_size, # total size of the file
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                    bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', # Remove the right most time and speed
                    ncols=70, # width
                ) as bar:
                    # for data in chunks of size = block_size
                    for data in response.iter_content(block_size):
                        # write data
                        file_ref.write(data)
                        # update progress bar
                        bar.update(len(data))
                
                # return basename of the file
                return basename(self.filename)
    
    class Memory:
        def __init__(self, soul: 'Core.Soul', configuration_Dir: str):
            self.config_dir = configuration_Dir
            self.speech = self.Speech(self.config_dir)
            self.comprehension = self.Comprehension(speech=self.speech, soul=soul)
        
        @property
        def getSpeechMemory(self):
            return self.speech

        @property
        def getComprehensionMemory(self):
            return self.comprehension
        
        class Speech:
            def __init__(self, configuration_dir: str):
                # create reply obj
                self.reply = self.Simulate()
                # config dir
                self.config_dir = configuration_dir
                # define a file for backlogs
                # say, config_dir/__memory__/speech_backlogs.txt
                self.memory_path = join(self.config_dir, '__memory__')
                # backlogs path
                self.speech_backlog_path = join(self.memory_path, 'speech_backlogs.txt')
                # define a class variable for speech memory
                self.to_be_said: list[str] = []
                # define a pointer for this class variable
                self.index = 0
                # check if backlogs file exist
                if exists(self.speech_backlog_path):
                    # read the backlogs
                    self.read_backlogs
                    # add a little bit of extra info before backlogs
                    self.extend_from_front([
                        "Sir, I .. had a few things to say since last time..",
                    ])
                    # speak them
                    self.speak_till_end
                else:
                    # if backlogs file dont exist, check and make the memory_path
                    makedirs(self.memory_path, exist_ok=True)
            
            # create an add function
            def add(self, line: str):
                self.to_be_said.append(line)
            
            # create an extend function
            def extend(self, extender: list[str]):
                self.to_be_said.extend(extender)
            
            # create an extendee function
            def extend_from_front(self, extendee: list[str]):
                extendee.extend(self.to_be_said)
                self.to_be_said = extendee
            
            # create a property to return current index
            @property
            def pointer(self) -> int:
                return self.index
            
            # create a property to return maximum current capacity
            @property
            def capacity(self) -> int:
                return len(self.to_be_said)
            
            # create a property that returns true if there are unspoken words
            @property
            def want_to_speak(self) -> bool:
                return self.pointer < self.capacity
            
            # create a property to return next line to be said
            @property
            def next(self) -> str | None:
                """what to say next?"""
                try:
                    to_say = self.to_be_said[self.pointer]
                    self.index += 1
                    return to_say
                except IndexError:
                    return None
            
            # create a property that saves pending conversations for next boot
            @property
            def next_time_then(self):
                """"save all the stuff u need to say for next time"""
                for i in range(len(self.to_be_said)):
                    self.to_be_said[i] += '\n'
                
                with open(self.speech_backlog_path, 'w+') as backlog_ref:
                    backlog_ref.writelines(self.to_be_said[self.pointer:])
            
            # create a property to read all the backlogs and delete the physical file
            @property
            def read_backlogs(self):
                # read the contents:
                with open(self.speech_backlog_path, 'r+') as backlog_ref:
                    self.to_be_said = backlog_ref.readlines() # there have "\n" in them
                
                # replace the "\n" of these lines
                for i in range(len(self.to_be_said)):
                    self.to_be_said[i] = self.to_be_said[i].replace('\n', '')
                
                # delete the backlog file
                unlink(self.speech_backlog_path)
            
            # create a property to speak
            @property
            def speak(self):
                line = self.next
                if line != None:
                    self.reply.tts.speak(line)
                else:
                    pass
            
            # create a property to say_till_end:
            @property
            def speak_till_end(self):
                while self.pointer < self.capacity:
                    line = self.next
                    if line != None:
                        self.reply.tts.speak(line)
                    else:
                        pass
            
            def greet(self, designation: str = "Sir", custom_greeting: str| None = None):
                if custom_greeting != None:
                    self.speak(custom_greeting)
                else:
                    self.speak(self.greet_text + " " + designation)
                
            
            @property
            def greet_text(self) -> str:
                hour = int(datetime.now().hour)

                if hour >= 0 and hour < 12:
                    return "Good Morning!"
                elif hour >= 12 and hour < 18:
                    return "Good Afternoon!"
                else:
                    return "Good Evening!"

            def speak_as_thread(self, text: str, wait: bool = False):
                # create a thread function
                non_local_simulate = self.reply
                def thread_to_speak(t: str):
                    nonlocal non_local_simulate
                    non_local_simulate.tts.speak(t)
                
                thread = threading.Thread(target=thread_to_speak, args=(text,))
                thread.start()
                if wait:
                    thread.join()
            
            # create a Simulate class under Speech
            class Simulate:
                def __init__(self):
                    # create a tts object from the Friday2.rust.gtts lib
                    self.text_to_speech = gtts.TextToSpeech(volume=3)
                
                # create a property to easily fetch text_to_speech obj
                @property
                def tts(self):
                    return self.text_to_speech
        
        class Comprehension:
            def __init__(self, speech: 'Core.Memory.Speech', soul: 'Core.Soul', designation: str = "Sir", ):
                # get speech
                self.speech = speech
                # get soul
                self.soul = soul
                # designation
                self._designation = designation
                # terminal updater
                self.updater = Updater()
                # NLU server link
                self.nlu_url = "http://localhost:5005/webhooks/rest/webhook"
                # commands list
                self.command_list: list[str] = [
                    "Friday",
                    "Open",
                ]
            
            def resolve_with_nlp(self, command: str, sender="Friday") -> str | None:
                # create payload
                payload = {
                    "sender":sender,
                    "message":command,
                }

                # send the request to the rasa server
                response = requests.post(self.nlu_url, json=payload)

                # check if the response status is OK(200)
                if response.status_code == 200:
                    return response.json()[0]['text']
                    # print(response.json(), type(response.json()))
                    # sys.exit(0)
                else:
                    return None
            
            @property
            def clist(self) -> list[str]:
                return self.command_list
            
            @property
            def designation(self) -> str:
                return self._designation
            
            @designation.setter
            def designation(self, dsg: str):
                self._designation = dsg
            
            def pathway(self, clist_index: int, comprehended_command: str):
                # get command to follow
                command = self.clist[clist_index]
                # remove the command from the comprehended_command:
                remaining_command = comprehended_command.lower().replace(command.lower(), '').strip()

                # Greet command
                if command == "Friday":
                    self.speech.speak_as_thread(self.speech.greet_text + " " + self.designation, wait=True)
                    self.speech.speak_as_thread(self.soul.name + "... " + self.soul.version_in_words + ", At your service!")
                elif command == "Open":
                    # identify what is the sub_command
                    if remaining_command == "github":
                        # update status
                        self.updater.refresh
                        self.updater.message = f"{Fore.BLUE}Running{Fore.RESET} default web-browser"
                        self.updater.update()

                        self.speech.speak_as_thread("GitHub has been opened!")

                        # open
                        webbrowser.open("https://github.com")
                        self.updater.refresh
                        
                    elif remaining_command == "linkedin":
                        self.updater.refresh
                        self.updater.message = f"{Fore.BLUE}Running{Fore.RESET} default web-browser"
                        self.updater.update()

                        self.speech.speak_as_thread("Linkedin has been opened!")

                        webbrowser.open("https://linkedin.com/in/")
                        self.updater.refresh
                else:
                    pass