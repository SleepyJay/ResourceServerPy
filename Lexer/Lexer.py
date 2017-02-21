
import os.path
import re
from Directive import Directive

__package__ = "Lexer"

class Lexer(object):
    def __init__(self):
        opening_string = self.getOpeningString()
        self.re_directive = re.compile('{}\s?([A-Za-z._]+) (.*)'.format(opening_string))
        self.re_dir_type = re.compile('([^.]+)\.(.+)')

        self.lexed = []
        self.valid_directives = set()
        self.buildValidDirectives()

    #
    def isValidDirectve(self, name):
        return name in self.valid_directives

    #
    def lexFile(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass
        
        line_num = 1

        for line in f:
            directive = self.lexDirective(line, line_num)
            if directive:
                # Stop looking for directives at EOResources, thank you.
                if directive.name == 'EOResources' or directive.name == 'EOR':
                     break
                directive.file_path = file_path
                self.lexed.append(directive)
            else:
                directives = self.lexLine(line, line_num)
                if directives:
                    self.lexed.extend(directives)

    #
    def lexDirective(self, line, line_num=None):
        """
        This essentially both checks that we have a directive, and if so,
        returns an object based on it
        """
        ptrn = self.re_directive # directive [params]
        dots = self.re_dir_type # [type:]directive

        m = ptrn.match(line)

        if m:
            type = self.getBaseType()
            name = m.group(1)
            params = m.group(2)

            d = dots.match(name)
            if d:
                type = d.group(1)
                name = d.group(2)

            directive = Directive(type, name, params, line_num)
            directive.line = line
            directives.append(directive)

        return directive

    #
    def lexOptions(self, options):
        for key in options:
            directive = Directive(self.getBaseType(), key, options[key])
            self.lexed.append(directive)

    #
    def lexLine(self, line, line_num=None):
        """
        Sometimes you have a situation where your particular file has 'embeded' directives.
        This method is available to find those.
        Should return a list of directive objects or None. Override this in your custom lexer.
        """
        
        # We are not implementing non-standard directives
        return None

    #
    def getOpeningString(self):
        return '//@'

    #
    def getBaseType(self):
        return 'rsc'

    #
    def getLexed(self):
        return self.lexed
    
    #
    def clearLexed(self):
        self.lexed = []
    
    
    
    
    




