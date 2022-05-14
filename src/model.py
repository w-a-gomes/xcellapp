#!/usr/bin env python3
import random

from attachment.workingoutlibs.wolcsv import WolCsv


class Model(object):
    """..."""
    def __init__(self):
        """..."""
        pass

    def csv_file_processing(self, file_url: str):
        """..."""
        self.file_url = file_url

        if self.file_url:
            csv_obj = WolCsv(file_url=self.file_url)
            return csv_obj
        
        return False
