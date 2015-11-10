from random import randrange


def division():
    while True:
        num1=randrange(5)
        num2=randrange(5)*num1

        while num1==0:
            num1=randrange(5)
            num2=randrange(5)*num1
        try:
            answre=int(input(str(num2)+"/"+str(num1)+"="))
            if answre == num2//num1 :
                print("CORRECT!")
            else:
                print("INCORRECT1")
        except ValueError:
            print("Pleas enter Integers Only!")
        except SystemExit:
            print("exit process..")
            break

        
print("Well ply Integer Divisions game. Try to solve it. \n Good Luck..\n")
division() 





