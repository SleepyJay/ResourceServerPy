#!/usr/bin/python


# Whiteboard Thunks:
    # handle in : handler
    # read config:
        # lexer : lexer.config
        # parser (common?)
        # storage? Config.py?
    # scan paths : scanner
    # read rsc : lexer
    # read files : lexer
    # build and store res tree : parser
    # satisfy dependencies : engine?
    # build output : emitter
    # handle out : handler

from Config import Config
from Parser.ConfigParser import ConfigParser
from Lexer.ConfigLexer import ConfigLexer
import os
import re

RES_TYPES = {
    'jsr': 'js',
    'cssr': 'css',
}

class ResourceServer(object):

    # pass just res_path, or all three
    def __init__(self, res_path, res_name=None, res_type=None):
        if not res_name:
            res_path, res_name, res_type = self.splitResPath(res_path)

        self.res_path = res_path
        self.res_name = res_name
        self.res_type = res_type

    #
    def splitResPath(self, res_path):
        path, file = os.path.split(res_path)
        filename, file_extension = os.path.splitext(file)
        file_extension = re.compile('^\.').sub('',file_extension)
        res_type = file_extension
        if file_extension in RES_TYPES:
            res_type = RES_TYPES[file_extension]
        return path, filename, file_extension


    #
    def start(self, options=None):
        print("\nResourceServer: starting\n")

        self.configure(options)

        self.scan()





    #
    def configure(self, options):
        print "res_path: '{}'".format(self.res_path)

        config_path = self.getConfigPath()
        lexed = ConfigLexer().lex(config_path, options)

        config_parser = ConfigParser(self.res_path, self.res_name, self.res_type)
        self.config = config_parser.parse(lexed)


    #
    def getConfigPath(self):
        if os.path.isfile(self.res_path + "/local.rsc"):
            return self.res_path + "/local.rsc"

        elif os.path.isfile(self.res_path + "/config.rsc"):
            return self.res_path + "/config.rsc"
    
    
    #
    def scan(self):
        pass
        
        
        
        
        
        
        
        
        

    
    



