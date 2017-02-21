#!/usr/bin/python

import os.path


class Config(object):
    
    def __init__(self, resource):
        self.resource = resource
        self.config = []
        self.lexer = ConfigLexer

    #
    def start(self, options):
        config_dir = self.resource.res_path
        if config_dir == None: return


    
    



