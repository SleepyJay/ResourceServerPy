#!/usr/bin/python

import os
from Parser.SourceParser import SourceParser

class Scanner(object):
    
    def __init__(self, config):
        self.config = config

        self.resources = {}
        self.path_map = {}
    
    #
    def scan(self, res_lexer):
        res_parser = SourceParser(self.config)

        for classpath in self.config.classpaths:
            for (path,dirs,files) in os.walk(classpath):
                for dir in dirs:
                    if(dir.startswith('.')):
                        dirs.remove(dir)

                for filename in files:
                    if filename.startswith('.'):
                        continue

                    res_path = "{}/{}".format(path, filename)
                    lexed = res_lexer.lex(res_path)
                    
                    print( "{} /// {} => ".format(path, filename) )
                    
                    resource = res_parser.parse(lexed)
                    resource.file_path = res_path

                    for res_name in resource.provides:
                        self.resources[res_name] = resource

                    if not res_path in self.path_map:
                        self.path_map[res_path] = []

                    self.path_map[res_path].extend(resource.provides)

