import os
os.chdir('E:\\NTU\\大四下\\商管程式設計')

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
fo.write(str(x1) + " " + str(x2) + " " + str(x3) + " " + str(x4) + " " + str(x5) + " " + str(x6))
fo.close()