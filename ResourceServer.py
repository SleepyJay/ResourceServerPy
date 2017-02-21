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


from Lexer.ConfigLexer import ConfigLexer
from Parser import Parser
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
        
        config_lexer = ConfigLexer()

        if os.path.isfile(self.res_path + "local.rsc"):
            config_lexer.lexFile(self.res_path + "local.rsc")

        elif os.path.isfile(self.res_path + "config.rsc"):
            config_lexer.lexFile(self.res_path + "config.rsc")

        if options:
            config_lexer.lexOptions(options)

        lexed = config_lexer.getLexed()
        
        config_parser = Parser()
        self.config = config_parser.parse(lexed)
    

    
    



