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
from Resource import Resource
import os
import re

RES_TYPES = {
    'jsr': 'js',
    'cssr': 'css',
}

class ResourceServer(object):
    
    def __init__(self, res_path=None, res_name=None, res_type=None):
        if res_path:
            if not res_name:
                res_path, res_name, res_type = self.splitResPath(res_path)

        self.resource = Resource(res_path, res_name, res_type)

        self.config = Config(self.resource)

    
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
        self.config.start(options)
    
    
    
    



