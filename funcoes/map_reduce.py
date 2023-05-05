#!python3

# MAP E REDUCE

from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

# Primeiro exemplo - Procedural
# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
# print(notas)


# Segundo exemplo - Procedural
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
# 
# print(notas)


# Terceiro exemplo - Usando Map
# def exemplo_map():
#     def mais_um_meio(nota):
#         return nota + 1.5
#     
#     nf = list(map(mais_um_meio, notas))
#     print(nf)


# Quarto exemplo - Usando Map e Avaliação tardia (lazy)
def segundo_exemplo_map(delta):
    def somar_nota(delta):
        def calc(nota):
            return nota + delta
        
        return calc

    nf = list(map(somar_nota(delta), notas))
    print(nf)


# Exemplo de reduce - Somar todas as notas
def exemplo_reduce():
    def somar(a, b):
        return a+ b
    
    # função, notas, valor inicial
    print(reduce(somar, notas, 0))