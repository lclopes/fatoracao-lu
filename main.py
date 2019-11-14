from decomposition_LU import decompositionLU

# Os dados de entrada do programa são: n (# incógnitas), m (# sistemas), os elementos da matriz dos coeficientes dos sistemas e os elementos da matriz segundo membro dos sistemas. Estes dados deverão ser lidos de um arquivo denominado SISTEMA.

# Variáveis de controle do programa
log = ""

# Funções de controle do programa
def addLogEntry(entry):
	global log
	log = log+entry+"\n"

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

#print(A, b_list, n, m)

#caso de teste: Exercício 2 da lista de resolução de sistemas lineares
testA = [[6.0, 7.0, 4.0],
         [4.0, 4.0, 3.0],
         [2.0, 1.0, 1.0]]
    
#caso de teste: Exercício 11 da lista de resolução de sistemas lineares
testB = [3.0, 6.0, -16.0, 18.0]

testC = [[3.0, 2.0, 0.0, 1.0],
         [9.0, 8.0, -3.0, 4.0],
         [-6.0, 4.0, -8.0, 0.0],
			[3.0, -8.0, 3.0, -4.0]]

decompositionLU(testC,testB)