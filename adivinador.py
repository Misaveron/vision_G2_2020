print('') 
print('') 
print('') 
print('--------------------------Programa ADIVINA--------------------------')

veces = 0
c_entrada =0
condicion =0
rintentos =0
tintentos=0
print('') 
print('') 
print('') 
tintentos = int (input(' Ingresá la cantidad de intentos que quieres tener '))
print('') 
print('') 
print('') 

while condicion ==0:
	n_entrada = int (input(' Ingresá un numero entero del 0 al 100: '))

	import random

	numero = random.randint(0, 0)
	veces = veces + 1
	rintentos = tintentos - veces 
	
		if numero == n_entrada:
			print('Ingresaste el número "{0}" y... ¡adivinaste el numero!'.format(n_entrada))
			print('------------------Felicitaciones!------------------')
			condicion = condicion + 1	
		else:
			if veces < tintentos:
				print('Ingresaste el número "{0}" y no adivinaste, será la próximaa...'.format(n_entrada))
				print('') 
				print('La cantidad de intentos es {0} y te quedan {1} oportunidades '.format(veces, rintentos))
	
				print('') 
			else:	
		  		print( '--------------GAME OVER--------------')
				condicion = condicion + 1 
