
def calculate_average(marks):#-----------------------------Calculating average of marks entered
    sum=0
    for i in marks:
        sum=sum+i
    avg=sum/len(marks)
    return(avg)#-------------------------------------------Returning value of average of marks to main function

def get_grade(average):#-----------------------------------Checking the Grade as per Average
    if average>=90:#---------------------------------------Assigning value to grade as per the average using if-elif-else statements
        grade="A"
    elif average>=80:
        grade="B"
    elif average>=70:
        grade="C"
    elif average>=60:
        grade="D"
    elif average<60:
        grade="F"
    return(grade)#-----------------------------------------Returning value of grade to main function


def main():
    print("*******************************")
    marks_five=input("Enter marks for 5 subjects: ")
                            #------------------------------Taking input marks of 5 subjects

    marks_list = marks_five.split(",")#--------------------Spltiing values based on ','


    int_list = []#-----------------------------------------New list to append items after changing their type from 'str' to 'int'
    for m in marks_list:
        int_list.append(int(m))#---------------------------Type changing


    mark=[]#-----------------------------------------------Checking the marks entered are valid or not
    if len(int_list)==5:
        for i in int_list:
            if i>0 and i<=100 :
                mark.append(i)
            elif i==0 or i<0 or i>100:
                print("Mark entered is NOT VALID!!!!!!Please check the Marks again")
                exit()
            else:
                exit()
    else:
        print("Check the number of Marks entered!!!!!!!!!!!!!")
        exit()
                    #--------------------------------------Calling functions to calculate values of avg and grade
    avg=calculate_average(mark)
    grade=get_grade(avg)
                    #--------------------------------------Printing average and Grade
    print("*******************************")
    print("Average Marks : ",avg)
    print("Grade : ",grade)
    print("*******************************")



main()                        #---------------------------Calling main function to run the program as per need
