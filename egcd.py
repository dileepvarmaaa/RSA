a = int(input())
factors_a=[]
for i in range(1,a+1):
	if a%i==0:
		factors_a.append(i)
print(factors_a)


b = int(input())
factors_b=[]
for j in range(1,b+1):
	if b%j==0:
		factors_b.append(j)
print(factors_b)
g = (set(factors_a) & set(factors_b))
print(g)

greatest_common_divisor = max(g)
print(greatest_common_divisor)

def egcd(x,y):
	for x in range(1,1000):
		for y in range(1,1000):
			if (a*x + b*y) == greatest_common_divisor:	
				return(x,y)
				break

print(egcd(a,b))


