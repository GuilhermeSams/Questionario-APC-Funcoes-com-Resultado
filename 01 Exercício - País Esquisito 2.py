'''Pedro e Guilherme passaram o ano no país esquisito e agora estão planejando continuar sua aventura! Porém para o
espanto de ambos, Wil e Jon, nativos do país da águia careca resolveram ir com vocês para fugir da cidade também e
conhecer o mundo! Muito bom né...? Mas agora o problema se inverteu, eles não conseguem entender como o resto do mundo
usa medidas tão estranhas. Como eles são muito orgulhosos, (alguns chamariam de "patriotismo") não estão dispostos a
usar uma máquina conversora de medidas como Pedro e Guilherme usaram durante esse último longo ano. Eles usarão todas
as medidas que encontrarem fora do país como se ela estivesse na medida de seu país. Você, como grande amigo e
conterrâneo deles, fará ao menos uma função compensa que recebe dois argumentos, um inteiro n que representa o valor da
medida e uma string m sendo o tipo da medida, caso o valor de n e o seu valor convertido para a medida desse país forem
iguais, retorne "AHA quem precisa de conversor ?", caso contrario, retorne "Ai irmao eh melhor converter isso ai...".

Regra 1: 1 medida de comprimento estrangeira equivale a 0.62137 medida de comprimento do país.
Regra 2: 0º na temperatura estrangeira equivale a 32º na temperatura desse país. (use a fórmula n∗(9/5)+32 para fazer a
conversão e use a divisão entre números reais).
Regra 3: 5 moedas estrangeiras equivalem a 1.0 moeda deste país.

A Entrada consiste de:
Parâmetros da função compensa que são um número inteiro n(0<=n<=10000) representando a medida e uma string m que é a
medida de conversão. As medidas podem ser somente 3, comprimento, temperatura e dinheiro.

A Saída deve apresentar:
Sua função deve retornar "AHA quem precisa de conversor ?" caso os valores convertidos forem iguais, ou "Ai irmao eh
melhor converter isso ai...", caso contrário, ambos sem aspas.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Para as fórmulas de comprimento e dinheiro, pode-se usar regra de três.

Descrição dos Exemplos:
No primeiro exemplo, o resultado é "AHA quem precisa de conversor ?" pois o valor convertido e o não convertido são
iguais.
No segundo exemplo,o resultado é "Ai irmao eh melhor converter isso ai..." porque os valores convertido e não
convertido são diferentes.'''


def compensa(n, m):
    if m == 'comprimento':
        comp = n // 0.62137
        if comp == n:
            return "AHA quem precisa de conversor ?"
        return "Ai irmao eh melhor converter isso ai..."
    elif m == 'temperatura':
        temp = n * (9/5) + 32
        if temp == n:
            return "AHA quem precisa de conversor ?"
        return "Ai irmao eh melhor converter isso ai..."
    elif m == 'dinheiro':
        din = n / 5
        if din == n:
            return "AHA quem precisa de conversor ?"
        return "Ai irmao eh melhor converter isso ai..."


print(compensa(0, "comprimento"))