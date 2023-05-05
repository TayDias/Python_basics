# TUPLAS

nomes = ('Ana', 'Gui', 'Tay', 'Ana') #tuple
print(type(nomes))
print(nomes)

# Verificar se elemento está presente
print('Bia' in nomes)
print('Tay' in nomes)

# Para ser considerado um tupla e não uma string - VALIDO PARA LISTAS
x = ('Teste')
y = ('Teste',)
print(f'x:{type(x)} y:{type(y)}')

# Pegar todos os elementos a partir do terceiro
print(nomes[2:])

# Pegar todos os elementos até o penultimo
print(nomes[:-1])


# Sobre tuplas:
#
# - Aceita repetições