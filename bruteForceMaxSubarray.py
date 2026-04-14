import numpy as np

def getCost(A,ini,fin):
	suma=0
	for i in range(ini,fin+1):
		suma=suma+A[i]
		#print("suma de {} a {} es = {}".format(ini,fin,suma))
	return suma


def maxSubarray(A):
	mymax=getCost(A,0,1)
	largeIni=0
	largeFin=1
	cont=0
	for i in range(0,len(A)):
		#print("i:",i)
		for j in range(i+1,len(A)):
		#	print("j:",j)
			cont=cont+1
			val=getCost(A,i,j)
			#print("cost:{} from i={} to j={}".format(val,i,j))
			if (val>mymax):
				mymax=val
				largeIni=i
				largeFin=j
	print("El valor mayor del arreglo {} es {} y se obtiene desde {} hasta {} el numero de operaciones es {}".format(A,mymax,largeIni,largeFin,cont))



#arr = np.random.randint(-50,50, size=10)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(arr)
maxSubarray(arr)