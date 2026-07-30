#-----------------------------------------------------taking inputs from user
num1=float(input("Enter the First Number :  "))
num2=float(input("Enter the Second Number :  "))

print("-------------------------Operations-------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Exponention")
print("------------------------------------------------------------------")

#------------------------------------------------------entering the choice corresponding to operation to be done
x=int(input("Enter the choice: "))
print("------------------------------------------------------------------")

#------------------------------------------------------doing calculations and printing output using operators and control structures
if x==1:
    print("Addition :",num1,"+",num2,"=",num1+num2)
elif x==2:
    print("Subtraction :",num1,"-",num2,"=",num1-num2)
elif x==3:
    print("Multiplication :",num1,"*",num2,"=",num1*num2)
elif x==4:
    print("Division :",num1,"/",num2,"=",num1/num2)
elif x==5:
    print("Modulus :",num1,"%",num2,"=",num1%num2)
elif x==6:
    print("Floor Division :",num1,"//",num2,"=",num1//num2)
elif x==7:
    print("Exponention :",num1,"**",num2,"=",num1**num2)
else:
    print("Invalid choice")
print("------------------------------------------------------------------")





#-----------------------------------------Task 2-----------------------------------------------------------------------------------------------


#--------------------------------------------------------taking input
n = int(input("Enter number of rows needed: "))

for i in range(1, n + 1):        #-----------------------rows
    for j in range(i, 0, -1):    #-----------------------values in each rows

        print(j, end=" ")

    print('\n')                  
