x1 = int(input())
x2 = int(input())
y = int(input())

if y < x1:
	x1 -= y
	x2 += y
else:
	x2 += x1
	x1 = 0
	
print(x1, x2)

	
