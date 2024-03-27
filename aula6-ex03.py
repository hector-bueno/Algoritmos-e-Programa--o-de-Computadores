# Escreva um laço for que exiba a seguinte sequência de números, um por linha.

print("\nInteiros de 3 até 12, inclusive este.");
for i in range(3, 12+1, 1):
    print(i);

print("\nInteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1");
# (isto é, 0, 2, 4, 6, 8).
for i in range(0, 9, 2):
    print(i);


print("\nInteiros de 0 até (mas não incluindo) 24, com um passo de 3.");
for i in range(0, 24, 3):
    print(i);

print("\nInteiros de 3 até (mas não incluindo) 12, com um passo de 5.");
for i in range(3, 12, 5):
    print(i);