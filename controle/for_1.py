# LAÇO DE REPETIÇÃO - FOR

# Quantidade fixa de repetições
for i in range(10):
    print(i)

print('')

# Mais a definição de início e fim
for i in range(1, 11):
    print(i)

print('')

# Mais a definição do tamanho do intervado (passo)
for i in range(1, 100, 7):
    print(i)

print('')

# Com o passo decrescente
for i in range(20, 0, -3):
    print(i)

print('')

# Percorrer lista de números
nums = [2, 4, 6, 8]

for n in nums:
    print(n)

print('')

# Mostrar todos os numeros em uma linha só
for n in nums:
    print(n, end=' ')

print('')

# Percorrer uma string
texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end=' ')

print('')

# Percorrer um 'set'
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')

print('')

# Percorrer um dicionário
produto = {
    'nome': 'Caneta',
    'preco': 8.80
}

print('')

# Percorrer os itens
for atributo in produto:
    print(atributo, ' - ', produto[atributo])

print('')

# Percorrer os itens - variação
for atributo, valor in produto.items():
    print(atributo, ' - ', valor)

print('')

# Percorrer somente os valores
for valor in produto.values():
    print(valor, end=' ')

print('\n')

# Percorrer somente as chaves
for atributo in produto.keys():
    print(atributo, end=', ')