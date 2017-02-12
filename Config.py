#!/usr/bin/python

import os.path
from Lexer.ConfigLexer import ConfigLexer

class Config(object):
    
    def __init__(self, config_dir = None):
        self.lexer = ConfigLexer(config_dir)

    #
    def start(self, config_dir = None):
        if config_dir == None: return

        if os.path.isfile(config_dir + "config.rsc"):
            self.lexer.lex(config_dir + "config.rsc")

        # local overrides config
        if os.path.isfile(config_dir + "local.rsc"):
            self.lexer.lex(config_dir + "local.rsc")
    
    



