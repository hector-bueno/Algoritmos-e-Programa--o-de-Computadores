# Desenvolver os diagramas de blocos e as codificações em português estruturado usando
# laço incondicional (para) do seguinte problema: Construir um programa que apresente a
# soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).

num = 1;
soma = 0;

for num in range(1, 101):
    soma = soma + num;

print(soma);