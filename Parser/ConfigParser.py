#

from Config import Config

class ConfigParser(object):

    def __init__(self, res_path, res_name, res_type):
        self.config = Config()
        self.config.res_path = res_path
        self.config.res_name = res_name
        self.config.res_type = res_type

    #
    def parse(self, lexed):
        for directive in lexed:
            name = directive.name

            if name == 'classpath':
                self.collectClasspath(directive)

            elif name == 'verbose':
                self.collectVerbose(directive)

            elif name == 'echo':
                self.collectEcho(directive)

        return self.config


    #
    def collectClasspath(self, directive):
        # todo: create rewrite directive here?
        class_path = directive.params
        self.config.classpaths.append(class_path)

    #
    def collectVerbose(self, directive):
        params = directive.params
        if params and params == 'off':
            self.config.verbose = False
        else:
            self.config.verbose = True







    


    
    
    
    



