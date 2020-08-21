import sqlite3

"""
Query traz o somatória do campo VL_ITEM anual

SELECT SUM(VL_ITEM) 
FROM desafio_tabela_C170

"""

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.execute('SELECT SUM(VL_ITEM) FROM desafio_tabela_C170')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
connection.close()
