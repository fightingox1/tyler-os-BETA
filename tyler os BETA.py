b5 = "password"
import datetime
import random
num = random.randint(1, 10)
c1 = "user"
a2 = "y"
while a2 == "y" :
    c = "y"
    print("hello")
    print(c1) 

    a = input("password to start program-") 
    if a == "b5" :
        print("correct password starting program")
        b = input("go to application menu (Y/N)")
    if b == "y" :
        print("systems ready for use")
        c = "n"

    while c == "n":
        z = input("calculator=1 clock=2 guess the number=3 settings=4 logout=5")

                                
        if z == "3" :
            d = input("guess a number between one and ten")
            if d == "num" :
                print("YOU WIN!")
            else:
                print("try again") 
            

                                          
        if z == "4" :
            c = "y"
            a1 = input("username=1 log out=2 empty=3")
            if a1 == "1" :
             c1 = input("change username")
             a2 = input("go home? (Y/N)")
        if a1 == "3" :
            b5 = input("new password") 
            z = "4"
        if a1 == "2" :
            z = "5"
             
             
            
            
            c = input                                        
        if z == "5" :
            c = "y"
            a2 = "y" 

        if z == "2" :
            import datetime
            time = datetime.datetime.now()
            print(str(time))
            e1 = input(" type y to get the home page menu")
            print("type n to go to home page")

        if z == "1" :
            print("started calculator") 
            print("adding=+ subtracting=- dividing=/ multiplying=x")
            A = int(input("a number-"))
            integer = input("type of math-")
            B = int(input("another number-")) 

            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)
            f = input("Reset? (y/n)")
            if f == "y" :
                A = int(input("a number-"))
                integer = input("type of math-")
                B = int(input("another number-")) 





            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)
                f = input("Reset? (y/n)")
            if f == "y" :
                A = int(input("a number-"))
                integer = input("type of math-")
                B = int(input("another number-")) 





            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)
            f = input("Reset? (y/n)")
            if f == "y" :
                print("adding=+ subtracting=- dividing=/ multiplying=x")
                A = int(input("a number-"))
                integer = input("type of math-")
                B = int(input("another number-")) 





            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)

            f = input("Reset? (y/n)")
            if f == "y" :
                A = int(input("a number-"))
            integer = input("type of math-")
            B = int(input("another number-")) 





            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)
                f = input("Reset? (y/n)")
            if f == "y" :
                A = int(input("a number-"))
            integer = input("type of math-")
            B = int(input("another number-")) 





            if integer == "x" :
                print(A * B)
            if integer == "+" :
                print(A + B)
            if integer == "-" :
                print(A - B)
            if integer == "/" :
                print(A / B)
                e1 = "y"

if e1 == "y":
    e1 = "b"
    print("type n to go home")
    c = input("go home?")
else:
	print("Incorrect password")
