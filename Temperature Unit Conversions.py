class Unit_Conversions():
    def Temperature_Conversion_Logic():
        User_Input = (input('F for Farenheit or C for Celcius: '))
        while User_Input != 'F' and User_Input != 'f' and User_Input !='C' and User_Input != 'c':
            User_Input = input("please enter F or C: ")

        if User_Input == 'F' or User_Input == 'f':
            F = float(input("Enter Temperature in Farenhiet: "))
            New_TempC = (F - 32) // 1.8
            print("The written Temperature in Celcius is ", New_TempC)

        if User_Input == 'C' or User_Input == 'c':
            C = float(input("Enter Temperature in Celcius: "))
            New_TempF = (C * 1.8) + 32
            print("The written Temperature in Farenhiet is ", New_TempF)

        

    def Weight_Conversion_Logic():
        User_Input = (input('P for Pounds or K for Kilograms: '))
        while User_Input != 'P' and User_Input != 'p' and User_Input !='k' and User_Input != 'K':
            User_Input = input("please enter P or K: ")

        if User_Input == 'P' or User_Input == 'p':
            P = float(input("Enter Weight in Pounds: "))
            New_WeightK = P // 2.2
            print("The written Weight in Kilograms is ", New_WeightK)

        if User_Input == 'K' or User_Input == 'k':
            K = float(input("Enter Temperature in Kilograms: "))
            New_WeightP = K * 2.2
            print("The written Weight in Pounds is ", New_WeightP)


# Unit_Conversions.Temperature_Conversion_Logic()
# Unit_Conversions.Weight_Conversion_Logic()
