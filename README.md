def bunnyEars2(x, y=0):
        if x!=0:
                if (x%2 ==1):
                        y=y+2
                else:
                        y=y+3
        else:
                x=y
        print("bunnyEars2(",x,")-->",y)
        bunnyEars2(x+1,y)
        
bunnyEars2(0)
