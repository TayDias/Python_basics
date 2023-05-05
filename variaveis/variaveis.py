# VARIÁVEIS

texto = 'Sua idade é...'
idade = 26 # int
# idade = 26.0 # float

# Primeira forma
# print(texto + str(idade))

# Melhor forma: Fstring - interpretar o valor dentro da variável
print(f'{texto} {idade}')

# Imprimir um resultado varias vezes
print(3 * 'bom dia ')