# Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

# A soma de 2 e 2 é menor que 4.

boolSomaUm = 2 + 2 < 4;
print('A soma de 2 e 2 é menor que 4.', boolSomaUm);

# O valor de 7 // 3 é igual a 1 + 1.

boolDivisores = 7 // 3 == 1 + 1;
print('O valor de 7 // 3 é igual a 1 + 1.', boolDivisores);

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
boolQuadrados = 3 ** 2 + 4 ** 2 == 25
print('A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.', boolQuadrados);

# A soma de 2, 4 e 6 é maior que 12.
boolSomaDois = 2 + 4 + 6 > 12;
print('A soma de 2, 4 e 6 é maior que 12.', boolSomaDois);

# 1387 é divisível por 19.
boolDivisaoInteira = 1387 % 19 == 0;
print('1387 é divisível por 19.', boolDivisaoInteira)

# 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
boolPar = 31 % 2 == 0;
print('31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)', boolPar);

# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
boolPrecoMenor = min(34.99, 29,95, 31,50) < 30;
print('O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.', boolPrecoMenor);