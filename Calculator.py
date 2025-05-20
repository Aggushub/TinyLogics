#Function to add two numbers
def add(x,y):
    return x+y
#Function to subtract two numbers
def sub(x,y):
    return x-y

#Function to multiply two numbers
def mul(x,y):
   return x*y

#Function to divide two numbers
def div(x,y):
    if y == 0:
        return "Error Division by zero is not allowed"
    else:
        return x/y
#Function for main Calculator
def Calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        #Take input from the user
        choice = input("Enter choices (1/2/3/4): ")
        #Where numbers are inputted
        if  choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
	            print(f"{num1} + {num2} = {add(num1,num2)}")
            
            if choice == '2':
        	    print(f"{num1} - {num2} = {sub(num1,num2)}")
            
            if choice == '3':
            	print(f"{num1} x {num2} = {mul(num1,num2)}")
            
            if choice == '4':
            	print(f"{num1} / {num2} = {div(num1,num2)}")
            #Option to exit the loop
        next_calculation = input("Do you want to continue doing calculations? (yes/no):")
        if next_calculation.lower() != 'yes':
            break
    print("Exiting Calculator. Goodbye")
#Call the calculator function
Calculator()
            
