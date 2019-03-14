## variables
c1 = int(input())			# unit cost floor
c2 = int(input())			# unit cost ceiling
a1 = int(input())			# const.
r1 = int(input())			# const.
r2 = int(input())			# const.

a2 = a1 - r1 + 2*r1			# get a2
a3 = a2 - 2*r2 + r2			# get a3
p = int()					# price
q = []						# demand of a3 prices
pi = []						# profit
p_max = []					# prince of max profit


## calculate
for c in range(c1, c2 + 1):
	q = []						# initialize
	pi = []						# initialize
	i = int()					# counter
	p_max.append(c)
	while True: 
		p = c + i
		q.append(0)
		if p < r1:
			if (a1 - p) > 0:
				q[i] = a1 - p
		elif p < r2:
			if (a2 - 2*p) > 0:
				q[i] = a2 - 2*p
		elif p < a3:
			if (a3 - p) > 0:
				q[i] = a3 - p
		
		pi.append((p-c)* q[i])
		
		# find max profit
		if pi[i] > pi[p_max[c-c1] - c]:	# if this profit is bigger than last maximum
			p_max[c-c1] = p
		
		# the condition to break
		if q[i] <= 0:
			break
		
		# counter
		i += 1
	

## output
for c in range(c1, c2+1):
	print(p_max[c-c1], end = '')
	if c != c2:
		print(",", end = '')

