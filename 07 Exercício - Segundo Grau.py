'''O código abaixo é a implementação de duas funções. A função calcula_delta recebe os coeficientes a, b e c de uma
função do segundo grau (a×x2+b×x+c) e o valor de x. Após o cálculo do delta, caso esse não seja negativo, é calculado
o valor numérico da função a partir de x pela função calcula_f.

def calcula_f(a,b,c,x):
  print((a*x*2)+(b*x)+c)

def calcula_delta(a,b,c,x):
  delta = (b*b - 4*a*c)
  if(delta < 0):
    return "Equacao sem raizes reais"
  else:
    return "O resultado de f(" + x + ") eh: " + str(calcula_f(a,b,c,x))
A partir dos exemplos disponibilizados, identifique os erros que o código acima apresenta e faça os ajustes necessários
para que funcione de maneira correta.

A Entrada consiste de:
A função calcula_delta(a,b,c,x), onde a, b, c e x, todos inteiros.

A Saída deve apresentar:
Uma string, como indica o enunciado e os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
É aconselhável que a depuração seja realizada majoritariamente em seu próprio computador e não no Moodle. Assegure-se de
 que sua resposta está correta antes de enviar para que não haja desconto na pontuação.

Descrição dos Exemplos:
No primeiro exemplo, como o delta não é negativo, calcula-se o valor numérico de f(1), que é -12.
No segundo exemplo, o delta é negativo então a função calcula_f não é invocada.'''


def calcula_f(a, b, c, x):
  print((a*x*2)+(b*x)+c)


def calcula_delta(a, b, c, x):
  delta = (b**2) - 4*a*c
  if delta < 0:
    return "Equacao sem raizes reais"
  else:
    return "O resultado de f(" + str(x) + ") eh: " + str(calcula_f(a, b, c, x))


print(calcula_delta(4, 0, -16, 1))
