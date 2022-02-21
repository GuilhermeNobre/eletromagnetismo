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

map_numbers = [0,0,0,0,0,0]

def print_matrix():
    matrix_vector = np.array([ [map_numbers[0], map_numbers[1], map_numbers[2]] , 
        [map_numbers[3], map_numbers[4], map_numbers[5]]])

    print(matrix_vector)

print_matrix()

for i in range(0, len(map_numbers)):
    val_to_insert = int(input("Insira o valor posicao {}: ".format(i+1)))
    map_numbers.pop(i)
    map_numbers.insert(i, val_to_insert)
    print_matrix()

matrix_vector = np.array([ [map_numbers[0], map_numbers[1], map_numbers[2]] , 
        [map_numbers[3], map_numbers[4], map_numbers[5]]])

matrix_vect_first = [map_numbers[0], map_numbers[1], map_numbers[2]]
matrix_vect_second = [map_numbers[3], map_numbers[4], map_numbers[5]]

def calc_vector():
    result_l1 = (map_numbers[1] * map_numbers[5]) - (map_numbers[2] * map_numbers[4])
    result_l2 = (map_numbers[2] * map_numbers[3]) - (map_numbers[0] * map_numbers[5])
    result_l3 = (map_numbers[0] * map_numbers[4]) - (map_numbers[1] * map_numbers[3])

    print("O VALOR RESULTANDO: {}i {}j {}k".format(result_l1, result_l2, result_l3))
    sleep(2)
    return

calc_vector()
