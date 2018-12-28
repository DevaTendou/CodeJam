import math as m

N = 8 #Numero de lugares
K = 6 #Numero de pessoas

def func(k, n):
	
	if (n & 1):	tail = False
	else:		tail = True
	
	peopleLeft = k
	leftchoice, rightchoice = 0, 0

	nParts = 1
	while (nParts << 1) < k:	nParts <<= 1
	
	peopleLeft -= nParts
	placesPerPart = n//nParts
	
	if tail and (peopleLeft == 1):
		leftchoice = ((placesPerPart + 1) >> 1) - 1
		rightchoice = (placesPerPart + 1) >> 1
	elif placesPerPart == 1:
		leftchoice = 0
		rightchoice = 0
	else:
		leftchoice = (placesPerPart >> 1) - 1
		rightchoice = placesPerPart >> 1 
		
	
	
	print(peopleLeft, placesPerPart, tail)
	print(leftchoice, rightchoice)
	
	
	
	
	
func(K, N)