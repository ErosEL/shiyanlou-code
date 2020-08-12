a = 0
while a < 100:
	a += 1	
	if a == 7:
		continue	
	elif a % 7 == 0:
		continue
	elif a % 10 == 7:
		continue
	elif 70 < a and a < 80:
		continue
	print(a)
