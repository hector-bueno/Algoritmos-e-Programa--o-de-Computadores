lista = [];
resposta = 'S';

while resposta != 'N':
    palavra = input('Digite a palavra a ser inserida na lista:');
    lista.append(palavra);


    resposta = input('Deseja inserir mais uma palavra? (S/N)').upper();

print(lista);


for i in lista:
    if len(i) == 4:
        print(i);