#!/usr/bin/python

import os.path

class Resource(object):
    
    def __init__(self, res_path, res_name, res_type):
        self.res_path = res_path
        self.res_name = res_name
        self.res_type = res_type

    
    def __repr__(self):
        return "Resource({}/, {}, {})".format(self.res_path, self.res_name, self.res_type)
    




