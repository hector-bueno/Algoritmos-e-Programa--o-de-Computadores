s = '0123456789';

def exibeLista(lista, numInicio, numFim):
    resultado = '';

    for i in lista:
        if (i >= numInicio) and (i <= numFim):
            resultado = resultado + i;
    
        if i >= numFim:
            return resultado;

print(exibeLista(s, '2', '4'));
print(exibeLista(s, '7', '8'));
print(exibeLista(s, '1', '7'));
print(exibeLista(s, '0', '3'));
print(exibeLista(s, '7', '9'));