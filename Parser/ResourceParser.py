#

from Resource import Resource
from Parser import Parser

class ResourceParser(Parser):

    def __init__(self, config):
        self.config = config

    #
    def parse(self, lexed):
        resource = Resource()
        for directive in lexed:
            name = directive.name

            if name == 'import':
                resource.imports.add(directive.params)

            elif name == 'require':
                resource.requires.add(directive.params)

            elif name == 'provides':
                resource.provides.add(directive.params)

            elif name == 'echo':
                self.collectEcho(directive)

        return resource

    







    


    
    
    
    



