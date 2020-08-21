"""
Joao        R$1.237,00
Manoel      R$3.272,00
André       R$757,00
Fernanda    R$2.522,00

cédulas: 100, 50, 20, 10, 5, 2 e 1

"""


def forma_de_pagamento(salario_tabela):

    for nome, salario in salario_tabela.items():
        print(f'Funcionario : {nome} - Salario: R${salario},00')

        notas_de_100 = 0
        notas_de_50 = 0
        notas_de_20 = 0
        notas_de_10 = 0
        notas_de_5 = 0
        notas_de_2 = 0
        notas_de_1 = 0

        notas = {}

        if len(str(salario)) >= 3:
            notas_de_100 = str(salario)[:-2]
            notas['notas_de_100'] = notas_de_100

            valor = int(str(salario)[-2:])
            if valor >= 50:
                notas_de_50 = 1
                notas['notas_de_50'] = notas_de_50
                valor = valor - 50

                if valor >= 40:
                    notas_de_20 = 2
                    notas['notas_de_20'] = notas_de_20
                    valor -= 40
                if valor >= 20 and valor < 40:
                    notas_de_20 = 1
                    notas['notas_de_20'] = notas_de_20
                    valor -= 20
                if valor >= 10:
                    notas_de_10 = 1
                    notas['notas_de_10'] = notas_de_10
                    valor -= 10
                if valor >= 5:
                    notas_de_5 = 1
                    notas['notas_de_5'] = notas_de_5
                    valor -= 5
                if valor >= 4:
                    notas_de_2 = 2
                    notas['notas_de_2'] = notas_de_2
                    valor -= 4
                if valor < 4 and valor >= 2:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor >= 40:
                notas_de_20 = 2
                notas['notas_de_20'] = notas_de_20
                valor -= 40
                if valor >= 20 and valor < 40:
                    notas_de_20 = 1
                    notas['notas_de_20'] = notas_de_20
                    valor -= 20
                if valor >= 10:
                    notas_de_10 = 1
                    notas['notas_de_10'] = notas_de_10
                    valor -= 10
                if valor >= 5:
                    notas_de_5 = 1
                    notas['notas_de_5'] = notas_de_5
                    valor -= 5
                if valor >= 4:
                    notas_de_2 = 2
                    notas['notas_de_2'] = notas_de_2
                    valor -= 4
                if valor < 4 and valor >= 2:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor >= 20 and valor < 40:
                notas_de_20 = 1
                notas['notas_de_20'] = notas_de_20
                valor -= 20
                if valor >= 10:
                    notas_de_10 = 1
                    notas['notas_de_10'] = notas_de_10
                    valor -= 10
                if valor >= 5:
                    notas_de_5 = 1
                    notas['notas_de_5'] = notas_de_5
                    valor -= 5
                if valor >= 4:
                    notas_de_2 = 2
                    notas['notas_de_2'] = notas_de_2
                    valor -= 4
                if valor >= 2 and valor < 4:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor >= 10:
                notas_de_10 = 1
                notas['notas_de_10'] = notas_de_10
                valor -= 10
                if valor >= 5:
                    notas_de_5 = 1
                    notas['notas_de_5'] = notas_de_5
                    valor -= 5
                if valor >= 4:
                    notas_de_2 = 2
                    notas['notas_de_2'] = notas_de_2
                    valor -= 4
                if valor < 4 and valor >= 2:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor >= 5:
                notas_de_5 = 1
                notas['notas_de_5'] = notas_de_5
                valor -= 5
                if valor >= 4:
                    notas_de_2 = 2
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor < 4 and valor >= 2:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor >= 4:
                notas_de_2 = 2
                notas['notas_de_2'] = notas_de_2
                if valor < 4 and valor >= 2:
                    notas_de_2 = 1
                    notas['notas_de_2'] = notas_de_2
                    valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            elif valor < 4 and valor >= 2:
                notas_de_2 = 1
                notas['notas_de_2'] = notas_de_2
                valor -= 2
                if valor == 1:
                    notas_de_1 = 1
                    notas['notas_de_1'] = notas_de_1

            else:
                notas_de_1 = 1
                notas['notas_de_1'] = notas_de_1

        for k, v in notas.items():
            numero_formatado = k.replace('notas_de_', '')

            if v == 1:
                print(f'{v} nota de R${numero_formatado},00 ')
            else:
                print(f'{v} notas de R${numero_formatado},00 ')

        print('==================================================')


if __name__ == '__main__':

    salario_tabela = {
        'Joao': 1237,
        'Manoel': 3273,
        'Andre': 757,
        'Fernanda': 2522,
        'Ismael': 6598,
    }

    forma_de_pagamento(salario_tabela)
