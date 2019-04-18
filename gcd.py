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

x = (set(factors_a) & set(factors_b))
print(x)

largest_common_factor = max(x)
print(largest_common_factor)

