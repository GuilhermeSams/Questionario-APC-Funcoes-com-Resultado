'''Dado um número n, crie uma função pattern(n) que imprima números em ordem, seguindo o padrão dos exemplos.


A Entrada consiste de:
O único parâmetro da sua função será o valor 0≤n≤106.

A Saída deve apresentar:
Os valores, de acordo com o padrão dos exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Observe que, ao criar uma função recursiva, é possível realizar operações de impressão antes e depois da chamada
recursiva, o que poderá facilitar a criação do padrão exigido pelo exercício.

Descrição dos Exemplos:
Devem ser analisados para encontrar o padrão.'''


def pattern(n):
    if n > 0:
        print(n)
        pattern(n - 5)
    print(n)

pattern(16)
