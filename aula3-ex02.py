# Dada a lista de notas de trabalho de casa dos alunos

# >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# escreva:


notas = [9, 7, 7, 10, 3, 9, 6, 6, 2];

# Uma expressão que avalia para o número de 7 notas.
cont = 0;

for i in range(len(notas)):
    if notas[i] == 7:
        cont = cont + 1;

print('A quantidade de \'7\' é de :', cont);

# Uma instrução que muda a última nota para 4.
notas[len(notas)-1] = 4;
print(notas);

# Uma expressão que avalia para a nota mais alta.
print('Nota mais alta:', max(notas));

# Uma instrução que classifica as notas da lista.
notas.sort();
print(notas);

# Uma expressão que avalia para a média das notas.
soma = 0;
media = 0;

for nota in notas:
    soma = soma + nota;

media = soma / len(notas)

print(media);