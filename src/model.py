#!/usr/bin env python3
import random

from attachment.workingoutlibs.csvdata import CsvData


class Model(object):
    """..."""
    def __init__(self):
        """..."""
        pass

    def csv_file_processing(self, file_url: str, header: str):
        """..."""
        self.file_url = file_url
        self.header = header

        if self.file_url and self.header:
            csv_obj = CsvData(
                file_url=self.file_url,
                header_list=self.header.split('\t'),
                exclude_row=None)
            
            return csv_obj
        
        return False
