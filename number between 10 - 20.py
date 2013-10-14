#number between 10 - 20

number = int(input("Please enter a number: ")) 
while not number in range(10,20):
    number = int(input("Please try again, enter another number: "))
    if number in range(10,20):
        print("That is within range.")
        
    
    



    
