# Inputs e verificações simples

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

num1 = input('Digite um numero inteiro: ')
hora = input('Digite a hora neste momentos [00.00]: ')
nome = input('Digite seu primeiro nome: ')

if is_int(num1):
    if (int(num1) % 2) == 0:
        print(f"{num1} é par!")
    else:
        print(f"{num1} é impar!")
else:
    print('O valor digitado não é um número inteiro')

if is_float(hora):
    if (float(hora) >= 0 and float(hora) < 12):
        print('Bom dia!')
    elif (float(hora) >= 12 and float(hora) < 18):
        print('Boa tarde!')
    elif (float(hora) >= 18 and float(hora) < 24):
        print('Boa noite!')
    else:
        print('Horário inválido')
else:
    print('Valor de horário digitado inválido')

if len(nome) > 0 and len(nome) <= 4:
    print('Seu nome é muito curto!')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome tem um tamanho normal!')
elif len(nome) > 6:
    print('Seu nome é grande!')
else:
    print('Você não digitou seu nome!')
