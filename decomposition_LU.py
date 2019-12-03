from math import fabs

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

def decompositionLU(a,b):
    # Variáveis
    L = []      # Matriz L    
    U = a       # Matriz U

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

            # Troca os elementos da matriz de segundo termo
            swap = b[k]
            b[k] = b[pivot_line]
            b[pivot_line] = swap

        # Realiza pivoteamento parcial              
        partialPivoting(U,k)

    # Gera a matriz L (MODIFICAR)
    for coluna in range(0, len(U)):
        for linha in range(coluna+1, len(U)):
            L[linha][coluna] = U[linha][coluna] # Matriz L
            U[linha][coluna] = 0     

    # return U, L, b, permut, cont           
    # Resultados
    print("Matriz L:") 
    L = truncate(L,2)
    printM(L) 
    print("") 
    print("Matriz U:")        
    U = truncate(U,2)
    printM(U)
    print("") 
    print("Matriz b:")
    print(b)

# Função para multiplicar duas matrizes
def multiplyM(a, b):
    n = len(a[0])
    rows = len(a)
    cols = len(b[0])
    c = []
    for i in range(rows):
        c.append(newLine(cols))
        for j in range(cols):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c

# Função para realizar pivoteamento parcial (MODIFICAR)        
def partialPivoting(matriz, i):
    N = len(matriz)  # Ordem da Matriz

    if(i != len(matriz)-1):
        den = matriz[i][i]

        for linha in range(i+1, N):
            num = matriz[linha][i]

            for coluna in range(i, N):
                matriz[linha][coluna] -= (num / den) * matriz[i][coluna]

            # Constrói a matriz L
            matriz[linha][i] = num / den

    
# Função auxiliar para geração de uma lista de zeros de tamamho N
def newLine(n):
    line = []
    for i in range(n):
        line.append(0)
    return line    

# Função auxiliar para imprimir a matriz de forma mais legível
def printM(m):
    for i in range(len(m)):
        print(m[i])

# Função auxiliar para arredondar os elementos da matriz m em até n casas decimais
def truncate(m,n):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j],n)
    return m            

# Função auxiliar para trocar elementos de um vetor
def swap(m, i, j):
    aux = m[i]
    m[i] = m[j]
    m[j] = aux
    return m