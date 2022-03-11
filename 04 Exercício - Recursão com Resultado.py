'''Crie um programa que lê um número inteiro a (2≤a), chama a função maiorQue1000, que tem como argumento o número
inteiro a, e imprime o valor retornado da função maiorQue1000.

A função maiorQue1000 checa se a é maior que 1000. Se for, retorna a. Se não, chama recursivamente maiorQue1000 com a
elevado ao quadrado como argumento e retorna o resultado dessa chamada recursiva.

Dessa forma, a função maiorQue1000 se chamará recursivamente até que a seja maior que 1000.

A Entrada consiste de:
Um número inteiro positivo.

A Saída deve apresentar:
Um número maior que 1000.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
#Quando a questão pedir um nome específico para a função --> Atenção, a criação de uma função com o nome determinado
pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita
corretamente (sendo case-sensitive o nome da função).

Descrição dos Exemplos:
No primeiro exemplo, foi digitado 2, retornando 65536
No segundo exemplo, foi digitado 1001, retornando 1001.
No terceiro exemplo, foi digitado 5, retornando 390625'''


a = int(input())


def maiorQue1000(a):
    if a > 1000:
        return a
    else:
        return maiorQue1000(a ** 2)


print(maiorQue1000(a))