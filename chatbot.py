import time
question = ""

while (question != 'Goodbye!'):

	question = raw_input("Please ask me a question: ")
	if ( question == "How are you?"):
		print("I am starving.")
	elif( question == "What is your favorite text editor?"):
		print("Gedit is alright, I guess.")
	elif( question == "What is the date?"):
		print("Today is " + time.strftime("%m/%d/%Y"))
	elif( question == "Goodbye!"):
		break
	else:
		print("What????")

print("Goodbye!")
