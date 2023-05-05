# PROGRAMAÇÃO FUNCIONAL

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


# Armazenamento da função dentro de uma variavel qualquer
somar = soma


# Funções que possuem funções
def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


# Funções que retornam outra função - Avaliação Tardia (lazy)
def soma_parcial(a):
    # exemplo: processamento 60 segundos
    def concluir_soma(b):
        # exemplo: processamento 10 segundos
        return a + b
    return concluir_soma


# Exemplo de medição de tempo de execução
#
# r1 = soma (10, 12) = 1m 10s de demora
# r2 = soma (10, 20) = 1m 10s de demora
# r2 = soma (10, 50) = 1m 10s de demora
#
# Total = 3m 30s

soma_1 = soma_parcial(1) # 1m
r1 = soma_1(12) # 10s
r2 = soma_1(20) # 10s
r3 = soma_1(50) # 10s

# Total = 1m 30s (2m a menos)