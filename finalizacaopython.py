'''compras = []

resp = 's'

while resp == 's':
    compras.append(input('Digite o item da Lista: '))
    resp = input('Deseja Continuar - s para Sim ou n para Não: ')

for x in compras:
    if x == 'banana':
        print('Encontrei a Banana')
    else:
        print('Não encontrei a Banana')

print(compras)'''

num1 = 0
num2 = 0
soma = 0

num1 = int(input("Insira o primeiro número "))
num2 = int(input("Insira o segundo número "))

soma = num1 + num2

print("O valor da soma multiplicado por 2 é:")
print(soma*2)
