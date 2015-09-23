# python
def count_frequency(myList):
    d={}
    for word in myList:
        count=0
        for item in myList:
            found =word.find(item)
            if found >=0:
                count+=1
                d.update({word:count})
        ourlist=d.items()
    return ourlist

myList=["one","two","eleven","one","three","two","eleven","three","seven","eleven"]

print(count_frequency(myList))
