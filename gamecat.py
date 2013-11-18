from sys import exit

def dead(acto) :
	print (acto ,"decision wrong!!!")
	print ("Back at begging")
	casting = ("Yes or no -> ")
	if casting == "yes" :
		began()
		
	else:
		print ("Well, see you later")
		exit(0)


def food() :
	print ("Do you want to eat or not?")
	
	choose = input("-> ")
	
	if choose == "eat" or choose == "Eat" or choose == "EAT" :
		print ("You're eatting now!")
		
	else:
		print ("You're don't eatting")

def sniff() :
	print ("You want to sniff or not?")
	
	step = input("-> ")
		
	if step == "sniff" or step == "Sniff" :
		print ("You're sniffing now!")
	
	else: 
		print("You don't are siffing!")
			




			
def mode() :
	print ("Well, you want to run or walk?")
	
	cat_moved = False
	
	while True :
		step = input("-> ")
	
		if step == "run" or step == "Run" or step == "RUn" or step == "RUN" :
			print ("You're running now!")
			cat_moved = True
		
		elif step == "walk" or step == "Walk" or step == "WALK" :
			print ("You're walking now!")
			cat_moved = True
		
		else :
			print ("Please, you need do a move!!!")

def sniff() :
	print ("Do you go will eat or sniff?")
		
		decision = input("-> ")
		
		if decision == "sniff" or decision == "Sniff" or decision == "SNIFF" :
			print ("Do you go will eat or not?")
			
			step = input("-> ")
			
			if step == "eat" or step == "Eat" or step == "EAT" :
				print ("You're eatting now")
				print ("But you're not felling well")
				dead("You're dead now, you're could eat food of house out")
				
			else:
				print("Congratulations, you got a good decision.")
				print ("GO ahead")
				mode()
				
		else:
			dead("You don't even sniffed")

def began() :
	print ("The cat walk through the neighbourhood as very cat.")
	print ("But in this episode it will find many challenges that have to be made.")
	print ("It has to make decisions crucial to their survival and return home.")
	print ("Fillers him in search of better situations.\n\n")
	
	print ("The cat is on the roof of neighbour, what you do now decided at the beginning of this adventure?\n")
	print ("Guide the cat to first wall you meet,\n at some food along the way(first sniff),\n go to the roof of another neighbour ,\n or remain stationary\n")
	print ("wall, roof, or stationary")
	
	step = input("-> ")
	
	if step == 'wall' or step == "Wall" or step == "WALL" :
		mode()
		print ("Here, you have a choose way!")
		print ("By the way")
		print ("You're going to the first wall.")
		print ("What do you want to do ?")
		print ("Have a some food on way")
		print ("Do you'll stop or continue?")
		
		decision = input("-> ")
		
		if decision == "stop" or decison == "Stop" or decision == "STOP" :
			print ("You have time to some food")
			sniff()
			
		else:
			print ("You don't care even to food, so continue!")
			print ("You come to the wall")
			print ("Fist step done")
			

		
		
		