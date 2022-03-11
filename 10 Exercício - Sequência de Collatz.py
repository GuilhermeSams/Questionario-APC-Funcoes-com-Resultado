'''A sequência de Collatz é formada da seguinte forma: Dada uma semente inicial s, o próximo número da sequência é n/2
 se n é par e 3n+1 do contrário. Collatz, que está aprendendo programação, implementou uma função recursiva para achar
  o n-ésimo termo da sua sequência.

def collatz(s, n, cont):
    if cont <= n:
        if s % 2 == 0: #é par
            clltz = int(s/2)
        else:
            clltZ = 3*s + 1
        collatz(clltz, n, cont+1)
    else:
        return s

Mas a função dele contém erros de sintaxe e lógica. Ajude-o a depurar o código Python da função collatz.

A Entrada consiste de:
a função collatz(s, n, cont), onde s é a semente, n é o n-ésimo termo da sequência que se quer e cont conta a quantidade
 de vezes que a função recursiva é chamada para parar de gerá-la quando achar o n-ésimo termo.

A Saída deve apresentar:
o n-ésimo termo da sequência de Collatz de semente /(s/).
Exemplo:
o sequência de Collatz gerada com a semente 12 é 12, 6, 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 1, 4, 2, 1 ...
e o seu quinto termo é 5.
'''

cont = 0
def collatz(s, n, cont):
        if s % 2 == 0: #é par
            clltz = int(s/2)
            print(s, end=" ")
            cont += 1
            collatz(s,n,cont)
            return clltz
        elif s % 3 == 0:
            calc = 3*s + 1
        else:
            return s


print(collatz(12, 5, 1))