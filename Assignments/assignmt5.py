
##-----------------T A S K - 1--------------Even Numbers, Greetings------------------------------------------------------

## generator function to find n even numbers starting 2
def even_numbers(n):
    for i in range(2,n):
        if i%2==0:
            yield(i)

num=even_numbers(30)##---------------------n=30,starting from 2 to n
for i in num:
    print(i)

##decorator greet that prints Hello! before executing a function
def my_decorator(func):
    def inner():
        print("Hello!",end=" ")##-------------adding a decorator text before execution of main function
        result=func()##-----------------------passing value of main function into result
        return result
    return inner
@my_decorator##-------------------------------applying a decorator to main function
def display_hello():
    return "My name is Alice"
print(display_hello())


##-----------------T A S K - 2-------------Text Analyzer-------------------------------------------------------

##------------------------------------------------------------finding email addresses in  text
import re
text="Email me at monica123@gmail.com or monica222@gmail.com"
pattern=r"[a-z][a-zA-Z0-9$#%^!&*()-+]+\@[a-z]+\.[a-z]+"
print(re.findall(pattern,text))

##------------------------------------------------------------finding phone numbers in text
import re
text = "Call me at (123) 456-7890 or 987-654-3210."
pattern=r"[0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4}"
print(re.findall(pattern,text))

##------------------------------------------------------------replacing words in text
import re
text="I love Python programming"
pattern="Python"
print(re.sub(pattern,"Java",text))