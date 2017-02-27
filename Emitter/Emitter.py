#!/usr/bin/python

import os

class Emitter(object):
    
    def __init__(self, config):
        self.config = config

        self.file_list = []
        self.output = ''

    
    #
    def buildOutput(self, resources, dependencies):
        path_set = set()
        for dep_name in dependencies:
            dep = resources[dep_name]
            path = dep.file_path
            
            if not path in path_set:
                print "output: {}".format(path)
                self.file_list.append(path)
                path_set.add(path)

                with open(path) as x: self.output += x.read()

        return self.output


