from random import getrandbits
from math import pi, pow

#use area em metros
area = 10000
#use 1 byte for area
#use 1 byte for number persons
#use 1 byte for potencia
#fitness is a number of anthens
#antena de telefonia movel ERB

# use os.urandom para gerar numeros aleatorios
class pop():
	def __init__(self):
		self.SIZE_POP = 30
		self.lenght_gene = 24
		self.dbi = 255

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
			print(list_pop)

	def create_model(self):
		#M[i] = (1 - alfa) * Xi + alfa * (average half best individuals)
		pass
		#for individual in range (2, N):
			#if max(Probn(Indi | M(k)), k=1 .... Ni) < Fc

	def calc_hamming(self):
		#Probn = (A * 100) \ (T)
		pass

	def calc_fitness(self, gene):
		pass
		#maximize area e diminua qtd antena

	def convert_binary(self, binary):
		str1 = ''.join(str(x) for x in binary)
		n = int(str1, 2)
		return n

	def conv_radius_area(self, radius):
		area = pi * pow(radius, 2)
		return area




def conv():
	n=int(input('please enter the no. in decimal format: '))
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
	#random.seed() #inicia a semente dos número pseudo randômicos
	obj = pop()
	x = obj.conv_radius_area(15)
	print(x)
	


if __name__ == '__main__':
	main()
