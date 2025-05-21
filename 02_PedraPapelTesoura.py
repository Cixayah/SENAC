from os import system, name
import random

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def gg():
    option = 'S'
    while option.upper() == 'S':
        clear_screen()
        
        cpu = random.randint(0, 2)
        try:
            player = int(input('''Escolha uma opção para jogar: 
[1] Pedra
[2] Papel
[3] Tesoura
Digite sua escolha: ''')) - 1
            if player not in [0, 1, 2]:
                print("Escolha inválida. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue
        
        opt_choices = ('Pedra', 'Papel', 'Tesoura')
        table = (
            ('NINGUÉM', 'JOGADOR', 'CPU'),
            ('CPU', 'NINGUÉM', 'JOGADOR'),
            ('JOGADOR', 'CPU', 'NINGUÉM')
        )
        
        print(f'Você escolheu {opt_choices[player]}')
        print(f'A CPU escolheu {opt_choices[cpu]}')
        print(f'{table[cpu][player]} GANHOU!!!')
        
        option = input('Jogar novamente? Aperte (S) para sim: ')

if __name__ == "__main__":
    gg()
