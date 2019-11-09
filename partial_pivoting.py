# Esta função tem como objetivo realizar o pivoteamento parcial de uma matriz
# quadrada de ordem n.
# Parâmetros:
#    a: matriz de coeficientes (ax + b)
#                               ^
#    b: matriz de segundo membro (ax + b)
#                                      ^ 
# A função retorna a matriz 'a' após a operação de pivoteamento parcial.
def partialPivoting(a):
    mList = []
    L = []
    U = a

    for k in range(len(U) - 1):
        #pivô começa como o primeiro elemento da primeira linha
        pivot = U[k][k]

        #salvo a linha do pivo para realizar a operação de troca
        pivot_line = k

        for i in range(k+1, len(U)):
            #verifico se o pivô é o maior elemento da coluna
            if U[i][k] > pivot:
                pivot = U[i][k]
                pivot_line = i
        
        #se o pivô for 0: saímos da iteração
        if pivot == 0:
            break
        else:

            #se a linha do pivô não for a linha atual: troco as linhas
            if pivot_line != k:
                for j in range (len(U)):
                    swap = U[k][j]
                    U[k][j] = U[pivot_line][j]
                    U[pivot_line][j] = swap
        
        #realizo operação de soma de linhas
        for i in range (k+1, len(U)):
            m = U[i][k] / U[k][k]
            U[i][k] = 0
            mList.append(m)
            for j in range (k+1, len(U)):
                U[i][j] = U[i][j] - m * U[k][j]
                
    #geração da matriz L
    for i in range (len(U)):
        linha = newLine(len(U))
        for j in range (len(U[i])):
            if i == j:
                linha[j] = 1
            elif i < j:
                linha[j] = 0
            else:
                linha[j] = mList[j]
        L.append(linha) 
    
    print(mList)
    print(U) 
    print(L) 

def newLine(n):
    line = []
    for i in range(n):
        line.append(0)
    return line    