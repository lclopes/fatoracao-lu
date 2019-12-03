from math import fabs
from matrix import newLine

# Esta função tem como objetivo realizar a fatoração LU de uma m matrizes
# quadradas de ordem n.
# Parâmetros:
#
#    m: número de sistemas
#
#    n: número de equações/variáveis 
#
#    a: matriz de coeficientes (ax = b)
#                               ^
#    b: matriz de segundo termo (ax = b) 
#                                     ^  
# A função, no momento, imprime a matriz U (matriz a após pivoteamento parcial),
# a matriz L (matriz triangular inferior criada a partir dos fatores de multiplicação
# das linhas da matriz U) e a matriz b após uma possível troca de linhas ser efetuada.

def decompositionLU(a, b_list):
    # Variáveis
    L = []      # Matriz L    
    U = a       # Matriz U
    P = 1

    # Geração da matriz L: gera uma matriz identidade de ordem n que será preenchida posteriormente
    for i in range (len(U)):
        line = newLine(len(U))
        for j in range (len(U[i])):
            if i == j:
                line[j] = 1
        L.append(line)

    for k in range(len(U) - 1):
        # Pivô começa como o primeiro elemento da primeira linha
        pivot = U[k][k]

        # Salvo a linha do pivo para realizar a operação de troca
        pivot_line = k

        for i in range(k+1, len(U)):
            # Verifico se o pivô é o maior elemento da coluna
            if fabs(U[i][k]) > fabs(pivot):
                pivot = U[i][k]
                pivot_line = i
        
        # Se o pivô for 0: saímos da iteração
        if pivot == 0:
            break
        
        # Se a linha do pivô não for a linha atual: troco as linhas
        if pivot_line != k:
            for j in range (len(U)):
                swap = U[k][j]
                U[k][j] = U[pivot_line][j]
                U[pivot_line][j] = swap
                P = P * (-1)

            # Troca os elementos da matriz de segundo termo
            for b in b_list:
                swap = b[k]
                b[k] = b[pivot_line]
                b[pivot_line] = swap

        # Realiza pivoteamento parcial              
        partialPivoting(U,k)

    # Popula matriz L
    for col in range(len(U)):
        for row in range(col+1, len(U)):
            mij = U[row][col]
            L[row][col] = mij
            U[row][col] = 0
             
    return L, U, P, b_list

# Função de pivoteamento parcial     
def partialPivoting(m, i):

    if(i != len(m)-1):
        divisor = m[i][i]

        for row in range(i+1, len(m)):
            n = m[row][i]
            for col in range(i, len(m)):
                m[row][col] -= (n / divisor) * m[i][col]
            m[row][i] = n / divisor

# Função auxiliar para arredondar os elementos da matriz m em até n casas decimais
def truncate(m,n):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j],n)
    return m            

# Função auxiliar para trocar elementos de um vetor (não usada)
def swap(m, i, j):
    aux = m[i]
    m[i] = m[j]
    m[j] = aux
    return m