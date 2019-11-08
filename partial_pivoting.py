# Esta função tem como objetivo realizar o pivoteamento parcial de uma matriz
# quadrada de ordem n.
# Parâmetros:
#    a: matriz de coeficientes (ax + b)
#                               ^
#    b: matriz de segundo membro (ax + b)
#                                      ^ 
# A função retorna a matriz 'a' após a operação de pivoteamento parcial.
def partialPivoting(a):

    for k in range(len(a) - 1):
        #pivô começa como o primeiro elemento da primeira linha
        pivot = a[k][k]

        #salvo a linha do pivo para realizar a operação de troca
        pivot_line = k

        for i in range(k+1, len(a)):
            #verifico se o pivô é o maior elemento da coluna
            if a[i][k] > pivot:
                pivot = a[i][k]
                pivot_line = i
        
        #se o pivô for 0: saímos da iteração
        if pivot == 0:
            break
        else:

            #se a linha do pivô não for a linha atual: troco as linhas
            if pivot_line != k:
                for j in range (len(a)):
                    swap = a[k][j]
                    a[k][j] = a[pivot_line][j]
                    a[pivot_line][j] = swap
        
        #realizo operação de soma de linhas
        for i in range (k+1, len(a)):
            m = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range (k+1, len(a)):
                a[i][j] = a[i][j] - m * a[k][j]
    
    return a