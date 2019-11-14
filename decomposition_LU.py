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
    mList = []  # Agrupar fatores multiplicativos das linhas
    L = []      # Matriz L    
    U = a       # Matriz U
    p = 0       # Ponteiro para percorrimento da lista de fatores mList

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

        # Realizo operação de soma de linhas
        for i in range (k+1, len(U)):
            m = U[i][k] / U[k][k]
            U[i][k] = 0
            mList.append(m)     # Salva o fator na lista para operação posterior
            for j in range (k+1, len(U)):
                U[i][j] = U[i][j] - (m * U[k][j])
              
    # Geração da matriz L: gera uma matriz identidade de ordem n
    for i in range (len(U)):
        line = newLine(len(U))
        for j in range (len(U[i])):
            if i == j:
                line[j] = 1
        L.append(line) 

    # Adiciona os fatores da lista mList na matriz L
    while(p < len(mList)):
        for i in range(len(L)):
            for j in range(len(mList)):
                if(i > j):
                    L[i][j] = mList[p]
                    p = p+1

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

#    z = [6.0, 16.0, 2.0, (3/13)]
#    print("")
#    print("Matriz b:")
#    printM(multMat(L,z))

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
