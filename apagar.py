# O seguinte programa em Python calcula o menor de três números.  

# numero1 = eval(input("Digite o número 1: "))
# numero2 = eval(input("Digite o número 2: "))
# numero3 = eval(input("Digite o número 3: "))

def maiorNumero (numero1, numero2, numero3):

    if(numero1 > numero2) and (numero1 > numero3) and (numero2 > numero3): 
        print("O maior número é o primeiro: ",numero1) 
    if(numero2 > numero1) and (numero2 > numero3) and (numero3 > numero1): 
        print("O maior número é o segundo: ",numero2) 
    if (numero3 > numero1) and (numero3 > numero2) and (numero1 > numero2): 
        print("O maior número é o terceiro: ",numero3) 

    print("fim")

# maiorNumero(7, 9, 3);
# maiorNumero(3, 3, 3);
# maiorNumero(9, 5, 2);

# A
# salario = float(input('Digite o salario: '))
# tempo_casa = int(input('Digite o tempo de casa: '))
# if salario >= 5:
#     bonus = salario * 20 / 100 
# else:
#     bonus = salario * 10 / 100 
# print(f'O bonus é R$ {bonus:.2f}')	

#B
# salario = int(input('Digite o salario: '))
# tempoCasa = int(input('Digite o tempo em anos que está na empresa: ')) 
# if tempoCasa >= 5:
#     bonus = salario * 20 / 100 
# elif:
# bonus = salario * 10 / 100 
# print('O bonus é R$: ',bonus) 
# print('O salário é R$: ',salario+bonus)

#C
# salario = eval(input('Digite o salario: '))
# tempoCasa = int(input('Digite o tempo em anos que está na empresa: ')) 
# if tempoCasa >= 5:
#     bonus = salario * 20 / 100 
# else:
#     bonus = salario * 10 / 100 
# print('O bonus é R$: ',bonus)

# salario = int(input('Digite o salario: '))
# tempoCasa = int(input('Digite o tempo em anos que está na empresa: ')) 
# if tempoCasa >= 5:
#     bonus = salario + salario * 20 / 100 
# else:
#     bonus = salario + salario * 10 / 100 
# print('O bonus é R$: ',bonus)

# tempoCasa = int(input('Digite o tempo em anos que está na empresa: ')) 
# if tempoCasa >= 5:
#     bonus = 20 / 100
# else: bonus = 10 / 100 
# print('O bonus é R$: ',bonus)
    
# a.
# adivinha = input("Digite um número") 
# if adivinha == 56: 
#     print("Você acertou!!!") 
# elif adivinha < 56: 
#     print("Seu palpite está ABAIXO do número") 
# else: 
#     print("Seu palpite está ACIMA do número")

# b.	
adivinha = eval(input("Digite um número")) 
if adivinha == 56: 
    print("Você acertou!!!") 
elif adivinha < 56: 
    print("Seu palpite está ABAIXO do número")
else: 
    print("Seu palpite está ACIMA do número")

# c.	
# adivinha = input("Digite um número") 
# if adivinha == 56: 
#     print("Você acertou!!!") 
# elif adivinha < 56: 
#     print("Seu palpite está ABAIXO do número") 
# elif adivinha < 56: 
#     print("Seu palpite está ACIMA do número")

# d.	
# adivinha = eval(input("Digite um número")) 
# if adivinha == 56: 
#     print("Você acertou!!!") 
# elif adivinha < 56: 
#     print("Seu palpite está ABAIXO do número") 
# elif adivinha < 56: 
#     print("Seu palpite está ACIMA do número")

# e.	
# adivinha = eval(input("Digite um número")) 
# if adivinha == 56: 
#     print("Você acertou!!!") 
# elif adivinha < 56: 
#     print("Seu palpite está ABAIXO do número") 
#     print("Seu palpite está ACIMA do número")