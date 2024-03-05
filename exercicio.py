# Exercício 1
'''soma = 0
k = 0
for num in range(0, 13):
    k = k+1
    soma = soma+k

print(soma)'''

# Exercício 2
'''n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else:
    count = 0
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1

        if (n != termo):
            continue
        if (n == termo):
            print('Número pertence à sequência de Fibonacci')
            break
    print('Número não pertence à sequência de Fibonacci')'''

# Exercício 3
''' a) 9,11,13...
    b) 128,254,528...
    c) 49,64,81...
    d) 100,144,196...
    e) 13,21,34...
    f) 20,21,22...
    
Exercício 4
Ligo o primeiro interruptor, entro na segunda sala, logo se não ligar a lâmpada
da primeira e nem da segunda sala, a lâmpada acendeu na terceira, depois volto na
primeira sala e ligo o segundo interruptor, assim saberei se a lâmpada acender na primeira
sala ou na segunda sala


#Exercício 5
nome = "Fabricio de Lima"
nome_invertido = nome[::-1]
print(nome_invertido)'''
