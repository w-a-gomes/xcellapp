#!/usr/bin/ env python3
import os
import pathlib
import time
import openpyxl

from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool

def timeout(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            pool = ThreadPool(processes=1)
            result = pool.apply_async(function, args=args, kwds=kwargs)
            try:
                return result.get(timeout=seconds)
            except TimeoutError as e:
                return e
        return wrapper
    return decorator

@timeout(5)
def get_excel_file():
    existing_workbook_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'tests/data/banco.xlsx')
    return openpyxl.load_workbook(existing_workbook_path)

excel_file = get_excel_file()

if isinstance(excel_file, TimeoutError):
    print('Demorou muito para carregar o documento. Algo saiu errado!')
else:
    print(excel_file.sheetnames)
