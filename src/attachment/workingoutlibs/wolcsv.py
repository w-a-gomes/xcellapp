#!/usr/bin/ env python3
import csv
import os.path


class RS(object):
    def __init__(self, value):
        self.__reais = 0
        self.__centavos = 0
        self.__valor_texto = '0,00'
        self.__valor_float = 0.0

        self.__set_value(value)
    
    def __set_value(self, value):
        if isinstance(value, int):
            self.__reais = value
            self.__centavos = 0
            self.__valor_texto = f'{value},00'
            self.__valor_float = float(self.__valor_texto.replace(',', '.'))

        elif isinstance(value, float):
            self.__valor_float = value

            value = str(value).split('.')
            self.__reais = int(value[0])
            self.__centavos = int(value[1])

            if len(value[1]) == 1:
                self.__valor_texto = f'{value[0]},{value[1]}0'
            else:
                self.__valor_texto = f'{value[0]},{value[1]}'

        elif isinstance(value, str):
            value = (
                value.lower().replace('r$', '')
                .replace('.', '').replace(',', '.')
                .replace(' ', '')
            )
            
            if '.' in value:
                reais_cent = value.split('.')
                self.__reais = int(reais_cent[0])
                self.__centavos = int(reais_cent[1])
                if len(reais_cent[1]) == 1:
                    self.__valor_texto = f'{reais_cent[0]},{reais_cent[1]}0'
                else:
                    self.__valor_texto = f'{reais_cent[0]},{reais_cent[1]}'
            else:
                self.__reais = int(value)
                self.__centavos = 0
                self.__valor_texto = f'{self.__reais},00'
            
            self.__valor_float = float(self.__valor_texto.replace(',', '.'))
    
    @property
    def reais(self):
        return self.__reais
    
    @reais.setter
    def reais(self, value):
        self.__set_value(value)
    
    @property
    def centavos(self):
        return self.__centavos
    
    @centavos.setter
    def centavos(self, value):
        self.__set_value(value)
    
    @property
    def valor_em_texto(self):
        return self.__valor_texto
    
    @valor_em_texto.setter
    def valor_em_texto(self, value):
        self.__set_value(value)
    
    @property
    def valor_em_float(self):
        return self.__valor_float
    
    @valor_em_float.setter
    def valor_em_float(self, value):
        self.__set_value(value)
    
    def __repr__(self):
        return f'<RS object: {self.__valor_texto}>'


class WolCsv(object):
    """CSV datas"""
    def __init__(self, file_url: str) -> None:
        """Constructor"""
        self.__file_url = file_url
        self.__filename = file_url.replace(os.path.dirname(file_url) + '/', '')
        self.__csv_datas = self.__load_data()
        self.__header_found = False

    @property
    def file_url(self) -> str:
        """..."""
        return self.__file_url

    @property
    def filename(self) -> str:
        """..."""
        return self.__filename
        
    @property
    def csv_datas(self) -> list:
        """csv_datas"""
        return self.__csv_datas
    
    @property
    def header_found(self) -> bool:
        return self.__header_found

    def __load_data(self) -> list:
        # ...
        csv_datas = []

        with open(self.__file_url, encoding='utf-8') as csv_file:
            # worksheet = csv.DictReader(csv_file) newline=''
            worksheet = csv.reader(csv_file, delimiter=',')
            
            header = None
            header_found = False
            for row in worksheet:
                # if not self.__row_is_empty(row):
                if not header_found:
                    header = row
                    header_found = True

                else:
                    items = []
                    for field, item in zip(header, row):
                        items.append(
                            {
                                'field': field,
                                'value': {item: self.__item_type(item)}
                            },
                        )
                    csv_datas.append(items)
        
        return csv_datas
    
    @staticmethod
    def __item_type(item):
        item_clean = (
            item.lower().replace('r$', '')
            .replace('.', '').replace(',', '.')
            .replace(' ', ''))
        
        if item_clean.replace('.', '').isdigit():
            new_item = RS(item)

            if 'R$' in item:
                # return new_item
                return new_item.valor_em_float
            elif '.' in item_clean:
                return float(item_clean)
            else:
                return int(item_clean)

        return item

    @staticmethod
    def __row_is_empty(row) -> bool:
        # ...
        row_is_empty = True

        for item_row in row:
            if item_row.strip():
                row_is_empty = False
                break
        
        return row_is_empty


if __name__ == '__main__':
    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Geral                              |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/tdata/csv/1-db-atualizado-geral.csv'
    csv_obj = WolCsv(file_url=url)
    for x in csv_obj.csv_datas[0]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[1]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[2]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[3]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[4]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[-1]:
        print(x)
    
    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Banco_Material                     |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/tdata/csv/1-db-atualizado-material.csv'
    csv_obj = WolCsv(file_url=url)
    for x in csv_obj.csv_datas[0]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[1]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[4]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[5]:
        print(x)

    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Cadastro                           |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/tdata/csv/1-db-atualizado-cadastro.csv'
    csv_obj = WolCsv(file_url=url)
    for x in csv_obj.csv_datas[0]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[1]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[4]:
        print(x)
    print('---')
    for x in csv_obj.csv_datas[5]:
        print(x)

    for i in ['1700', '1700.50', '1.700', '1.700,50', 1700, 1700.50]:
        r = RS('1700')
        print(r.reais, 'Reais e', r.centavos, 'centavos')
        print(r.valor_em_float)
        print(r.valor_em_texto)
        print('----')
