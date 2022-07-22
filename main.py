### Autor: Weslley Borges dos Santos
### Data de criação: 08/06/2022
### Última atualização: 17/07/2022
###
### Criar um sistema de programação de modo que resolva
### sistemas de equações lineares 3 X 3 através do método do escalonamento
### de matrizes, através de uma linguagem de programação escolhida por
### vocês.

import copy

# Separa os coeficientes da equação ao 
# percorrer e verificar todos os caracteres.
def parse_coefficients(equation):
    coefficients = []
    past_character = ''
    last_number = None

    for i in equation:
        if i == '=': break

        if str.isnumeric(i):
            if past_character == '-':
                coefficients.append(int(past_character+i))
                last_number = int(past_character+i)
            elif str.isnumeric(past_character):
                coefficients[coefficients.index(last_number)] =  int(str(last_number) + i)
                last_number = int(str(last_number) + i)
            else:
                coefficients.append(int(i))
                last_number= int(i)

        elif i in ['x','y', 'z'] and str.isnumeric(past_character) is False:
            if past_character in ['-','+']:
                coefficients.append(int(past_character+'1'))
            else:
                coefficients.append(1)

        past_character = i
    return coefficients


# Altera os valores de uma coluna
def replace_values(matrix, substitute, column):
    replaced = matrix

    i = 0
    while i < len(matrix):
        replaced[i][column] = substitute[i]
        i += 1
    return replaced
    

def print_matrix(matrix, result):
    for i in matrix: 
        print('\t'.join(map(str, i)))
    print(result,"\n")


# Descobre a determinante de uma matrix
def sarrus_law(matrix):
    for i in matrix:
        i.append(i[0])
        i.append(i[1])
    
    # Multiplica os os elementos da matrix 
    # nas diagonais principal e secundária e soma seus produtos
    i , j = 0, 0
    primary_diagonals, secondary_diagonals = 0, 0

    while j < len(matrix[0]):
        def calculate_diagonals(signal):
            diagonal_products = matrix[i][j]
            
            for euclidian_distance in range(1, len(matrix)):
                diagonal_products *= matrix[i+euclidian_distance][j + (euclidian_distance*signal)]
            return diagonal_products

        if j <= 2: # Coluna 0 - 2 
            primary_diagonals += calculate_diagonals(1)
        if j >= 2: # Coluna 2 - 4
            secondary_diagonals += calculate_diagonals(-1)
            
        j+=1

    return primary_diagonals - secondary_diagonals


# Descobre os valores de x, y e z no sistema
def cramer_rule(matrix, equations_results):
    D = sarrus_law(copy.deepcopy(matrix))
    
    matrix_replaced_X = replace_values(copy.deepcopy(matrix), equations_results, 0)
    matrix_replaced_Y = replace_values(copy.deepcopy(matrix), equations_results, 1)
    matrix_replaced_Z = replace_values(copy.deepcopy(matrix), equations_results, 2)

    Dx = sarrus_law(matrix_replaced_X)
    Dy = sarrus_law(matrix_replaced_Y)
    Dz = sarrus_law(matrix_replaced_Z)

    x = Dx/D
    y = Dy/D
    z = Dz/D

    print_matrix(matrix_replaced_X, "Dx = "+str(Dx))
    print_matrix(matrix_replaced_Y, "Dy = "+str(Dy))
    print_matrix(matrix_replaced_Z, "Dz = "+str(Dz))
    print("S = {(",x,", ",y,", ",z,")}")


# 1. Extrair os coeficientes e colocá-los em uma matriz 3x3
# 2. Aplicar a Regra de Sarrus para descobrir D, Dx, Dy e Dz
# 3. Aplicar as fórmulas da Regra de Cramer para descobrir o valor de x, y e z.
def start(test):
    if test:
        linear_systems = [["2x+2y-z=3","3x+3y+z=7", "x-y+5z=5"], ["5x+2y+z=-12","-x+4y+2z=20", "2x-3y+10z=3"]]
        
        for system in linear_systems:
            matrix = []
            equations_results = []

            for equation in system:
                matrix.append(parse_coefficients(equation))
                equations_results.append(int(equation.split('=')[1]))
                print("| "+equation)
            print("\n")
            cramer_rule(copy.deepcopy(matrix), equations_results)  
            print("---------------------------\n\n")       

    else:
        matrix = []
        equations_results = []

        for count in range(3):
            equation = str(input(""+str(count+1)+"ª equação (Ex.: x+2y+z=0): ")).lower()
            matrix.append(parse_coefficients(equation))
            equations_results.append(int(equation.split('=')[1]))
        print('\n')
        cramer_rule(copy.deepcopy(matrix), equations_results)

start(True)
start(False)
