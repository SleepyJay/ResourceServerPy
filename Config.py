#!/usr/bin/python

import os.path


class Config(object):
    
    def __init__(self):
        self.res_path = ''
        self.res_name = ''
        self.res_type = ''

        self.classpaths = []
        self.verbose = False

    #
    def __repr__(self):
        return str(self.__dict__)

    
    



