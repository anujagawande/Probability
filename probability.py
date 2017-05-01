import random

#Probabilistically estimating the value of pi.
def piEstimate(n):
	m =0 #to keep track of darts that land within circle
	for i in range(n):
		x = random.uniform(-1,1)   # generating random co-ordinates BETWEEN -1.0 and 1.0 exclusive
		y = random.uniform(-1,1)
		#if random co-ordinates are within circle, increment m
		if ((x*x)+(y*y))**0.5 <= 1:
			m = m+1
	pi = (4.0*m)/n
	print ("Pi = " + str(pi))

piEstimate(50000)
print ("---------------------------------------------------")

#Simulation of Monty Hall problem. 1,2,3 represent doors.
#for staying with original door
def simulation():
	i=0
	numberOfWins=0
	#simulating for 100000 trials
	while i<= 100000:
		carDoor = random.randint(1,3)#randomly placing car behind one of three doors
		choosenDoor = random.randint(1,3)#player randomly choosing any 1 of 3 doors
		if carDoor == choosenDoor:
			numberOfWins=numberOfWins+1
		i=i+1
	print ("Number of wins(staying with original door): " + str(numberOfWins))
	percentageOfWin = (numberOfWins/100000.0)*100
	print ("Percentage of wins: " + str(percentageOfWin) + "%")
	print ("---------------------------------------------------")

#for changing the door
def simulation2():
	i=0
	numberOfWins2 = 0
	while i<= 100000:
		carDoor2 = random.randint(1,3)
		choosenDoor2 = random.randint(1,3)
		#checking for loosing door and opening it. Changing the players choice to the one remaining door
		if carDoor2 ==1 and choosenDoor2 ==2: 
			loosingDoor = 3
			choosenDoor2 = 1
			numberOfWins2  = numberOfWins2+1
		if carDoor2 ==2 and choosenDoor2==1: 
			loosingDoor = 3
			choosenDoor2= 2
			numberOfWins2  = numberOfWins2+1
		if carDoor2 ==2 and choosenDoor2==3:  
			loosingDoor = 1
			choosenDoor2 = 2
			numberOfWins2  = numberOfWins2+1
		if carDoor2 ==3 and choosenDoor2==2:
			loosingDoor = 1 
			choosenDoor2 = 3
			numberOfWins2  = numberOfWins2+1
		if carDoor2 ==1 and choosenDoor2==3:  
			loosingDoor = 2
			choosenDoor2 = 1
			numberOfWins2  = numberOfWins2+1
		if carDoor2 ==3 and choosenDoor2==1: 
			loosingDoor = 1
			choosenDoor2 = 3
			numberOfWins2  = numberOfWins2+1
		#if player chose the right door initially, he/she looses when changes choice 
		#but probability of this situation is very low as we have only 3 such cases as compared to 6 above
		if carDoor2 ==1 and choosenDoor2==1: 
			loosingDoor = 2
			choosenDoor2 = 3
		if carDoor2 ==2 and choosenDoor2==2: 
			loosingDoor = 3
			choosenDoor2 = 1
		if carDoor2 ==3 and choosenDoor2==3:
			loosingDoor = 1
			choosenDoor2 = 2
		i=i+1
	print ("Number of wins(when the door is changed): " + str(numberOfWins2))
	percentageOfWin2 = (numberOfWins2/100000.0)*100
	print ("Percentage of wins: " + str(percentageOfWin2) + "%")

simulation()
simulation2()
