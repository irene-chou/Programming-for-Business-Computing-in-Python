## 求最佳進貨量q*及其預期利潤

### variables
c = int(input())	# unit cost
r = int(input())	# unit price
N = int(input())	# possible demand
s = int(input())	# salvage value
q = int()			# your order 
p = []				# probability
pi = int() 			# profit
pi_t = []			# total profit

### user input
for i in range(N+1):			# 0 to N
	p.append(float(input()))	# len(p) = N+1
# print(p)

### calculate the profit(pi)
for q in range(N+1): 		# 0 to N
	print("q =", q)
	pi = -q*c
	for i in range(N+1):
		print("pi =", pi)
		# i should less than q
		if i < q:
			j = i
		else:
			j = q
		
		pi += (j*r + (q-j)*s) * p[i]
	pi_t.append(pi)

### who's best
bestQ = 0
for i in range(N+1):
	if pi_t[i] > pi_t[bestQ]:
		bestQ = i

### output
print(bestQ, int(pi_t[bestQ]))

