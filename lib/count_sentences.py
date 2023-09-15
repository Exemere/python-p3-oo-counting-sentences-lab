#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Input value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
