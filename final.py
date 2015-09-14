import sys

#this is our dictionary that we will use for our map
#this it shows each node and then an inner key that shows all of the connecting nodes
# I learned this code from https://docs.python.org/2/tutorial/datastructures.html
g = {'Elevator': {'3050':10,'3020':10},
             '3050': {'3070':10,'Elevator':10,'3100':15},
             '3070': {'3050':10,'3075':10},
             '3075': {'3070':10,'3080':10},
             '3080': {'3075':10,'3090':10},
             '3090': {'3080':10,'3100':10},
             '3100': {'3090':10,'3005':10,'3050':15},
             '3005': {'3100':10,'3010':10},
             '3010': {'3005':10,'3015':10},
             '3015': {'3010':10,'3020':10},
             '3020': {'3015':10,'Elevator':10}}
             
    
             
#start user interface is here
print "\n"
print 'Welcome to Find Your Way => Version LWH'
print "\n"
print 'here is a list of possible rooms to choose from:'
print "\n"
print '=>Elevator \n=>3050 \n=>3070 \n=>3075 \n=>3080 \n=>3090 \n=>3100 \n=>3005 \n=>3010 \n=>3015 \n=>3020'
print "\n"
print'Please be sure to enter the EXACT string that is listed without the (=>), thanks'
start = input('Enter the location where you are staying: ')
print "\n"
finish = input('Thank you, now please enter your destination: ')
print "\n"


cost = 10000000000000
shortestTemp = 0
shortestTempRoute = []
shortestRoute = []
currentIteration = 0
beginning = ' '
anotherTemp = []
anotherArray = []
keys = []
currentArray = []

def shortest(start, finish, array):
	global currentIteration
	global anotherArray
	global currentArray
	global shortestTempRoute           
	global shortestRoute       
	global shortestTemp        
	global cost
	global g 
	global anotherTemp
	global beginning
	global keys
	keys.append(start)
	now = 1
    
    #this makes sure that current iteration is set to zero when the recursion call is made
    #resets the start value
	if currentIteration == 0:
    		beginning = start
    		shortestTempRoute.append(beginning)
    
   
	#Goes through all of the values in the Dict and compares the shortest path.
	#The value is that actual cost located on the edges of the graph
	thisTotal = 0
	for key, value in array.iteritems():
    		currentIteration = currentIteration+1
    	
    		
    		#still adds the key to the shortest route when key = end or beginning 
    		#Here is the start of our search algorithm 
    		if key == finish or key == beginning:
    			shortestTempRoute.append(key)
    			shortestTemp = shortestTemp + value
    		
    			
    			#Compares Values so that we will find the shortest cost
    			#cost is set to infinity
    			#This is an ending if statement that works if goal is reached 
    			if shortestTemp < cost:
    				cost = shortestTemp
    				shortestRoute.append(shortestTempRoute)
    			shortestTempRoute.remove(key)
    			
    			
    		#If key does not equal to start or finish this else will be executed
    		
    		else:
    			shortestTempRoute.append(key)
    			shortestTemp = shortestTemp + value
    			currentArray = []
    			currentArray = g[key]
    			del currentArray[start]
    			if (beginning in currentArray or finish in currentArray) and len(currentArray) == 1:
    				shortestTempRoute.remove(key)
    			shortest(key,finish,currentArray)
    			
		
shortest( str(start), str(finish), g[str(start)])
#shortest( '3020', '3090', g['3020'])
print cost
print shortestRoute
