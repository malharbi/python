import urllib.request
import json
from pprint import pprint

search=input("Plase enter the code name for any country you want to know its name and capital : ")
count=0
page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/co")
content = page.read()
content_string = content.decode("utf-8")

json_data=json.loads(content_string)

pprint(json_data)

for valueN in json_data.items():
    if search in valueN:
        name=json_data["name"]
        capital=json_data["capital"]
        count=1

if count == 1:
    print("The name:",name,"...", "The capital:", capital)
else :
    print("\n The code Not found !!!")
    
