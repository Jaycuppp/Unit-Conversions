
User_Input = (input('F or C: '))

def Temperature_Conversion_Calculator():
    if User_Input == 'F':
        F = float(input("Enter Temperature in Farenhiet: "))
        New_TempF = (F - 32) // 1.8
        print ("The current Temperature in Celcius is ", New_TempF)

    elif User_Input == 'C':
        C = float(input("Enter Temperature in Celcius: "))
        New_TempC = (C * 1.8) + 32
        print("The current Temperature in Celcius is ", New_TempC)
        
    else:
        while User_Input != 'F' or User_Input !='C':
             print("Please enter 'F' or 'C' ")
             break

Temperature_Conversion_Calculator()
