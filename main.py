from random import getrandbits
from math import pi, pow, ceil
from math import sqrt
from mpi4py import MPI
import time 


'''
cromossomo -> (x,y) - estado (ativo, nao ativo) - raio - sobreposicao - populacao -  radiacao de energia
considerar area de ddos = 4000 km -> lado 64 
0,7,14,15,23,31,39,47
'''																			
AREA = 4000 # aproximadamente area de dourados em km^2
RADIUS = 100

#antena de telefonia movel ERB

class pop():
	def __init__(self):
		self.SIZE_POP = 500
		self.lenght_gene = 55
		self.dbi = 255

	def init_n_pop(self):
		POP_1 = self.init_pop()
		POP_2 = self.init_pop()
		POP_3 = self.init_pop()
		POP_4 = self.init_pop()

		print("Tam da população 1, 2, 3 e 4 :", len(POP_1), len(POP_2), len(POP_3), len(POP_4))

		cont = 0
		for item in (POP_4):
			a = item[14]
			if(a == 1):
				cont += 1

	
		for item in (POP_4):
			self.calc_fitness(item)
	

	def init_individual(self):
		llist_indi = []
		for i in range(1, self.lenght_gene):
			pos = getrandbits(1) # pares entre 0 e 9
			llist_indi.append(pos)

		return llist_indi

	def init_pop(self):
		#individuo 1 da pop é usado para criar o primeiro modelo de probabilidade
		list_pop = []
		for i in range(0, self.SIZE_POP):
			baby = self.init_individual()
			list_pop.append(baby)

		return list_pop

	def create_model(self):
		#M[i] = (1 - alfa) * Xi + alfa * (average half best individuals)
		pass
		#for individual in range (2, N):
			#if max(Probn(Indi | M(k)), k=1 .... Ni) < Fc

	def calc_hamming(self):
		#Probn = (A * 100) \ (T)
		pass

	'''
	calcular -> soma da area total da antena
			-> soma da area de sobreposição da antena 
			-> qtd de antenas ativas
	'''
	def calc_fitness(self, individuo):
		xradius = []
		for i in range(15 ,22):
			xradius.append(individuo[i])

		area_coverage = self.area_hexa(self.convert_binary(xradius))

		radian = []
		for i in range(47, 54):
			radian.append(individuo[i])

		P_tot = self.convert_binary(radian)
		P_max = 255
		sobre = 1.0
		n_sbr = 1.0
		
		F_fit = (AREA - ( area_coverage / AREA ) ) + (sobre / AREA) + (P_tot / (n_sbr * P_max) )
		print(F_fit)


	def point_space(self, individuo):
		x = []
		for i in range(0 ,6):
			x.append(individuo[i])
		a = self.convert_binary(x)

		y = []
		for i in range(7 ,13):
			y.append(individuo[i])
		b = self.convert_binary(y)
		ponto = a,b
		return ponto

	def convert_binary(self, binary):
		str1 = ''.join(str(x) for x in binary)
		n = int(str1, 2)
		return n

	def conv_radius_area(self):
		area = pi * pow(RADIUS, 2)
		return (area/1000) #retorna area em km

	def ERB_min(self, coverage):
		erb_min = ceil(AREA / coverage)
		return erb_min

	def area_intersec(self, individuo1, individuo2):
		radius_1 = []
		for i in range(15 ,22):
			radius_1.append(individuo1[i])

		radius_2 = []
		for i in range(15 ,22):
			radius_2.append(individuo2[i])

		if (radius_1 > radius_2):
			area = pi * pow(radius_2, 2)

		if (radius_2 > radius_1):
			area = pi * pow(radius_1, 2)

		if (radius_1 == radius_2):
			x = ((2 * pi * pow(radius_1, 2)) / 3) - ((sqrt(3) * pow(radius_1, 2)) / 2)

		print("area:", x/1000)
		return x
# area do hexagono é igual a area de 6 triangulos equilateros  com lado igual a raio
	def area_hexa(self, radius):
		area = (3 * pow(radius,2) * sqrt(3) ) / 2
		return area



class slayer():
	def __init__(self):
		pass
		


def conv():
	n=int(input('numero decimal: '))
	x=n
	k=[]

	while (n>0):
		a = int(float(n%2))
		k.append(a)
		n=(n-a)/2

	#k.append(0)
	string=""

	for j in k[::-1]:
		string=string+str(j)

	print('The binary no. for %d is %s'%(x, string))


def main():

	ini = time.time()
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	#random.seed() #inicia a semente dos número pseudo randômicos

	if rank == 0:
		obj = pop()
		obj.init_n_pop()
		fim = time.time()

		print("time", fim - ini);

       


if __name__ == '__main__':
	main()
