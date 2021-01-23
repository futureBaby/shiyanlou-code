for n in range(1,101):
	if n % 7 == 0 or n % 10 == 0 or n // 10 == 0:
		continue
	print(n)

