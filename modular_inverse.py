a   = int(input())
mod = int(input())
def modular(x,d):
	for i in range(1,d):	
		if (x*i)%d == 1:
			return(i)	
			break
	return("no")
print(modular(a,mod))