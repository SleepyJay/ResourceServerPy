
import os.path
import re
from Lexer.Directive import Directive

__package__ = "Lexer.ConfigLexer"

BASE_TYPE = 'rsc'
DEF_OPEN_STRING = '//@'

class ConfigLexer(object):
    def __init__(self, opening_string=DEF_OPEN_STRING):
        self.re_line = re.compile('{}\s?([A-Za-z._]+) (.*)'.format(opening_string))
        self.re_dots = re.compile('([^.]+)\.(.+)')

    #
    def lexFile(self, file_path):
        f = open(file_path, 'r')
        
        lexed = []
        line_num = 1

        for line in f:
            directive = self.lexLine(line, line_num)
            if directive:
                # We don't type END
                # Stop looking for directives, thank you.
                if directive.name == 'END':
                     return lexed
                directive.file_path = file_path

                lexed.append(directive)

    #
    def lexLine(self, line, line_num=1):
        ptrn = self.re_line # directive [params]
        dots = self.re_dots # [type:]directive

        m = ptrn.match(line)

        if m:
            type = BASE_TYPE
            name = m.group(1)
            params = m.group(2)

            d = dots.match(name)
            if d:
                type = d.group(1)
                name = d.group(2)

            directive = Directive(type, name, params, line_num, line)
            return directive

        return None










        
    
    
    
    
    




