#!/usr/bin/python

import os.path
from Lexer.ConfigLexer import ConfigLexer
from Parser.ConfigParser import ConfigParser

class Config(object):
    
    def __init__(self, config_dir = None):
        self.lexer = ConfigLexer(config_dir)
        self.config = []

    #
    def start(self, config_dir = None):
        if config_dir == None: return

        if os.path.isfile(config_dir + "config.rsc"):
            lexed = self.lexer.lexFile(config_dir + "config.rsc")
            #self.config.extend(lexed)

        # local overrides config
        if os.path.isfile(config_dir + "local.rsc"):
            lexed = self.lexer.lexFile(config_dir + "local.rsc")
            #self.config.extend(lexed)
    
    



