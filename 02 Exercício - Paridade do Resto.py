'''Crie um programa que lê dois inteiros positivos x e y e chame uma função chamada resto que calcula o resto da divisão
desses inteiros.
Caso haja resto, crie outra função chamada par_ou_impar que faz a verificação desse resto e retorna "Par" ou "Impar".

Dependendo do valor retornado da função, imprima "Divisao inteira" caso não haja resto, "Par" caso o resto seja par ou
"Impar" caso o resto seja impar.

Entrada
A entrada consiste de dois inteiros positivos.

Saída
A saída será uma das mensagens dependendo do resultado da função.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, os valores 5 e 3 tem resto 2, então a saída será "Par".
No segundo exemplo, os valores 2 e 2 tem o resto 0, então a saída será "Divisão inteira".
No terceiro exemplo, os valores 5 e 2 tem o resto 3, então a saída será "Impar".'''
x = int(input())
y = int(input())

resto_div = x % y


def resto(x, y):
    if resto_div == 0:
        return "Divisao Inteira"

def par_ou_impar(x, y):
    if resto_div != 0:
        if resto_div % 2 == 0:
            return "Par"
        return "Impar"


if resto_div == 0:
    print(resto(x, y))
else:
    print(par_ou_impar(x, y))