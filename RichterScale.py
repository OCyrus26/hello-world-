##print("Welcome to Richter Scale Calculation")
##firstName = input("Enter first name: ")
##lastName = input("Enter last name: ")
##Id = int (input ("Enter your id number: "))
end = False

while (end == False):
    Richter = float (input("Enter the Richter scale value: "))

    if  Richter >= 8:
        print("Most structures fall")
        end = True
    elif  Richter >= 7:
        print("Many buildings destroyed")
        end = True
    elif  Richter >= 6:
        print("Man buildings considerably damaged, some collasped")
        end = True
    elif  Richter >= 4.5:
        print("Damage to poorly constructed buildings")
        end = True
    elif Richter < 4.5 and Richter > 0:
        print("No destruction of buildings")
        end = True
    elif Richter == -99:
        print("End")
        break
    elif Richter < 0 and Richter == -99:
        print("No negative values")
        

    
    


