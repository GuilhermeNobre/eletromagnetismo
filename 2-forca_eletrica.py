"""
Author: Guilherme Guimarães Dantas 
Data: 20/02/2022

Email: guinobre1602@gmail.com

Donate? 

Bitcoin: bc1qkzddvlt26mzj30wrvlzlf0474krefnu4surmwu
"""

import numpy as np
from numpy import cross
from time import sleep
from math import pow

from streamlit import stop

map_numbers = [0,0,0,0,0,0]
expoents_num = [0,0,0,0,0,0]

print("CALCULO DO FORÇA MAGNETICA\n")
sleep(1.5)

def print_tutorial():
    print("INSIRA O VALOR DOS PRODUTOS VETORIAIS\n")
    print("SEGUINDO A FÓRMULA Fm = q * v * B\n")
    sleep(2.0)
    print("AONDE")
    print("Fm - Forca Magnetica (N - Newton)")
    sleep(1.0)
    print("q - Carga eletrica (C - Columb)")
    sleep(1.0)
    print("v - Velocidade da particula (m/s - metros por segundo)")
    sleep(1.0)
    print("B - Campo Magnetico (T - Tesla)\n")
    sleep(1.0)
    print("Vamos começar o valor carga eletrica")
    sleep(2.0)
    print("Qual o  valor da carga eletrica?")
    sleep(0.1)

answer = int(input("Deseja saber como funciona o cálculo?\n1- Sim\n2- Não\nResposta: "))
if(answer == 1):
    print_tutorial()

charge_q = [0,0]

print("\nInsira o valor da carga eletrica da seguinte forma \"X Y\"\n")
sleep(0.5)
print("Onde X é indice (1~10)")
sleep(2)
print("Onde Y é expoente (VALOR INTEIRO)")
sleep(2)
charge_q[0], charge_q[1] = input("\nQual valor da carga: ").split()

calculate_charge = float(charge_q[0])
expo_q = float(charge_q[1])

def print_matrix():
    matrix_vector = np.array([ [map_numbers[0], map_numbers[1], map_numbers[2]] , 
        [map_numbers[3], map_numbers[4], map_numbers[5]]])

    # print(matrix_vector)

# print_matrix()

# for i in range(0, len(map_numbers)):
#     val_to_insert = int(input("Insira os valores das componentes x,y e z do vetor A  {}: ".format(i+1)))
#     map_numbers.pop(i)
#     map_numbers.insert(i, val_to_insert)
#     print_matrix()

print("Insira os valores da velocidade de particula na seguinte forma \"X i\" \"Y j\" \"Z k\"\n")
sleep(0.5)
print("Exemplo uma particula 10^12 2^-12 5^7\nSeria 10 12 2 -12 5 7\no mesmo vale para o campo magnetico")
sleep(4)



map_numbers[0], expoents_num[0],

map_numbers[0], expoents_num[0], map_numbers[1], expoents_num[1], map_numbers[2], expoents_num[2] = input("\nInsira os valores das velocidade de particula: ").split()
map_numbers[3], expoents_num[3], map_numbers[4], expoents_num[4], map_numbers[5], expoents_num[5] = input("Insira os valores das campo magnetico: ").split()

for i in range(0, len(map_numbers)):
    map_numbers[i] = int(map_numbers[i])

print_matrix()

matrix_vector = np.array([ [map_numbers[0], map_numbers[1], map_numbers[2]] , 
        [map_numbers[3], map_numbers[4], map_numbers[5]]])

matrix_vect_first = [map_numbers[0], map_numbers[1], map_numbers[2]]
matrix_vect_second = [map_numbers[3], map_numbers[4], map_numbers[5]]

def calc_vector():
    result_l1 = (map_numbers[1] * map_numbers[5]) - (map_numbers[2] * map_numbers[4]) * int(charge_q[0])
    result_l2 = (map_numbers[2] * map_numbers[3]) - (map_numbers[0] * map_numbers[5]) * int(charge_q[0])
    result_l3 = (map_numbers[0] * map_numbers[4]) - (map_numbers[1] * map_numbers[3]) * int(charge_q[0]) 

    #Expontes
    result_e1 = int(expoents_num[0]) + int(expoents_num[3]) + int(expo_q)
    result_e2 = int(expoents_num[1]) + int(expoents_num[4]) + int(expo_q)
    result_e3 = int(expoents_num[2]) + int(expoents_num[5]) + int(expo_q)

    print("\nO VALOR RESULTANDO DA FORCA: {}i*10^{} {}j*10^{} {}k*10^{}".format(result_l1, result_e1, result_l2, result_e2, result_l3, result_e3))
    sleep(2)
    return

calc_vector()