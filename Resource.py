#!/usr/bin/python

import os.path

class Resource(object):
    
    def __init__(self):
        self.imports = set()
        self.requires = set()
        self.provides = set()
        self.file_path = ''
        
        # used later, in Engine
        self.unresolved = None


    
    def __repr__(self):
        return str(self.__dict__)

    #
    




