numInicial = eval(input('Insira o número inicial a ser contado: '));
numFinal = eval(input('Insira o número final a ser contado: '));

if numInicial > numFinal:
    aux = numInicial;
    numInicial = numFinal;
    numFinal = aux;

frase = 'Inteiros de ' + str(numInicial) + ' a ' + str(numFinal) + ' (isto é, ' ;

for i in range(numInicial, numFinal+1, 1):
    if i < numFinal:
        frase = frase + str(i) + ', ';
    else:
        frase = frase + str(i);

frase = frase + ').';   

print(frase);