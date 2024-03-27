# Comece executando as instruções de atribuição:

# >>> s1 = 'ant'
# >>> s2 = 'bat'
# >>> s3 = 'cod'
            
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de
# avaliar para:  


s1 = 'ant';
s2 = 'bat';
s3 = 'cod';

# 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3);

# 'ant ant ant ant ant ant ant ant ant ant'
uniao = '';
for i in range(10):
    if i == 0:
        uniao = s1;
    else:
        uniao = uniao + ' ' + s1;

print(uniao);

# 'ant bat bat cod cod cod'
uniao = '';
lista = [];

lista.append(s1);
lista.append(s2);
lista.append(s3);

for j in range(3):
    if j == 0:
        uniao = s1;
    else:
        if j == 1:
            uniao = uniao + ((' ' + s2) * 2);
        else:
            uniao = uniao + ((' ' + s3) * 3);
    
print(uniao);

# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
uniao = '';

uniao = (s1 + ' ' + s2 + ' ') * 7;

print(uniao);

# 'batbatcod batbatcod batbatcod batbatcod batbatcod'
uniao = '';

uniao = (s2 * 2 + s3 + ' ') * 5;

print(uniao);