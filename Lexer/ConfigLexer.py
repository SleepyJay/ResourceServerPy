

from Lexer import Lexer

__package__ = "Lexer.ConfigLexer"

class ConfigLexer(Lexer):

    #
    def buildValidDirectives(self):
        self.valid_directives = { 'classpath', 'verbose', 'echo' }



    
    
    
    
    




