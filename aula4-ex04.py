resposta = 'S';

def negativos (lst):
    print('funcao: ', lst);

    for item in lst:
        if item < 0:
            print(item);

lst= [];

while resposta == 'S':

    itemlst = int(input('Insira o número a ser inserido na lista: '));
    lst.append(itemlst);

    print(lst);
    resposta = input('Deseja inserir mais um número na lista? (S/N)').upper();

negativos(lst);

help(negativos);
