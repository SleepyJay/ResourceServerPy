#!/usr/bin/python

import os
import re

from Parser.ConfigParser import ConfigParser
from Lexer.ConfigLexer import ConfigLexer
from Lexer.JSLexer import JSLexer
from Scanner import Scanner
from Engine import Engine
from Emitter.JSEmitter import JSEmitter


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

        self.config = None
        self.scanner = None
        self.depEngine = None



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
        self.configure(options)

        self.scan()

        dependencies = self.getDependencies()

        output = self.createOutput(self.scanner.resources, dependencies)

        return output


    #
    def configure(self, options):
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
        self.scanner = Scanner(self.config)
        res_lexer = self.getResourceLexer()
        self.scanner.scan(res_lexer)

    #
    def getDependencies(self):
        self.depEngine = Engine(self.config, self.scanner.resources)
        return self.depEngine.buildDepenencyList(self.config.res_name)

    #
    def createOutput(self, resources, dependencies):
        self.emitter = self.getEmitter()
        return self.emitter.buildOutput(resources, dependencies)
    
    #
    def getResourceLexer(self):
        # TODO: base this on res_type...
        return JSLexer()

    #
    def getEmitter(self):
        # TODO: base this on res_type...
        return JSEmitter(self.config)
        
        
        
        
        
        
        
        

    
    



