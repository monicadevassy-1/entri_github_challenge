#---assignment 3------

def has_unique_chars(s):#---------------------------function definition

    for i in range(len(s)):#------------------------w             a            a         t                     
        for j in range(i + 1, len(s)):#----------------a a t        a  t         t           


            if s[i] == s[j]:
                return False          
            
    return True       #----------------------------if nothing is same (st[i]!=st[j]), only it returns true


word=input("Enter the word : ")
msg = has_unique_chars(word)#---------------------calling with input,storing into 'msg' variable



if msg==True:
    print(" *********                               *********** ")
    print("            It  has  unique  characters           ")
    print(" *********                               *********** ")
else:
    print(" *********                                         *********** ")
    print("           It  does  not  have  unique  characters")
    print(" *********                                         *********** ")