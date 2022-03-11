'''Pedry é um avido usuário de diversos serviços da internet. Sejam serviços de streaming, redes sociais ou jogos online
 ele está sempre criando novas contas, e com isso criando também novas senhas. Normalmente a maioria dessas senhas
 requer pelo menos um dígito numérico para aumentar a segurança, mas nem todo número escolhido é tão seguro assim.
 Números muito simples, como sequências diretas do tipo "1234" ou datas importantes como ano de nascimento ou  datas
 de aniversário são as primeiras tentativas de invasores maliciosos invadirem sua conta, roubarem seu loot e
 distribuírem em fóruns de procedência duvidosa.

Portanto Pedry acredita que o número escolhido deve ser o menos óbvio possível, mas não completamente aleatório.
Se, por exemplo, ele somar todos os dígitos da data de seu aniversário ele terá gerado um novo número, não completamente
 óbvio mas ainda sim com um sentido lógico atrelado. Mesmo que ele não consiga se lembrar desse número em um dado
 momento ele sempre saberá o processo necessário para obtê-lo.

Crie uma função recursiva soma_digitos() que receba um número inteiro qualquer como parâmetro e retorne a soma de todos
os seus dígitos.



A Entrada consiste de:
A função recebe um número inteiro qualquer como parâmetro.
A Saída deve apresentar:
A função deve retornar um número inteiro representando a soma de todos os dígitos do número recebido como parâmetro.

Observações
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a função soma_digitos() recebe como parâmetro o número inteiro 31091999. Separando este inteiro em
cada um dos seus dígitos a soma a ser executada é: 3 + 1 + 0 + 9 + 1 + 9 + 9 + 9 = 41.
No segundo exemplo, a função soma_digitos() recebe como parâmetro o número inteiro 1042001. Separando este inteiro em
cada um dos seus dígitos a soma a ser executada é: 1 + 0 + 4 + 2 + 0 + 0 + 1 = 8
'''

def soma_digitos(n):


print(soma_digitos(31091999))