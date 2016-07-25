from random import getrandbits
from math import pi, pow, ceil
from math import sqrt
from mpi4py import MPI
import time 


'''
cromossomo -> (x,y) - estado (ativo, nao ativo) - raio  - populacao -  radiacao de energia - sobreposicao
considerar area de ddos = 4000 km -> lado 64 
0,7,14,15,23,31,39,47
'''																			
AREA = 4000 # aproximadamente area de dourados em km^2
RADIUS = 100

#antena de telefonia movel ERB

class mestre():
	def __init__(self):
		pass



class pop():
	def __init__(self):
		self.SIZE_POP = 500
		self.lenght_gene = 55
		self.dbi = 255

	def init_n_pop(self):
		POP_1 = self.aux_init_pop()
		POP_2 = self.init_pop()
		POP_3 = self.init_pop()
		POP_4 = self.init_pop()

		cont = 0
		for item in (POP_4):
			a = item[14]
			if(a == 1):
				cont += 1

		for item in (POP_4):
			calc_fitness(item)
	
	def aux_init_pop(self):
		POP = self.init_pop()
		self.checaColisao(POP)

		return POP

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
			if (baby in list_pop):
				while (baby in list_pop):
					baby = self.init_individual()
			else:
				list_pop.append(baby)

		return list_pop


	def checaColisao(self, populacao):
		for erb in populacao:
 			p1 = point_space(erb)
 			x1, y1 = p1
 			radius_1 = []

 			for i in range(15,22):
 				radius_1.append(erb[i])

 			for others_erb in populacao:
 				p2 = point_space(others_erb)
 				x2, y2 = p2
 				cateto1 = x2 - x1
 				cateto2 = y2 - y1
 				distancia = sqrt( pow(cateto1, 2) + pow(cateto2, 2) )
 				radius_2 = []
 				for k in range(15, 22):
 					radius_2.append(others_erb[k])

 				raio1 = convert_binary(radius_1)
 				raio2 = convert_binary(radius_2)
 				if(distancia < (raio1 + raio2)):
 					val_col = self.area_intersec(erb, others_erb)
 					str_col = conv(val_col, 0)
 					print(str_col ,'->', len(str_col))
 					for j in range(len(str_col), 0):
 						aux_list[j]= str_col[j]
 				else:
 					print("nao colidiu")


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

		R1 = convert_binary(radius_1)
		R2 = convert_binary(radius_2)

		if (R1 > R2):
			area = pi * pow(R2, 2)

		if (R2 > R1):
			area = pi * pow(R1, 2)
		
		if (R1 == R2):
			area = ((2 * pi * pow(R1, 2)) / 3) - ((sqrt(3) * pow(R1, 2)) / 2)

		x = ceil(area/1000)

		return x
# area do hexagono é igual a area de 6 triangulos equilateros  com lado igual a raio
	
	def area_hexa(self, radius):
		area = (3 * pow(radius,2) * sqrt(3) ) / 2
		return area

#funcoes comuns -> organizar classe posteriormente
def point_space(individuo):
	x = []
	for i in range(0 ,6):
		x.append(individuo[i])
	a = convert_binary(x)

	y = []
	for i in range(7 ,13):
		y.append(individuo[i])
	b = convert_binary(y)
	ponto = a,b
	return ponto

def convert_binary( binary):
	str1 = ''.join(str(x) for x in binary)
	n = int(str1, 2)
	return n

def conv_radius_area():
	area = pi * pow(RADIUS, 2)
	return (area/1000) #retorna area em km

def calc_fitness(individuo):
	xradius = []
	for i in range(15 ,22):
		xradius.append(individuo[i])

	obj = pop()
	area_coverage = obj.area_hexa(convert_binary(xradius))

	radian = []
	for i in range(47, 54):
		radian.append(individuo[i])

	P_tot = convert_binary(radian)
	P_max = 255
	sobre = 1.0
	n_sbr = 1.0
		
	F_fit = (AREA - ( area_coverage / AREA ) ) + (sobre / AREA) + (P_tot / (n_sbr * P_max) )


class slayer():
	def __init__(self):
		pass
		
def conv(n, flag):
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

	if flag:
		return string
	else:
		return k




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
