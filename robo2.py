
import random
import pyttsx3

random_number=random.randint(1,50) # random number generator

# robo speaking code
def robo(message):   
    print(message)
    speak = pyttsx3.init() # initialize here robo speaker
    speak.setProperty('rate',150) # tlaking speed of robo 
    speak.say(message)  
    speak.runAndWait()

robo("This is, guess correct number game ") # calling robo function

def random():
    count = 0
    robo("please enter the number ") 
    while True:
        number = int(input()) # taking input again and again 
        count=count+1
        if(number>random_number):
            lower= f"please choose lower number"
            robo(lower)    
        elif(number<random_number):
            higher=f"please choose higher number"
            robo(higher) 
        else:
            m1 = f"congratulation you have guess correct number : {random_number}\n attempt take to guess is :{count}"
            robo(m1) 
            break
    

random() 
            
        


