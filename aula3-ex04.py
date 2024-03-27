# Escreva expressões Python correspondentes ao seguinte:

import math;

# O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
# catA = float(input('Insira o valor do Primeiro Cateto: '));
# catB = float(input('Insira o valor do Segundo Cateto: '));
# hip = math.pow(catA, 2) + math.pow(catB, 2);
# raizQdeHip = math.sqrt(hip);
# print('Testosamente ', raizQdeHip);

# O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
# if raizQdeHip == 5:
#     print('A hipotenusa deste triângulo é igual a 5.');
# else:
#     print('A hipotenusa deste triângulo NÃO é igual a 5.');

# A área de um disco com raio a
# raioA = float(input('Insira o valor do Raio do círculo: '));
# area = math.pi * math.pow(raioA, 2);

# print('A área do círculo é de: ', area)

# O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro ( a, b ) e raio r
respostaCirculo = 'S';


while respostaCirculo == 'S':
    raioA = float(input('Insira o valor do Raio do Novo círculo: '));
    centroX = int(input('Insira a posição central deste círculo em X: '));
    centroY = int(input('Insira a posição central deste círculo em Y: '));
    respostaPonto = 'S';
    
    while respostaPonto == "S":    
        ptX = int(input('Insira a posição X do ponto: '));
        ptY = int(input('Insira a posição Y do ponto: '));
        hipotenusa = math.sqrt(pow(ptX-centroX, 2) + pow(ptY-centroY, 2));

        if ((ptY == centroY) and ((abs(ptX - centroX) <= raioA))) or ((ptX == centroX) and ((abs(ptY - centroY) <= raioA))) or (hipotenusa <= raioA):
            isDentrodaArea = True;
            # print('O ponto está dentro da área do círculo');
        else:
            isDentrodaArea = False;
            # print('O ponto NÃO está dentro da área do círculo');

        print('O ponto está dentro da área do círculo?', isDentrodaArea);

        respostaPonto = input('Deseja verificar outro PONTO? S/N ').upper();

    respostaCirculo = input('Deseja verificar outro CÍRCULO? S/N ').upper();

print();
