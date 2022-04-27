#!/usr/bin env python3
import random

class Model(object):
    """..."""
    def __init__(self):
        """..."""
        pass

    def csv_file_processing(self, file_url: str, header: str) -> bool:
        """..."""
        self.file_url = file_url
        self.header = header

        if self.file_url and self.header:
            print(file_url)
            print(header)
            return True
        
        print("Nope")
        return False
