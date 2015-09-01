name = input("Hi, what is your name?")
print("Hello\t" + name + "\tLet's play game!\n Think of random number from 1 to 100, and I'll try to guess it!")
first, last, cont = 1, 100, 0
avg = (last+first)//2
ask= "yes"
while (ask == "yes"):
    first, last, cont = 1, 100, 0
    avg = (last+first)//2
    ask = input("Do you want to play ?")
    if ask == "yes":
        while (first <= last):
            cont= cont+1
            print("Is it", avg ,"?")
            answre=input("(yes/no)\t")
            if answre == "yes":
                print("Yeey! I got it in" , cont , "tries!")
                break
            
            elif answre == "no":
                print("Is the number larger than" ,avg )
                ans=input("(yes/no)\t")
                if ans == "yes":
                    first = avg
                    avg = (last+first)//2
          
                elif ans == "no": 
                    last = avg
                    avg = (last+first)//2
                    continue
    elif ask == "no":
            break 
    
           
print("Bey-Bey")
