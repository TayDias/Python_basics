# ARGUMENTOS

def soma(*nums):
    print(type(nums))
    total = 0
    for n in nums:
        total += n
    return total


def resultadoFinal(**kwargs):
    print(type(kwargs))
    status = 'aprovado(a)' if kwargs['nota'] >=7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}.'



# kwargs = key words args (argumantos nomeados)