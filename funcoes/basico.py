# FUNÇÕES BÁSICAS

# Sintaxe
def nada():
    pass


# Com conteúdo
def saudacao():
    print('Bom dia!')


# Com parâmetros
def saudacao_nome(nome):
    print(f'Bom dia {nome}!')


# Parametro com valor padrão
def saudacao_alternativa(nome = 'Pessoa'):
    print(f'Bom dia {nome}!')


# Com retorno
def soma_e_multiplicacao(a, b, x):
    return (a + b) * x


# Obs: Python não tem sobrecarga, uma função com mesmo nome é diferenciada na chamada pelos parametros