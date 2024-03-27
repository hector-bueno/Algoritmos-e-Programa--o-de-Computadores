import math;

resposta = 'S';

def calculaPerimetro (raio):
    perimetro = 2 * math.pi * raio;
    return perimetro;

while resposta == 'S':
    raio = 0;

    while raio <= 0:
        raio = float(input('Insira o valor do Raio do círculo (valor maior que Zero): '));

        if raio <= 0:
            print ('Favor inserir um valor maior que Zero: ');
        else:
            print(calculaPerimetro(raio));

    resposta = input('Deseja verificar outro círculo? (S/N): ').upper();
