# Supondo que a variável previsão tenha recebido a string
# 'It will be a sunny day today'
# escreva instruções Python correspondentes a estas atribuições:

previsao = 'It will be a sunny day today';

print('A variável cont, a quantidade de ocorrências da string \'day\' na string previsão.');
cont = previsao.count('day');
print(cont);

print('A variável clima, o índice em que a substring \'sunny\' começa.');
clima = previsao.index('sunny');
print(clima);

print('A variável troca, uma cópia de previsão na qual cada ocorrência da substring \'sunny\' é substituída por \'cloudy\'.');
troca = previsao.replace('sunny', 'cloudy');
print(troca);
