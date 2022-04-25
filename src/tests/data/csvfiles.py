#!/usr/bin/ env python3
import csv
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool
import time
from typing import Union


def timeout(seconds):
    # Decorator Timeout
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

# 1. abrir o arquivo
with open('/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/data/csv/1-db-atualizado-geral.csv', encoding='utf-8') as arquivo_referencia:
    # 2. ler a tabela
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    # 3. navegar pela tabela
    n = 0
    for l in tabela:
        n += 1
        grupo = (str(l[0]) + (' ' * 30))[:15]
        descricao = (str(l[1]) + (' ' * 30))[:15]
        unidade = (str(l[2]) + (' ' * 30))[:15]
        largura = (str(l[3]) + (' ' * 30))[:15]
        comprimento = (str(l[4]) + (' ' * 30))[:15]
        print(f'{grupo}{descricao}{unidade}{largura}{comprimento}')

        if n == 30:
            break
    """
    for l in tabela:
        id_autor = l[0]
        nome = l[1]
        print(id_autor, nome) # 191149, Diego C B Mariano
    """
