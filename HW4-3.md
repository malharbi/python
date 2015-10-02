import pickle
import shelve
from datetime import datetime

def dicWrite( name , age , place):
    dt1 = datetime.now()
    inf={}
    inf['Name']=name
    inf['Age']=age
    inf['Country']=place
    dicRead(inf)
    dt2= datetime.now()
    print("Execution time for Dictionary:", dt2-dt1)

def dicRead(dic):
    print("-----------------------\n", dic.items())

def shelveWrint(name , age , place):
    dt1 = datetime.now()
    writting = shelve.open("example.txt")
    writting['Name']=name
    writting['Age']=age
    writting['Country']=place
    writting.close()
    shelveReading()
    dt2= datetime.now()
    print("Execution time for Shelve :", dt2-dt1)
    
def shelveReading():
    reading = shelve.open("example.txt")
    print("-----------------------\n")
    for i in reading.keys():
        print(i ,":", reading[i])
    reading.close()

name=input("what is your name ?")
age=input("How old are you ?")
country= input("Where are you from ?")
dicWrite(name, age, country)
shelveWrint(name , age , country)

'''
----------------------- output--------------------------------
what is your name ?motaz
How old are you ?120
Where are you from ?makkah
-----------------------
 dict_items([('Age', '120'), ('Name', 'motaz'), ('Country', 'makkah')])
Execution time for Dictionary: 0:00:00.137963
-----------------------

Country : makkah
Name : motaz
Age : 120
Execution time for Shelve : 0:00:00.435297
----------------------------end----------------------------------
'''
