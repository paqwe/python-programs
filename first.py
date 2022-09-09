limit=100

def isprime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	else:
		return True

# print(isprime(15))
for i in range(3,limit):
	x = isprime(i)
	if x==True:
		print(i)