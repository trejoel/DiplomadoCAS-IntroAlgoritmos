import numpy as np


def searchElement(L,X):
	for i in range(len(L)):
		if L[i]==int(X):
			return i
	return -1


arr = np.random.randint(20, size=10)
print("Arreglo:",arr) 
y=input("Que numero quiere buscar:")
x=searchElement(arr,y)
if x>=0:
	print("Elemento ",y,  " encontrado en la posicion:",x)
else:
	print("El elemento ",y, " no se encuentra")
