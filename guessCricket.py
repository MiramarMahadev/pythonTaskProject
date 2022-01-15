import random
gaming = True
score = scorel = 0  			# INITIAL SCORES
space = (" "*20)  				# THIS RETURNS 15 SPACES, THIS VARIABLE CAN BE USED IN PLACE OF ("               ") 
end = (space + "Game over! ") 	# (space+"Game over! ") IS USED 3 TIMES . ASSIGNED IT A VARIABLE TO CALL WITH A SINGLE WORD


def blank_line(): 				#THIS FUNCTIONS CREATES A BLANK LINE
	print("")

def check_winner():  			#THIS FUNCTION GIVES JUDGEMENT BY COMPARING THE SCORES

	blank_line()
	if scorel > score :
		return((end+"COMPUTER wins").upper())

	elif scorel < score :
		return((end+"user_run wins").upper())

	else:
		return((end+"draw").upper())
	
		
print('''          
RULES OF THIS GAME:

          1.YOU WILL COMPETE WITH COMPUTER
	  2.ENTER A SINGLE DIGIT RUN
	  3.IF YOU AND COMPUTER ENTER THE SAME RUN,THEN GAME ENDS
	  4.ONE WITH THE HIGHEST SCORE WINS
	  5.IF YOU AND COMPUTER HAVE THE SAME SCORE,THEN GAME DRAWS''')

# GAME STARTS

while gaming:
	try:
		blank_line()
		user_run = int(input("Enter your Run: "))   			#TAKES THE USER RUN 
		
		if user_run >= 10 or user_run <= 0 :  	  		# CHECKING IF THE ENTERED RUN IS NOT IN BETWEEN 1 AND 9
			user_run = 0       					  		#IF RUN ENTERED IS NOT IN BETWEEN 1 AND 9 THEN THAT RUN WILL NOT BE COUNTED
			print('choose an integer between 1 and 9 or else your run will not count')

		else:
			COMPUTER = random.randint(1,9) 			 	#GENERATING A RANDOM INTEGER BETWEEN 1 AND 9
			print("computer's Run :" + str(COMPUTER)) 	#DISPLAYING COMPUTER'S RUN

			if user_run == COMPUTER:  
				blank_line()   												#IF COMPUTER AND USER SCORE THE SAME RUN 
				print(space+"your total score:".upper()+ str(score)) 		#IT DISPLAYS USER SCORE 
				print(space+"computer's total score:".upper()+ str(scorel)) #IT DISPLAYS COMPUTER SCORE
				blank_line										
				print(check_winner())										#DISPLAYS THE JUDGEMENT
				break 														#GAME WILL STOP

			else:                         	#IF COMPUTER AND USER SCORE DIFFERNT RUNS
				scorel += COMPUTER    		#STORING THE SUM OF COMPUTER'S RUNS 
				score += user_run        	#STORING THE SUM OF USER'S RUNS
	except:
		print('choose an integer between 1 and 9')	