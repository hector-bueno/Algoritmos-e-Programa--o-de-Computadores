# Ler uma temperatura em graus Celsius e apresentá-la convertida
# em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
# sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

temp = float(input("Insira a temperatura em ºC a ser convertida: "));

conversao = temp * 9 / 5 + 32;

print('A temperatura ', temp,'ºC foi convertida para ', conversao,'ºF');