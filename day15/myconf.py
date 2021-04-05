

from configparser import ConfigParser

class Myconf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename,encoding="utf-8")

