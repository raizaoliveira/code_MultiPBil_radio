from random import getrandbits
from math import pi, pow, ceil
from math import sqrt
from mpi4py import MPI
import time 


'''
cromossomo -> (x,y) - estado (ativo, nao ativo) - raio  - populacao -  radiacao de energia - sobreposicao
considerar area de ddos = 4000 km -> lado 64 
0 ,7,14, 15, 23,31,39,47
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

#inicializa as populacoes
	def init_n_pop(self):
		POP = self.aux_init_pop()
		return POP

#auxilia na determinacao de area de sobreposicao para os individuos da populacao
	def aux_init_pop(self):
		POP = self.init_pop()
		self.checaColisao(POP)
		return POP

#Gera e retorna um cromossomo
	def init_individual(self):
		llist_indi = []
		for i in range(1, self.lenght_gene):
			pos = getrandbits(1) # pares entre 0 e 9
			llist_indi.append(pos)

		return llist_indi 

#inicializa e retorna uma  popupalacao
	def init_pop(self):
		#individuo 1 da pop é usado para criar o primeiro modelo de probabilidade
		list_pop = []
		for i in range(0, self.SIZE_POP):
			baby = self.init_individual()
			if (baby in list_pop):#repita ate o individuo que o individuo gerado não exista na pop
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
 					aux_list = fill_list_bin(str_col)
 					aux = 0
 					for i in range(39, 46):
 						erb[i] = aux_list[aux]
 						others_erb[i] = aux_list[aux]
 						aux += 1


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
	
#retorna uma lista com a mmm das populacoes
	def cal_mmm_populations(self, pop1, pop2, pop3, pop4):
		list_mmm = []
		x = mmm(pop1)
		list_mmm.append(x)
		x = mmm(pop2)
		list_mmm.append(x)
		x = mmm(pop3)
		list_mmm.append(x)
		x = mmm(pop4)
		list_mmm.append(x)
		print(list_mmm)
		return list_mmm
		

'''
funcoes comuns -> organizar classe posteriormente
'''
#retorna o ponto de localizacao da antena
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

#convert uma lista de bits em um inteiro
def convert_binary( binary):
	str1 = ''.join(str(x) for x in binary)
	n = int(str1, 2)
	return n

#retorna a area de cobertura de uma antena
def conv_radius_area():
	area = pi * pow(RADIUS, 2)
	return (area/1000) #retorna area em km

#calculo  de fitness de um individuo
def calc_fitness(individuo):
	xradius = []
	for i in range(15 ,22):
		xradius.append(individuo[i])

	obj = pop()
	area_coverage = obj.area_hexa(convert_binary(xradius))

	radian = []
	for i in range(47, 54):
		radian.append(individuo[i])

	cov_sob = []
	for i in range(39, 46):
		cov_sob.append(individuo[i])


	pot_tot = []
	for i in range(47, 54):
		pot_tot.append(individuo[i])

	P_tot = convert_binary(radian)
	sobre = convert_binary(cov_sob)
	P_max = 255
	n_sbr = 1.0

	F_fit = (AREA - ( area_coverage / AREA ) ) + (sobre / AREA) + (P_tot / (n_sbr * P_max) )
	return F_fit

#calcula a media da metade dos melhores individuos de uma populacao
def mmm(population):

	best = []
	for i in range(0, len(population)):
		best.append(0)

	k = 0
	for item in population:
		best[k] = calc_fitness(item)
		print('best[',k,'] = ', calc_fitness(item))
		print('best', best[k])
		k+=1

	best.sort()
	print('minimo', min(best))

	som = 0;
	lim = ceil(len(population)/ 2) 
	som = best[0]
	i = 0
	while i < lim:
		val = best[i]
		som += val
		i+=1

	som = som / lim;
	return som;


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



def fill_list_bin(list_str):
	list_str = list_str[::-1]
	list_aux = []
	for i in range(0,8):
		list_aux.append(0)

	n = len(list_str)
	x = 8 - n
	aux = 0
	for i in range(x,8):
		list_aux[i] = list_str[aux]
		aux += 1

	return list_aux

def main():

	ini = time.time()
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	#random.seed() #inicia a semente dos número pseudo randômicos

	'''
	POP_1 = initialize_population();/*Inicializa as populacoes aleatoriamente*/
	POP_2 = initialize_population();
	POP_3 = initialize_population();
	POP_4 = initialize_population();

	best1 = mmm(POP_1);/*Calcula a media da metada dos melhores individuos de cada populacao*/
	best2 = mmm(POP_2);
	best3 = mmm(POP_3);
	best4 = mmm(POP_4);
	

	/*Cria os modelos probabilisticos*/
	N1 = create_models1(POP_1, modelo1, 25, best1);
	printf("N1 %d\n", N1);
	N2 = create_models1(POP_2, modelo2, 50, best2);
	printf("N2 %d\n", N2);
	N3 = create_models1(POP_3, modelo3, 75, best3);
	printf("N3 %d\n", N3);
	N4 = create_models1(POP_4, modelo4, 100, best4);
	printf("N4 %d\n", N4);
	'''
	if rank == 0:
		'''
		inicialize as populacoes
		calcule a media da metade dos melhores indiduos
		crie os modelos variando entre 25%, 50%, 75%  e 100%
		envie para cada escravo seu modelo correspondente
		'''
		print('mestre')
		obj = pop()
		POP_1 = obj.init_n_pop()
		POP_2 = obj.init_n_pop()
		POP_3 = obj.init_n_pop()
		POP_4 = obj.init_n_pop()
		llist_mmm = obj.cal_mmm_populations(POP_1, POP_2, POP_3, POP_4)
		print('llist', llist_mmm)
		fim = time.time()

		print("time", fim - ini);
	if rank == 1:
		print('escravo 1')
	if rank == 2:
		print('escravo 2')
	if rank == 3:
		print('escravo 3')

       


if __name__ == '__main__':
	main()
