#!/usr/bin/ env python3
import csv


class CsvData(object):
    """CSV datas"""
    def __init__(
            self, file_url: str, header_list: list, exclude_row: dict = None
            ) -> None:
        """Constructor"""
        self.__header_list = header_list
        self.__file_url = file_url
        self.__exclude_row = exclude_row
        self.__csv_datas = self.__load_data()
        
    @property
    def csv_datas(self) -> dict:
        """csv_datas"""
        return self.__csv_datas

    def __load_data(self) -> list:
        # ...
        csv_datas = []

        with open(self.__file_url, encoding='utf-8') as csv_file:
            worksheet = csv.reader(csv_file, delimiter=',')
            
            for row in worksheet:
                if not self.__row_is_empty(row) and not self.__row_is_head(row):
                    csv_datas_item = {}
                    
                    for field in enumerate(self.__header_list):
                        csv_datas_item[field[1]] = row[field[0]]
                    
                    if csv_datas_item != self.__exclude_row:
                        csv_datas.append(csv_datas_item)
        
        return csv_datas
    
    def __row_is_head(self, row) -> bool:
        # ...
        row_is_head = False

        found_count = 0
        for item_row in row:
            for item_head in self.__header_list:
                if item_row.lower().strip() == item_head.lower().strip():
                    found_count += 1
                    continue
            
            if found_count == len(self.__header_list):
                row_is_head = True

        return row_is_head

    def __row_is_empty(self, row) -> bool:
        # ...
        row_is_empty = True

        for item_row in row:
            if item_row.strip():
                row_is_empty = False
                break
        
        return row_is_empty


if __name__ == '__main__':
    import pprint

    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Geral                              |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/data/csv/1-db-atualizado-geral.csv'
    headers = [
        'Código', 'Grupo', 'Descrição', 'Unid.', 'Largura', 'Comprimento',
        'Mt2', 'PesoM2', 'Preço', 'PreçoMt2', 'Chapa', 'Peso Kg m', 'Metragem',
        'Preço Kg', 'Peso Mt', 'Preço mt', '% de aumento', 'Preço c/ Aumento',
        'Imp. sob compra', 'Frete', 'Perda', 'Preço Final',
    ]
    con = {'% de aumento': '',
        'Chapa': '',
        'Comprimento': '',
        'Código': '',
        'Descrição': '',
        'Frete': '',
        'Grupo': '',
        'Imp. sob compra': '',
        'Largura': '',
        'Metragem': '',
        'Mt2': ' -   ',
        'Perda': '',
        'Peso Kg m': '',
        'Peso Mt': '0,00',
        'PesoM2': '',
        'Preço': '',
        'Preço Final': ' R$ -   ',
        'Preço Kg': '',
        'Preço c/ Aumento': ' R$ -   ',
        'Preço mt': ' R$ -   ',
        'PreçoMt2': ' -   ',
        'Unid.': ''}
    # csv_obj = CsvData(file_url=url, header_list=headers)
    csv_obj = CsvData(file_url=url, header_list=headers, exclude_row=con)
    pprint.pprint(csv_obj.csv_datas[0])
    pprint.pprint(csv_obj.csv_datas[1])
    pprint.pprint(csv_obj.csv_datas[2])
    pprint.pprint(csv_obj.csv_datas[3])
    pprint.pprint(csv_obj.csv_datas[4])
    pprint.pprint(csv_obj.csv_datas[-1])

    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Banco_Material                     |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/data/csv/1-db-atualizado-material.csv'
    headers = ['Código', 'Grupo', 'Descrição', 'Peso Mt', 'Preço Final']
    csv_obj = CsvData(file_url=url, header_list=headers)
    pprint.pprint(csv_obj.csv_datas[4])
    pprint.pprint(csv_obj.csv_datas[5])

    s = (
        '+---------------------------------------+\n'
        '|    1 - BANCO DE DADOS - Atualizado    |\n'
        '|    Cadastro                           |\n'
        '+---------------------------------------+'
    )
    print(s)
    url = '/home/alien/Scripts/Git/GitHub/xcellapp/src/tests/data/csv/1-db-atualizado-cadastro.csv'
    headers = ['Funcionário', 'Cargo', 'Setor', 'Salário']
    csv_obj = CsvData(file_url=url, header_list=headers)
    pprint.pprint(csv_obj.csv_datas[4])
    pprint.pprint(csv_obj.csv_datas[5])
