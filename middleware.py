
import random

string = ""
size = 10
for x in range(0, size):
	abc = "ABCDEFGHIJKLMNOPQRSTUVWKYZ"
	letterOrNumber = random.randint(0,1)

		#Inicialmente Letra sera un numero alatorio de 0 a 9
	letra = random.randint(0,9)
		#si es 1 entonces sera una letra
	if letterOrNumber == 1:
				#Se rifa la letra a escoger
		letraPos = random.randint(0,25)			
		letra = abc[letraPos]
			#Se rifa si sera UPPER o Lower
		numberCase =random.randint(0,1)
		if numberCase == 1:
			letra = letra.lower()
		string = string + letra
	else:
		string = string + str(letra)

print(string)