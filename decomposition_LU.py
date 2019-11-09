from math import fabs

# Esta função tem como objetivo realizar a fatoração LU de uma matriz
# quadrada de ordem n.
# Parâmetros:
#    a: matriz de coeficientes (ax + b)
#   
# A função, no momento, imprime a matriz U (matriz a após pivoteamento parcial)
# e a matriz L (matriz triangular inferior criada a partir dos fatores de multiplicação
# das linhas da matriz U).
def decompositionLU(a):
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
            elif i < j:
                line[j] = 0
        L.append(line) 

    #adiciona os fatores da lista mList na matriz L
    while(p < len(mList)):
        for i in range(len(L)):
            for j in range(len(mList)):
                if(i > j):
                    L[i][j] = mList[p]
                    p = p+1
    
    print("Matriz L:") 
    L = truncate(L)
    printM(L) 
    print("") 
    print("Matriz U:")        
    U = truncate(U)
    printM(U) 


###########FUNÇÕES AUXILIARES############
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

def truncate(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j],2)
    return m            
