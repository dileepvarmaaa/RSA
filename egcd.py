dividend = int(input())
divisor = int(input())
q = dividend//divisor
r = dividend % divisor
dividend1 = 1
dividend2 = 0
divisor1 = 0 
divisor2 = 1
remainder1 = dividend1 - (q*divisor1)
remainder2 = dividend2 - (q*divisor2)
def egcd(dividend,dividend1,divisor2,divisor,divisor1,remainder1,remainder2,dividend2,r):
	while(r!=2):	
		dividend = divisor 
		divisor = r
		q = dividend // divisor
		r = dividend % divisor
		dividend1 = divisor1
		divisor1 = remainder1
		remainder1 = dividend1 - (q*divisor1)
		dividend2 = divisor2
		divisor2 = remainder2
		remainder2 = dividend2 - (q*divisor2)
	return(remainder1,remainder2)
print(egcd(dividend,dividend1,divisor2,divisor,divisor1,remainder1,remainder2,dividend2,r))

