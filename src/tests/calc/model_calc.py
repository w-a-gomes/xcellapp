#!/usr/bin env python3


class Model(object):
    def __init__(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        
        elif caption == '%':
            pass

        elif caption == '=':
            value = self.__evaluate()
            if '.0' in str(value):
                value = int(value)
                
            self.value = str(value)

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)
        
        else:
            if self.value: 
                self.operator = caption
                self.previous_value = self.value
                self.value = ''
        
        return self.value
    
    def __evaluate(self):
        return eval(self.previous_value+self.operator+self.value)
