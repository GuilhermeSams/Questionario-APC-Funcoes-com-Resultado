'''Uma equação do 2º grau é completa se todos os seus coeficientes são diferentes de zero. Elabore uma função completa
que recebe três números inteiros a, b e c, que representam os coeficientes de uma equação, e retorne True se a equação
for completa ou False caso contrário.


A Entrada consiste de:
A função recebe como argumento três números inteiros, que representam os coeficientes da equação.

A Saída deve apresentar:
True ou False, de acordo com o enunciado.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, todos os coeficientes são diferentes de zero, então é uma função do segundo grau completa.
No segundo exemplo, um dos coeficientes é igual a zero, logo é uma função do segundo grau incompleta.'''


def completa(a, b, c):
    if a and b and c != 0:
        return True
    else:
        return False


print(completa(1, -7, 0))
