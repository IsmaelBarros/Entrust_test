import sqlite3

"""
Query traz o produto totaliza R$ 79,05 no mês de dezembro

SELECT a.REG, a.COD_ITEM, b.DESCR_ITEM, a.DATA, SUM(a.VL_ITEM) as total 
FROM desafio_tabela_c170 as a
INNER JOIN desafio_tabela_0200 as b 
ON a.COD_ITEM=b.COD_ITEM AND a.DATA=b.DATA 
WHERE a.DATA="dez2019" 
GROUP BY a.REG, a.COD_ITEM, b.DESCR_ITEM, a.DATA 
HAVING total = 79.0

"""

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.execute(
    'SELECT a.REG, a.COD_ITEM, b.DESCR_ITEM, a.DATA, SUM(a.VL_ITEM) as total FROM desafio_tabela_c170 as a INNER JOIN desafio_tabela_0200 as b ON a.COD_ITEM=b.COD_ITEM AND a.DATA=b.DATA WHERE a.DATA="dez2019" GROUP BY a.REG, a.COD_ITEM, b.DESCR_ITEM, a.DATA HAVING total = 79.05')

for linha in cursor.fetchall():
    print(linha)

cursor.close()

cursor = connection.cursor()

connection.close()
