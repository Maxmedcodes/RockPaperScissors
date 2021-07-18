from random import randint

moves = ["rock", "paper", "scissors"]
active = True
while active:
	computer = moves[randint(0,2)]
	user = input("rock , paper or scissors or end the game : ").lower()
	if user == "end":
		print("you have quit")
		break 
	elif user == computer:
		print("its a tie !!!", "you chose",user, "and computer chose", computer)
	elif user == "rock":
		if computer == "paper":
			print("You lose ",computer,  "beats ",user)
		else:
			print(" You win !!!",user, "beats", computer)
	elif user == "scissors":
		if computer == "paper":
			print("you win",user,"beats",computer)
		else:
			print("you lose", computer,"beats",user)
	elif user == "paper":
		if computer == "rock":
			print("you win",user, "beats",computer)
		else:
			print("you lose", computer, "beats", user)
	if user == "quit":
		print("The game has ended thank you for playing ")
		active = False
