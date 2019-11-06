input("Enter First Name: ")
input("Enter Last Name: ")
int(input("Enter ID Number: "))
numberList = []
total = 0
for x in range(0,20):
    number = float(input("Enter a number: "))
    numberList.append(number)
    total = total + number
print(number)
print("Sum of the list is: "+str(total))
average = total / len(numberList)                
print("The average of the numbers given is: "+str(average))             
   
