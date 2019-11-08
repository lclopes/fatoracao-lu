def partialPivoting(a,b):
    
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

                swap = b[k]
                b[k] = b[pivot_line]
                b[pivot_line] = swap
        
        #realizo operação de soma de linhas
        for i in range (k+1, len(a)):
            m = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range (k+1, len(a)):
                a[i][j] = a[i][j] - m * a[k][j]
            b[i] = b[i] - m * b[k]
    
    print(a)
    print(b)

#### TODO: Fatoração LU