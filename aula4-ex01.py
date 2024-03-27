# Implemente um programa que solicita a temperatura atual em graus Fahrenheit
# do usuário e exibe a temperatura em graus Celsius usando a fórmula:
# celsius = 5 / 9 *(fahrenheit - 32).
# Seu programa deverá ser executado da seguinte forma:

# Digite a temperatura em graus Fahrenheit: 50
# A temperatura em graus Celsius é 10.0

temp = float(input("Digite a temperatura em graus Fahrenheit: "));

conversao = (temp - 32) / 1.8;

print('A temperatura', temp,'ºF em graus Celsius é ', conversao,'ºC');