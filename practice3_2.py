a = int(input())

b = 1000 - a
x1 = b//500
b %= 500
x2 = b//100
b %= 100
x3 = b//50
b %= 50
x4 = b//10
b %= 10
x5 = b//5
b %= 5
x6 = b


fo = open("output.txt", "w")
if x1:
	fo.write("500, " + str(x1))
	if (x2 != 0) | (x3 != 0) | (x4 != 0) | (x5 != 0) | (x6 != 0):
		fo.write("; ")
if x2:
	fo.write("100, " + str(x2))
	if (x3 != 0) | (x4 != 0) | (x5 != 0) | (x6 != 0):
		fo.write("; ")
if x3:
	fo.write("50, " + str(x3))
	if (x4 != 0) | (x5 != 0) | (x6 != 0):
		fo.write("; ")
if x4:
	fo.write("10, " + str(x4))
	if (x5 != 0) | (x6 != 0):
		fo.write("; ")
if x5:
	fo.write("5, " + str(x5))
	if (x6 != 0):
		fo.write("; ")
if x6:
	fo.write("1, " + str(x6))

fo.close()