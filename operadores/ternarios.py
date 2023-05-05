# OPERADORES TERNÁRIOS

lockdown = True

status = 'Em casa' if lockdown else 'Pode sair'
print(status)

lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <=100 else 'Pode sair'
print(status)

grana = 200

status = 'Em casa' if lockdown or grana <=100 else 'Pode sair'
print(status)

# Sobre operadores ternários:
#
# - Opera com mais de dois operandos
# - O resultado é sempre True ou False