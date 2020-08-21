import sqlite3

"""
Script para povoamento das tabelas

"""


def inserir_registro(registro, reg, data):
    """função para inserir cada registro nas devidas tabelas"""
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    if reg == '0000':
        cursor.execute('INSERT INTO desafio_tabela_0000 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro[6], registro[7], registro[8], registro[9], registro[10], registro[11],
                        registro[12], registro[13], data))
        connection.commit()

    elif reg == '0140':
        cursor.execute('INSERT INTO desafio_tabela_0140 VALUES (NULL,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro[6], registro[7], registro[8], data))
        connection.commit()

    elif reg == '0150':
        cursor.execute('INSERT INTO desafio_tabela_0150 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro[6], registro[7], registro[8], registro[9], registro[10], registro[11],
                        registro[12], data))
        connection.commit()

    elif reg == '0200':
        cursor.execute('INSERT INTO desafio_tabela_0200 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro[6], registro[7], registro[8], registro[9], registro[10], registro[11], data))
        connection.commit()

    elif reg == 'C100':
        cursor.execute('INSERT INTO desafio_tabela_C100 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro[6], registro[7], registro[8], registro[9], registro[10], registro[11],
                        registro[12], registro[13], registro[14], registro[15], registro[16], registro[17],
                        registro[18], registro[19], registro[20], registro[21], registro[22], registro[23],
                        registro[24], registro[25], registro[26], registro[27], registro[28], data))
        connection.commit()

    elif reg == 'C170':
        # formatação do campo VL_ITEM para que o valor tenha 2 casas decimais.
        registro_formated = float(registro[6].replace(',', '.'))
        cursor.execute('INSERT INTO desafio_tabela_C170 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                        registro_formated, registro[7], registro[8], registro[9], registro[10], registro[11],
                        registro[12], registro[13], registro[14], registro[15], registro[16], registro[17],
                        registro[18], registro[19], registro[20], registro[21], registro[22], registro[23],
                        registro[24], registro[25], registro[26], registro[27], registro[28], registro[29],
                        registro[30], registro[31], registro[32], registro[33], registro[34], registro[35],
                        registro[36], data))
        connection.commit()

    cursor.close()
    connection.close()


lista_meses = ['jan2019', 'fev2019', 'mar2019', 'abr2019', 'mai2019',
               'jun2019', 'jul2019', 'ago2019', 'set2019', 'out2019',
               'nov2019', 'dez2019'
               ]

for mes in lista_meses:
    with open(f'arquivos/{mes}.txt', 'r') as file:

        file.seek(0, 0)
        registro = file.readlines()

        for i in range(len(registro)):
            # extrai cada registro dos arquivos txt, coloca numa lista e manda para um função inserir
            if '|0000|' in registro[i][0:6]:
                reg = '0000'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)

            elif '|0140|' in registro[i][0:6]:
                reg = '0140'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)

            elif '|0150|' in registro[i][0:6]:
                reg = '0150'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)

            elif '|0200|' in registro[i][0:6]:
                reg = '0200'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)

            elif '|C100|' in registro[i][0:6]:
                reg = 'C100'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)

            elif '|C170|' in registro[i][0:6]:
                reg = 'C170'
                campos = registro[i].strip().split('|')
                lista_campos = campos[1:-1]
                inserir_registro(lista_campos, reg, mes)
