
c = int(input())	# unit cost
r = int(input())	# unit price
N = int(input())	# possible demand = 8
q = int()			# best order
p = []				# probability
pi = int() 			# unit profit
pi_t = []		# total profit

for i in range(N+1):			# 0 to N
	p.append(float(input()))	# len(p) = N+1
# print(p)

for q in range(0, N+1):			# 0 to N
	pi = 0
	
	maxSell = q
	if N < q:
		maxSell = N
		
	for i in range(N+1):		# 0 to N
		if i >= maxSell:
			j = maxSell
		else:
			j = i 
		pi += (j*r - q*c) * p[i]
	pi_t.append(pi)				# pi_t[0 to N]

max = 0
pi_max = pi_t[0]
for i in range(1, N+1):
	if pi_t[i] >= pi_max:
		max = i
		pi_max = pi_t[i]

print(str(max), str(int(pi_max)))




