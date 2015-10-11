import pickle
import shelve

def pickleWrite( name , age , place):
    inf={}
    inf['Name']=name
    inf['Age']=age
    inf['Country']=place
    writting = open("motaz.txt", "wb")
    pickle.dump(inf, writting)
    writting.close()

def pickleRead():
    reading = open("motaz.txt", "rb")
    inf= pickle.load(reading)
    print("-----------------------\n","Printing from Pickle way ..\n", inf)
    reading.close()

def shelveWrint(name , age , place):
    writting = shelve.open("example.txt")
    writting['Name']=name
    writting['Age']=age
    writting['Country']=place
    writting.close()

def shelveReading():
    reading = shelve.open("example.txt")
    print("-----------------------\n","Printing from shelve way ...")
    for i in reading.keys():
        print(i ,":", reading[i])
    reading.close()

name=input("what is your name ?")
age=input("How old are you ?")
country= input("Where are you from ?")

pickleWrite(name, age, country)
pickleRead()
shelveWrint(name , age , country)
shelveReading()
