# LAÇO DE REPETIÇÃO - WHILE

# Exemplo 1 - Laço com decréscimo
x = 10

while x:
    print(x)
    x -= 1

print('Fim')


# Exemplo 2 - Quantidade indeterminada de repetições
total = 0
nota = 0 
qtde = 0

while nota != -1:
     nota = float(input('Informe a nota ou -1 para sair: '))
     if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é {total / qtde}')
