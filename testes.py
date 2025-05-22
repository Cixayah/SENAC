# EXERCÍCIO 1: Soma de 1 a 100
# Calcule a soma de todos os números de 1 até 100

sum_total = 0
for i in range(1, 101):
    sum_total += i
print("Exercício 1 - Soma de 1 a 100:", sum_total)


# EXERCÍCIO 2: Par ou ímpar
# Peça um número e diga se ele é par ou ímpar

number = int(input("\nExercício 2 - Digite um número: "))
if number % 2 == 0:
    print("É par")
else:
    print("É ímpar")


# EXERCÍCIO 3: Tabuada
# Peça um número e mostre a tabuada dele de 1 a 10

table_number = int(input("\nExercício 3 - Tabuada de qual número? "))
print(f"Tabuada do {table_number}:")
for i in range(1, 11):
    print(f"{table_number} x {i} = {table_number * i}")


# EXERCÍCIO 4: Contar vogais
# Peça uma frase e conte quantas vogais ela tem

sentence = input("\nExercício 4 - Digite uma frase: ").lower()
vowels = "aeiou"
vowel_count = 0
for letter in sentence:
    if letter in vowels:
        vowel_count += 1
print("Quantidade de vogais:", vowel_count)


# EXERCÍCIO 5: Palíndromo
# Verifique se uma palavra é igual quando lida ao contrário

word = input("\nExercício 5 - Digite uma palavra: ").lower()
if word == word[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


# EXERCÍCIO 6: Fatorial
# Calcule o fatorial de um número (ex: 5! = 120)

factorial_number = int(input("\nExercício 6 - Digite um número para ver o fatorial: "))
factorial_result = 1
for i in range(1, factorial_number + 1):
    factorial_result *= i
print(f"Fatorial de {factorial_number} é {factorial_result}")


# EXERCÍCIO 7: Números primos até 50
# Mostre todos os números primos entre 1 e 50

print("\nExercício 7 - Números primos de 1 a 50:")
for prime_candidate in range(2, 51):
    is_prime = True
    for i in range(2, int(prime_candidate**0.5) + 1):
        if prime_candidate % i == 0:
            is_prime = False
            break
    if is_prime:
        print(prime_candidate, end=" ")
print()


# EXERCÍCIO 8: Média de notas
# Peça 3 notas e calcule a média

grade1 = float(input("\nExercício 8 - Nota 1: "))
grade2 = float(input("Nota 2: "))
grade3 = float(input("Nota 3: "))
average = (grade1 + grade2 + grade3) / 3
print(f"Média: {average:.2f}")


# EXERCÍCIO 9: Contagem regressiva
# Mostre uma contagem regressiva de 10 até 0

print("\nExercício 9 - Contagem regressiva:")
for i in range(10, -1, -1):
    print(i)


# EXERCÍCIO 10: Soma de números positivos
# Peça 5 números e some apenas os positivos

positive_sum = 0
print("\nExercício 10 - Digite 5 números:")
for i in range(5):
    value = float(input(f"Número {i+1}: "))
    if value > 0:
        positive_sum += value
print("Soma dos positivos:", positive_sum)
