

class BankAccount:
    def __init__(self,name,available_balance):
        self.name=name
        self.balance=available_balance#---------------------constructor,initialize 'balance' with 'available balance'

    def depositing_money(self,amount):#---------------------method to calculate 'balance' after depositing

        if amount>0:
            self.balance+=amount
            print("Amount is Deposited")
            x=input("Do you want to check the  Balance ? (Yes/No)")
            if x=='Yes' or x=='yes':
                self.display_balance()
            else:
                exit()
        else:
            print("Please enter  a Valid Amount  ,Thankyou!!")
            pass


    def withdrawing_money(self,amount):#---------------------method to calculate 'balance' after withdrawal
    
        if amount<=self.balance:
            self.balance-=amount
            print("Amount have been Withdrawn")
            x=input("Do you want to check the  Balance ? (Yes/No)")
            if x=='Yes' or x=='yes':
                self.display_balance()
            else:
                exit()
        else:
            print("Insufficient Balance !!!!")

                

    def display_balance(self):#--------------------------------method to display current 'balance'
        print("Account Holder:", self.name)
        print("Your current Account Balance is",self.balance)


#  main program

# Taking input from user
name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))
if balance<0:
    balance=0#-------------------------------------------------setting minimum balance


#creating account
account1=BankAccount(name,balance)#------------------------------------object created for class 'BankAccount'

#transactions
while True:#-----------------------------------------------------looping with 'while' until exiting

    print("\n*************** Welcome to The Bank **************** ")
    print("\n ***************Transactions****************")
    print("\n*  1. Deposit          *\n*  2. Withdraw         *\n*  3. Display Balance  *\n*  4. Exit             *")
    ch = int(input("\nPlease enter the number of your Choice : "))#------------inputting the choice
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")

    if ch==1:
        amount=float(input("Enter the Amount to Deposit : "))
        account1.depositing_money(amount)#-----------------------calling method for depositing_money
    elif ch==2:
        amount=float(input("Enter the Amount to Withdraw : "))
        account1.withdrawing_money(amount)#----------------------calling method for withdrawing money
    elif ch==3:
        account1.display_balance()#------------------------------calling method for displaying balance
    elif ch==4:
        print("Thankyou !!")
        exit()#--------------------------------------------------exiting from the program
    else:
        print("Please  enter a Valid option!!!!")




