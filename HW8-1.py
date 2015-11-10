class Animal:
        animal={"elephant":["I have exceptional memory","I am the largest land-living mammal in the world","I have long curved tusks, and massive ears"],
                "tiger":["I am the biggest cat","I come in black and white or orange and black","I'm a solitary animals"],                          "bat":["I use echo-location","I can fly","I see well in dark"]}

        def __init__(self, name):
                self.name=name

        def guess_who_am_i(self):
                print("****************************\n")
                print("I will give you 3 hints, guess what animl I am\n")
                tries=0
                for tries in range(4):
                        if tries < 3 :
                                 print(Animal.animal[self.name][tries])
                                 guess=input("WHo am I?:").lower()
                                 if guess == self.name:
                                         print("You got it! I am "+self.name)
                                         break
                                 else:
                                        print("Nope, try again!")
                        else:
                                print("I'm out of hints! The answer is:"+self.name +"\n")
                                break
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
