temperaturas = [
    [10, 13, 16, 21, 24, 27, 30],
    [11, 14, 17, 20, 23, 26, 29],
    [9, 12, 15, 18, 21, 24, 27]
];

print(temperaturas);
print('cidade 1 \t\t\t cidade 2\t\t\t cidade 3');
print();

print('Primeira Cidade, 7 dia');
print(temperaturas[0][6]); # espera-se 30
print();

print('Segunda Cidade, 5 dia'); # espera-se 23
print(temperaturas[1][4]);
print();
print("---------------------");

frutas = ["maçã", "banana", "laranja"];

for fruta in frutas:
    print(fruta);

print("---------------------");

for lista in frutas:
    print(lista);

print();
