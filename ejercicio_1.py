from math import sqrt

def cadena(cadena):
	return len(cadena)

def raiz(num):
	return sqrt(num)


def main():
	op = input("1.-Cadena\n2.-Raiz\n")

	if op == 1:
		print "###"*8
		string = raw_input("Ingrese Cadena: ")
		print "La Cadena Tiene: ", cadena(string)
	
	elif op == 2:
		
		print "###"*8
		num = input("Ingerse Numero: ")
		
		while num <= 0:
			num = input("Numero Debe ser Mayor a Cero: ")

		print "La Raiz es: ", raiz(num)
	
	else:
		print "Opcion No Valida."


main()