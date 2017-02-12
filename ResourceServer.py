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

class ResourceServer(object):
    
    def __init__(self):
        self.config = Config()
    
    #
    def start(self, options):
        print("\nResourceServer: starting\n")
        self.config.start()
    
    
    
    



