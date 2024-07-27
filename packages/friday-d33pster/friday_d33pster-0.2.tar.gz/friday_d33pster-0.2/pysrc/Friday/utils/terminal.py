
from platform import system as operating_system
from os import system as run

class Updater:
    def __init__(self):
        self.__message = ""
        self.system = operating_system()
    
    @property
    def message(self) -> str:
        return self.__message
    
    @message.setter
    def message(self, msg: str):
        self.__message = msg
    
    @message.deleter
    def message(self):
        self.__message = ""
    
    def update(self, end="\r"):
        print(self.message, end=end)
    
    @property
    def refresh(self):
        self.message = " " * (len(self.message) + 1)
        self.update()
    
    @property
    def print(self):
        print(self.message)
    
    @property
    def cls(self):
        if self.system.lower() == "darwin" or self.system.lower() == "linux":
            run('clear')
        elif self.system.lower() == 'windows':
            run('cls')