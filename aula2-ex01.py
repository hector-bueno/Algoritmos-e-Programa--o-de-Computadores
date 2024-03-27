# Escreva expressões algébricas Python correspondentes aos seguintes comandos:

# A soma dos 5 primeiros inteiros positivos.

num = 1;
soma = 0;

for num in range(1, 6):
    soma = soma + num;

print('A soma dos 5 primeiros inteiros positivos:',soma);

# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).

sara = 23;
mark = 19;
fatima = 31;

media = (sara + mark + fatima) / 3;
print('A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).', media);

# O número de vezes que 73 cabe em 403.

print('O número de vezes que 73 cabe em 403.', 403 // 73);

# O resto de quando 403 é dividido por 73.

print('O resto de quando 403 é dividido por 73.', 403 % 73);

# 2 à 10ª potência.

print('2 à 10ª potência. (2 ** 10)', 2 ** 10);

mult = 2;
for pot in range(1,10):
    mult = mult * 2;

print('2 à 10ª potência. (utilizando for)', mult);

# O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).

alturaSara = 54;
alturaMark = 57;

print('O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).', abs(alturaSara - alturaMark));


# O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.

preco1 = 34.99;
preco2 = 29.95;
preco3 = 31.50;

print('O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.', min(preco1, preco2, preco3));