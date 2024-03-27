# Escreva uma função soma2D() que aceita duas listas bidimensionais do mesmo
# tamanho (ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e
# incrementa cada entrada na primeira lista com o valor da entrada correspondente
# na segunda lista.

# Resultado Esperado
# [4, 8, 4, 5]
# [5, 2, 10, 3]
# [8, 4, 6, 6]
            
t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]];
print('Primeira Lista: ', t)
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]];
print('Segunda Lista: ', s)
print('');

def soma2D(t, s):
    novaLista = [];

    for i in range(len(t)):
        coluna = 0;
        novoItem = [];

        for j in range(len(t[i])):
            novoItem.append(t[i][coluna] + s[i][coluna]);
            coluna += 1;  
        
        novaLista.append(novoItem);

    print(novaLista);

print('Soma de cada um dos sub itens, de cada um dos itens de cada uma das 2 listas Apresentadas acima:')
soma2D(t, s);
print()
