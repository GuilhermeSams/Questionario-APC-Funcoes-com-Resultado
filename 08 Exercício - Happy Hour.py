'''Dentro da universidade é muito comum haver certas “confraternizações” carinhosamente chamadas de happy hour. Apesar
 de possuir o nome hour, nunca duram somente uma hora, portanto, seu trabalho será fazer uma função chamada hh_duracao
 que receba 6 parâmetros (hora_inicio, minuto_inicio, segundo_inicio, hora_ final, minuto_ final, segundo_ final) e
 retornará quantas horas, minutos e segundos, nessa ordem, durou o happy hour.

A Entrada consiste de:
Não é necessário cuidar dos inputs, porém a função criada deve receber os parâmetros hora_inicio, minuto_inicio,
segundo_inicio, hora_ final, minuto_ final, segundo_ final.

A Saída deve apresentar:
A função deve retornar a duração do evento, sendo a primeira variável as horas, a segunda, os minutos e a terceira,
os segundos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
 irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Lembrando que a duração máxima de um happy hour é 24 horas, que seria quando o horário inicial é exatamente igual ao
horário final.

Descrição dos Exemplos:
No primeiro exemplo, temos um happy hour que começou as 8 da manhã em um dia e terminou as 7 horas, 59 minutos e 59
segundos do outro dia, tendo, assim, a duração de 23 horas, 59 minutos e 59 segundos.
No segundo exemplo, temos o horário inicial igual ao horário final, portanto, temos um evento com 24 horas.'''


def hh_duracao(hora_inicio, minuto_inicio, segundo_inicio, hora_final, minuto_final, segundo_final):

    print(hh_duracao(8,0,0,7,59,59))