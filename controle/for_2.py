# LAÇO DE REPETIÇÃO - FOR 2

# For dentro de For
pessoas = ['Tay', 'Ana', 'Vinicius']
adjetivos = ['Bonito(a)', 'Inteligente', 'Estranho(a)', 'Maluco(a)']

for p in pessoas:
    for a in adjetivos:
        print(f'{p} é {a}!')


# Usar pass para deixar um laço vazio (sem codigo)
for i in [1,2,3]:
    pass


# Usar continue para pular o código e continuar o laço
for i in range(1, 11):
    if i % 2: # impar
        continue
    print(i, end=' ')

print('')

# Usar o comando break para interromper o laço
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')

print('Fim!')