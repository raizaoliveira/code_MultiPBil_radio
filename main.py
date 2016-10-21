from random import getrandbits, random
from math import pi, pow, ceil
from math import sqrt
from mpi4py import MPI
import time 
import matplotlib.pyplot as plt



'''
cromossomo -> (x,y) - estado (ativo, nao ativo) - raio  - populacao -  radiacao de energia - sobreposicao
considerar area de ddos = 4000 km -> lado 64 
0 ,7,14, 15, 23,31,39,47
'''																			
AREA = 4000 # aproximadamente area de dourados 
RADIUS = 100
MUT_PROB = 0.3
MUT_SH = 0.04

#antena de telefonia movel ERB

class pop():
	def __init__(self):
		self.SIZE_POP = 50
		self.lenght_gene = 55
		self.dbi = 255

	#inicializa as populacoes
	def init_n_pop(self):
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
		k+=1
	best.sort()
	som = 0;
	lim = ceil(len(population)/ 2) 
	i = 0
	while i < lim:
		val = best[i]
		som += val
		i+=1

	som = som / lim;
	return som;

		
def conv(n, flag):
	x=n
	k=[]
	while (n>0):
		a = int(float(n%2))
		k.append(a)
		n=(n-a)/2
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


class model():
	def __init__(self, SIZE):
		self.SIZE =  SIZE
		self.alpha = 0.05
		#define MUT_PROB 0.3
		#define MUT_SH 0.04

	def make_hamming(self, ind1, ind2):
		#se P2 < F entao o individuo2 é usado para gerar outro modelo, senao avalia-se o proximo individuo
		p = 0
		for i in range (0, 54):
			if ind1[i] == ind2[i]:
				p+=1

		P2 = (p * 100) / 54
		return P2

	def drop_pop(self, X):
		list(P)
		for i in range (0, self.SIZE):
			P[i+1] = P[i] * (1.0 - self.alpha) + X[i] * self.alpha

	def create_model(self, POP, average, F):
		aux = 0
		model = []
		ant_pop = []
		average = average / 10
		for item in POP:
			if aux == 0:
				for j in range(0, self.SIZE):
					x =  (((0.5 - self.alpha) * item[j] ) + (self.alpha * average)) / 100
					model.append(x)
					ant_pop.append(item[j])							
			if aux > 0:
				P2 = self.make_hamming(ant_pop, item)
				del ant_pop[:]
				if P2 < F:
					for j in range (0, self.SIZE):
						x = ((0.5 - self.alpha) * item[j] + self.alpha * average) / 100
						model.append(x)
				for j in range (0, self.SIZE):
					ant_pop.append(item[j])
			aux += 1
		return model
				
		





'''
criacao dos modelos probabilisticos
tem como parametros a matiz de populacao
matriz do modelo
F -> porcentagem de similaridade (25, 50, 75 ou 100)
average -> media da metade dos melhores de cada populacao
retorna a quantidade de modelos criados para cada populacao
'''



def main():


	ini = time.time()
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	#random.seed() #inicia a semente dos número pseudo randômicos

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

		obm = model(54)
		model_1 = obm.create_model(POP_1, llist_mmm[0], 25)
		model_2 = obm.create_model(POP_2, llist_mmm[1], 50)
		model_3 = obm.create_model(POP_3, llist_mmm[2], 75)
		print(llist_mmm[2])
		
		print('enviado', len(model_1), 'para escravo 1')
		comm.send(model_1,dest=1,tag=1)
		print('enviado', len(model_2), 'para escravo 2')
		comm.send(model_2,dest=2,tag=2)
		print('enviado', len(model_3), 'para escravo 3')
		comm.send(model_3,dest=3,tag=3)

		data_1 = comm.recv(source=1, tag=1)
		data_2 = comm.recv(source=2, tag=2)
		data_3 = comm.recv(source=3, tag=3)
	
		fit1 = calc_fitness(data_1)
		fit2 = calc_fitness(data_2)
		fit3 = calc_fitness(data_3)

		if (fit1 < fit2):
			if (fit2 < fit3):
				print('1 , 2, 3')

			if (fit3 < fit2):
				print('1 , 3, 2')

			if (fit3 < fit1):
				print('3, 1, 2')

		if (fit2 < fit1):
			if (fit1 < fit3):
				print('2 , 1, 3')

			if (fit3 < fit1):
				print('2, 3, 1')

			if (fit3 < fit2):
				print('3, 2, 1')




		fim = time.time()

		print("time", (fim - ini)/60)
	if rank == 1:
		data = comm.recv(source=0, tag=1)
		print('escravo 1')
		counter = 0
		while counter < 10:
			lista = new_pop(data)
			bests = []
			for item in lista:
				best = 0
				individuo = item
				for elemento in item:
					fit = calc_fitness(elemento)
					if fit > best:
						best = fit
						individuo = elemento
				bests.append(individuo)
		
				
			bestall = bests[0]
			data = update_model(bestall, data)
			counter += 1
		print('o 1 envia ', bestall)
		comm.send(bestall,dest=0,tag=1)
	
	if rank == 2:
		data = comm.recv(source=0, tag=2)
		print('escravo 2')
		lista = new_pop(data)
		counter = 0
		while counter < 10:
			lista = new_pop(data)
			bests = []
			for item in lista:
				best = 0
				individuo = item
				for elemento in item:
					fit = calc_fitness(elemento)
					if fit > best:
						best = fit
						individuo = elemento
				bests.append(individuo)
		
				
			bestall = bests[0]
			data = update_model(bestall, data)
			counter += 1

		comm.send(bestall,dest=0,tag=2)
		print('modelos', len(data), 'populacoes', len(lista))

	if rank == 3:
		data = comm.recv(source=0, tag=3)
		print('escravo 3')
		lista = new_pop(data)
		counter = 0
		while counter < 10:

			lista = new_pop(data)
			bests = []
			for item in lista:
				best = 0
				individuo = item
				for elemento in item:
					fit = calc_fitness(elemento)
					if fit > best:
						best = fit
						individuo = elemento
				bests.append(individuo)
		
				
			bestall = bests[0]
			data = update_model(bestall, data)
			counter += 1
		comm.send(bestall,dest=0,tag=3)

def new_pop(set_models):
	pop_model = []
	for model in set_models:
		new_pop = init_new_pop(len(set_models))
		pop_model.append(new_pop)
	return pop_model


#Gera e retorna um cromossomo
def init_gene():
	llist_indi = []
	for i in range(1, 55):
		pos = getrandbits(1) # pares entre 0 e 9
		llist_indi.append(pos)

	return llist_indi 

#inicializa e retorna uma  populacao
def init_new_pop(tam):
	list_pop = []
	for i in range(0, tam):
		baby = init_gene()
		if (baby in list_pop):#repita ate o individuo que o individuo gerado não exista na pop
			while (baby in list_pop):
				baby = init_gene()
		else:
			list_pop.append(baby)

	return list_pop


def update_model(ind, p):
	model = []
	for i in range (0, len(ind)):
		x = p[i]  * (1.0 - 0.05) + ind[i] * 0.05
		var = random()
		if (var < MUT_PROB):
			x = p[i] * (1.0 - MUT_SH) +  getrandbits(1) * (MUT_SH)
		model.append(x)
	return model

       


if __name__ == '__main__':
	main()
