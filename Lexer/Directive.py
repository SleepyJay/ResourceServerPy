#


class Directive(object):

    def __init__(self, type, name, params, line_num):
        self.type = type
        self.name = name
        self.params = params
        self.line_num = line_num
        self.file_path = ''
        self.line = '' # optional

    def __str__(self):
         return "{}: {}, {}, '{}'".format(self.line_num, self.type, self.name, self.params)

    
    




