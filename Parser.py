#

class Parser(object):

    def __init__(self):
        self.classpaths = []

    #
    def parse(self, lexed):
        # config = Config()
        #
        # for directive in lexed:
        #     if(directive.name == 'classpath'):
        #         self.classpaths.append(directive.params)
        #
        #     elif(directive.name == 'verbose'):
        #         self.collectVerbose(directive)
        #
        #     elif(directive.name == 'echo'):
        #         print directive.params
        #
        #     else:
        #         # Probably want an exception here...
        #         pass
        #
        # return config
        pass


    #
    def collectVerbose(self, directive):
        if directive.params == 'on':
            self.verbose = True
            
        elif directive.params == 'off':
            self.verbose = False

        elif directive.params == 'lexing':
            self.verboseLexing = True

        elif directive.params == 'parsing':
            self.verboseParsing = True

        elif directive.params == 'scanning':
            self.verboseScanning = True

        else:
            pass






    


    
    
    
    



