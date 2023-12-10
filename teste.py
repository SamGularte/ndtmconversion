import random

tuplas = [('0', '_', '_', 'r', 'q1'), ('q1', '1', 'b', 'r', 'q1'), ('q1', '0', 'a', 'r', 'q1'),
         ('q1', '1', 'b', 'r', 'q2'), ('q1', '0', 'a', 'r', 'q2'), ('q1', '_', '_', 'l', 'q3'),
         ('q2', '1', 'b', 'r', 'q2'), ('q2', '0', 'a', 'r', 'q2'), ('q2', '1', 'b', 'r', 'q1'),
         ('q2', '0', 'a', 'r', 'q1'), ('q2', '_', '_', 'l', 'q3'), ('q3', 'b', 'b', 'l', 'q3'),
         ('q3', 'a', 'a', 'l', 'q3'), ('q3', '1', '1', '*', 'q1'), ('q3', '0', '0', '*', 'q1'),
         ('q3', '1', '1', '*', 'q2'), ('q3', '0', '0', '*', 'q2'), ('q3', '_', '_', '*', 'halt_accept')]

# Função de chave para ordenar pelo primeiro e segundo componentes
def chave_de_ordenacao(item):
    return (item[0], item[1], item[4])

random.shuffle(tuplas)

print(tuplas)

# Ordena o vetor de tuplas usando a função de chave personalizada
tuplas_ordenadas = sorted(tuplas, key=chave_de_ordenacao)

# Imprime o resultado
print(tuplas_ordenadas)