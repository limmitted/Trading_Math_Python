# This program checks your trading skills
# importing the random module
import random
grade = 0
print("Trading")
print("Solve as many Exericses as possible in 3 minutes")
import time
start_time = time.time()



def my_function(score):
	score=0
#Exercise Type 1
	x=random.randint(100,1000)
	y=random.randint(0,200)
	z =(x+y)
	print( str(x)+ '+'+ str(y)+'=')
	#print(str(z))
	input1 =int( input())
	if input1 == z:
    		print("correct");score=score+1		
	else:
    		print("false")
#Exercise Type 2
	x=random.randint(200,1000)
	y=random.randint(0,200)
	z =(x-y)
	print( str(x)+ '-'+ str(y)+'=')
	#print(str(z))
	input1 =int( input())
	if input1 == z:
    		print("correct");score=score+1		
	else:
    		print("false")

#Exercise Type 3
	x=random.randint(0,20)
	y=random.randint(0,20)
	z =(x*y)
	print( str(x)+ '*'+ str(y)+'=')
	#print(str(z))
	input1 =int( input())
	if input1 == z:
    		print("correct");score=score+1		
	else:
    		print("false")

#Exercise Type 4
	w=random.randint(10,20)
	x=random.randint(1,100)*w
	z =(x/w)
	print( str(x)+ '/'+ str(w)+'=')
	#print(str(z))
	input1 =int( input())
	if input1 == z:
    		print("correct");score=score+1		
	else:
    		print("false")

#Exercise Type 5
	x=random.randint(11,20)
	y=random.randint(11,20)
	z =(x*y)
	print( str(x)+ '*'+ str(y)+'=')
	#print(str(z))
	input1 =int( input())
	if input1 == z:
    		print("correct");score=score+1		
	else:
    		print("false")
	return score

amount =5
percent=0
for x in range(amount):
	 percent = percent + my_function(percent)
	 time_ = time.time() - start_time
	 #print(time_)
	 #print(percent)
	 if time_>300:
    		break; print("Time is up")
		
		
percent = percent/(amount*5)
print("You scored "+ str(percent*100)+"%")

if percent > 0.8:
    print("Great job!")
elif percent > 0.5:
    print("Try more, you could do better.")
else:
    print("You should practise much more.")

