# EXERCÍCIO 1: Soma de 1 a 100
# Calcule a soma de todos os números de 1 até 100

soma = 0
for i in range(1, 101):
    soma += i
print("Exercício 1 - Soma de 1 a 100:", soma)


# EXERCÍCIO 2: Par ou ímpar
# Peça um número e diga se ele é par ou ímpar

num = int(input("\nExercício 2 - Digite um número: "))
if num % 2 == 0:
    print("É par")
else:
    print("É ímpar")


# EXERCÍCIO 3: Tabuada
# Peça um número e mostre a tabuada dele de 1 a 10

num_tabuada = int(input("\nExercício 3 - Tabuada de qual número? "))
print(f"Tabuada do {num_tabuada}:")
for i in range(1, 11):
    print(f"{num_tabuada} x {i} = {num_tabuada * i}")


# EXERCÍCIO 4: Contar vogais
# Peça uma frase e conte quantas vogais ela tem

frase = input("\nExercício 4 - Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
print("Quantidade de vogais:", contador)


# EXERCÍCIO 5: Palíndromo
# Verifique se uma palavra é igual quando lida ao contrário

palavra = input("\nExercício 5 - Digite uma palavra: ").lower()
if palavra == palavra[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


# EXERCÍCIO 6: Fatorial
# Calcule o fatorial de um número (ex: 5! = 120)

n = int(input("\nExercício 6 - Digite um número para ver o fatorial: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"Fatorial de {n} é {fatorial}")


# EXERCÍCIO 7: Números primos até 50
# Mostre todos os números primos entre 1 e 50

print("\nExercício 7 - Números primos de 1 a 50:")
for num in range(2, 51):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=" ")
print()


# EXERCÍCIO 8: Média de notas
# Peça 3 notas e calcule a média

n1 = float(input("\nExercício 8 - Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")


# EXERCÍCIO 9: Contagem regressiva
# Mostre uma contagem regressiva de 10 até 0

print("\nExercício 9 - Contagem regressiva:")
for i in range(10, -1, -1):
    print(i)


# EXERCÍCIO 10: Soma de números positivos
# Peça 5 números e some apenas os positivos

soma_positivos = 0
print("\nExercício 10 - Digite 5 números:")
for i in range(5):
    n = float(input(f"Número {i+1}: "))
    if n > 0:
        soma_positivos += n
print("Soma dos positivos:", soma_positivos)
