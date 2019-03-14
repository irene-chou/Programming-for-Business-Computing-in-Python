## input
str1 = input()
s1 = str1.split()
n_v = int(s1[0])				# number of villages
n_b = int(s1[1])				# number of base stations
d_cov = float(s1[2])				# the distance base station can cover

x = []
y = []			
p = []			# population 
for i in range(n_v):
	str = input()
	s = str.split()
	x.append(int(s[0]))
	y.append(int(s[1]))
	p.append(int(s[2]))

p_b = []					# this base station can cover how many villagers
b_max = int()				# the base station that can cover the most villagers
isCov = [False] * n_v		# village is covered or not 
d = float()					# the distance between 2 villages
p_t = int()					# covered villagers totally

##
for i in range(n_b):
	p_b = [0] * n_v				# initialize
	for j in range(n_v):		# base station	
		for k in range(n_v):	# village
			d = ((x[j] - x[k])**2 + (y[j] - y[k])**2)**(1/2)
			if (d <= d_cov) and (isCov[k] == False):
				p_b[j] += p[k]
				
		if p_b[j] > p_b[b_max]:
			b_max = j
	
	# put base station in village[b_max]
	print(b_max+1, end = ' ')
	p_t += p_b[b_max]
	
	# set some isCov to True
	for j in range(n_v):
		d = ((x[j] - x[b_max])**2 + (y[j] - y[b_max])**2)**(1/2)
		if (d <= d_cov) and (isCov[j] == False):
			isCov[j] = True

print(p_t)

