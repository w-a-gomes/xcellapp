#!/usr/bin env python3
from attachment.workingoutlibs.wolcsv import WolCsv


class Model(object):
    """..."""
    def __init__(self):
        """..."""
        pass

    @staticmethod
    def csv_file_processing(file_url: str):
        """..."""
        if file_url:
            csv_obj = WolCsv(file_url=file_url)
            return csv_obj
        
        return False
