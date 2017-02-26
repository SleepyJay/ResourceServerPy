#!/usr/bin/python

import os
import pprint
from Parser.ResourceParser import ResourceParser

class Scanner(object):
    
    def __init__(self, config):
        self.config = config

        self.resources = {}
        self.path_map = {}
    
    #
    def scan(self, res_lexer):
        pp = pprint.PrettyPrinter(indent=4)

        res_parser = ResourceParser(self.config)

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
                    pp.pprint( lexed )
                    
                    resource = res_parser.parse(lexed)
                    resource.file_path = res_path

                    for res_name in resource.provides:
                        self.resources[res_name] = resource

                    if not res_path in self.path_map:
                        self.path_map[res_path] = []

                    self.path_map[res_path].extend(resource.provides)

        print "\nscanner reources:"
        pp.pprint(self.resources)
        print "\nscanner path_map:"
        pp.pprint(self.path_map)

            

    




