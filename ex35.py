from sys import exit

def gold_room() :
	print ("This room is full of gold. How much do you take?")
	
	next = input(">>Type a number, please.\t- ")
	
	if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next :
		how_much = int(next)
		
		if how_much < 50 :
			print ("Nice, you're not greedy, you win!")
			exit(0)
		else :
			dead("You greedy bastard!")
	else :
		dead("Man, learn type a number.")
			
		
def bear_room() :
	print ("There is bear here")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is in fruit of another door.")
	print ("How are you going to move the bear?")
	bear_moved = False

	while True : 
		next = input(">> take honey , taunt bear or open door?\t-")
		
		if next == "take honey" :
			dead("The bear looks at you then slaps your face of.")
		elif next == "taunt bear" and not bear_moved :
			print ("The bear has moved has moved from the door. You can go through it now.")
			bear_moved = True
		elif next == "taunt bear" and bear_moved :
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" or "open the door" and bear_moved :
			gold_room()
		else :
			print ("I got no idead what that means.")
			
def cthulhu_room() :
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, Whatever stares at you and go insane.")
	print ("Do you flee for you life or eat your head?")
	
	next = input(">>flee for you life, eat your head?\t-")
	
	if "flee" in next or "flee for you life" in next :
		start()
	elif "head" in next or "eat your head" in next :
		dead("Well that was tasty!")
	else :
		print ("Well you need answer!!")
		cthulhu_room()
		
def dead(why) :
	print (why, "Good job, you're dead!!!")
	exit(0)
		
def start() :
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")
	
	next = input(">>Choose right or left, please.\t-")
	
	if next == "left" :
		bear_room()
	elif next == "right" :
		cthulhu_room()
	else :
		dead("You stumble around the room until starve.")
		
start()		