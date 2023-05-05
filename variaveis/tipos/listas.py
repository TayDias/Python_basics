# LISTAS

nums = [1,2,3]
print(type(nums)) #list

# Add elemento na lista
nums.append(3)

# Ver o tamanho da lista
print(len(nums))

# Verificar se elemento está presente
print(2 in nums)

# Alterar o valor de um índice
nums[3] = 4

# Fazer um insert e deslocar o resto
nums.insert(0, 200)

# Acessar o ultimo elemento
print(nums[-1])

# Acessar o penultimo elemento
print(nums[-2])

# Acessar de um elemento até outro
print(nums[1:3])

print(nums)


# Sobre listas:
#
# - Aceita repetições
# - Aceita alterações