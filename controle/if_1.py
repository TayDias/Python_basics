# CONDICIONAIS - 1

nota = float(input('Informe a nota do aluno: '))

if nota >= 9:
    print('Parabéns!\nQuadro de Honra')

elif nota >= 7:
    print('Aprovado')

elif nota >= 3.5:
    print('Recuperação')

else:
    print('Reprovado')

print(nota)