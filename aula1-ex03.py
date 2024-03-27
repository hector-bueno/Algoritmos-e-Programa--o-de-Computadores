# Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
# representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
# (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
# média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
# Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
# da média obtida pelo aluno

n1 = float(input('Insira o valor da Primeira Nota do Aluno: '));
n2 = float(input('Insira o valor da Segunda Nota do Aluno: '));
n3 = float(input('Insira o valor da Terceira Nota do Aluno: '));
n4 = float(input('Insira o valor da Quarta Nota do Aluno: '));

md = (n1 + n2 + n3 + n4) / 4;

if (md >= 5):
    print('Aluno aprovado com média ', md);
else:
    print('Aluno reprovado com média ', md);