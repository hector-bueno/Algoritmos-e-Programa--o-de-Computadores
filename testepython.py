''' inicio comentário
nome = ""

nome = input("Digite seu nome:")
print(nome + " bueno")
print(5+5)
fim comentário

idade = int(input('Digite sua idade: '))
# print(idade) # comentar linha
while idade > 18:
    if idade > 18 and idade < 30:
        print('A idade é maior que 18 e menor que 30')
    idade = int(input("Digite a sua idade: "))
    #else:
        #print('A idade é menor que 18')

x = 1
for x in range(3):
    if idade > 18 and idade < 30:
        print('A idade é maior que 18 e menor que 30')
    idade = int(input("Digite a sua idade: "))
'''

'''texto = 'Curso de Lógica'

for x in texto:
    print(x)'''

compras = ['banana', 'maçã', 'abacaxi']
print(compras)
print(compras[1])

for x in compras:
    print(x)

valores = ['texto', 2, True]
print(valores)