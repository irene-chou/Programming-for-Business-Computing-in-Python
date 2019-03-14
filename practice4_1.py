
c = int(input())	# unit cost
r = int(input())	# unit price
N = int(input())	# possible max demand
q = int(input())	# order
p = []				# probability
pi = [] 			# unit profit
pi_t = int()		# total p
rofit

counter = int()
for i in range(N+1):			# 0 to N
	p.append(float(input()))	# len(p) = N+1

max = q
if N < q:
	max = N


for i in range(N+1):			# 0 to N
	if i >= max:
		j = max
	else:
		j = i
	pi.append((j*r - q*c) * p[i])
	pi_t += pi[i]

print(int(pi_t))


