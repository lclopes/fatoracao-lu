from decomposition_LU import decompositionLU
from matrix import *
# Os dados de entrada do programa são: n (# incógnitas), m (# sistemas), os elementos da matriz dos coeficientes dos sistemas e os elementos da matriz segundo membro dos sistemas. Estes dados deverão ser lidos de um arquivo denominado SISTEMA.

# Variáveis de controle do programa
log = ""

# Funções de controle do programa
def addLogEntry(entry):
	global log
	log = log+entry+"\n"
    
def logMatrix(m):
    global log
    log = log + "["
    for i in range(len(m)):
        for j in range(len(m[0])):
            log = log + str(m[i][j])
            if j<len(m[0])-1:
                log = log + "\t"
        if i<len(m)-1:
            log = log + "\n"
    log = log + "]\n"

def saveLog(filename):
	f = open(filename, "w")
	global log
	f.write(log)
	f.close()
	print("Log foi salvo.")

# Lê arquivo de entrada
f = open("SISTEMA", "r")
lines = f.readlines()
f.close()

# Variáveis matemáticas
n, m = map(int, lines[0].split())
A = []
b_list = []

for i in range(2, n+2):
	row = list(map(int, lines[i].split()))
	A.append(row)

for i in range(n+3, n+3+m):
    b = list(map(int, lines[i].split()))
    b_list.append(b)
    
#print(A, b, n, m)

L, U, P, b_list = decompositionLU(A, b_list)

print("\nMatriz L:")
printM(L)
print("\nMatriz U:")
printM(U)

# Log
addLogEntry("\nMatriz L:")
logMatrix(L)
addLogEntry("\nMatriz U:")
logMatrix(U)

detA = detTriang(L) * detTriang(U) * P

print("\ndet(A) = "+str(detA))
addLogEntry("\ndet(A) = "+str(detA)) # Log

inv = invLU(L, U, b[0])
print("\nInversa da matriz A:")
printM(inv)

# Log
addLogEntry("\nInversa da matriz A:")
logMatrix(inv)

for b in b_list:
    
    print("\nSolucao (aproximada) para b = " + str(b))
    addLogEntry("\nSolucao (aproximada) para b = " + str(b)) # Log

    y = forw(L, b)
#    print(y)
    x = back(U, y)
    print("S = "+str(x))
    addLogEntry("S = "+str(x))
    
saveLog("RESUL")