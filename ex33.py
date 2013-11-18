i = 0
numbers = []

n = input("--> ")
a = int(n)

for i in range(i,a) :
	print ("At the top i is %d" % i)
	numbers.append(i)

	print ("Numbers now: ", numbers)
	print ("\tAt the botoom i is %d" % i + "\n")

print ("The numbers: ")

for num in numbers :
	print (">>>\t" + str(num))	