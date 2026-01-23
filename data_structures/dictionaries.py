# Dictionary:- multiple values are stored in it for single person in one variable., (values are stored in key pair)
#needed info:- keys, info by user:- value
#functions used in dictionary:- 1. get(), 2.key(), 3.values(), 4.update(), 5. popitem(), 6.pop(), 7. len(), 8. clear(), 9. items(), 10. copy()

record = { "Name": "Abhay" ,"Phone": 1234,"Marks": 69.08}
print(record)
print(type(record))
print(record["Name"])
print("enter name")
user=eval(input())
record["Name"]= user
print("Updated name value is:", record)

# A value of a key in dictionary can be data structure too

x= {"Names": ["Abhay", "Bharti"], "Marks": [69.08, 65] }
print(x)

#1.get()

record={"Name": "Abhay", "Phone no.": 1234}
g= record.get("Name")
print(g)
data={"Name": "Abhay", "Phone no": 12345}
print("Enter the key you want to find value of")
user=input()
if user in data:
    g=data.get(user)
    print("Value of the given key is:", g)
else:
    print("key not found") 

#2.key()

record ={"Name": "Abhay", "City": "Ghaziabad"}
k= record.keys()
print(k)

#3. values()

record={"Name": "Abhay", "City": "Ghaziabad"}
v=record.values()
print(v)

#4.update (static value)

record= {"Name": "Abhay", "Phone no": 7065667480}
record.update({"City": "Ghaziabad"})
print(record)

#dynamic value

record={"Name": "Abhay", "Phone no":7065667480 }
print("Previous Dictionary is", record)
print("Enter key & value")
k=eval(input())
v=eval(input())
record.update({k:v})
print("Updated dictionary", record)

#5.popitem

record={"Name": "Abhay", "Phone no": 7065667480}
p= record.popitem()
print("New dictionary")
print(record)
print("Popped item")
print(p)

#6.pop()

record={"name":"abhay", "city":"ghaziabad"}
p= record.pop("name")
print("Updated dictionary:", record)
print("Popped key:", p)

#7. len()

record= {"name": "abhay", "city": "ghaziabad"}
l = len(record)
print(l)

#8. clear()

record ={"name":"abhay", "city": "ghaziabad"}
record.clear()
print(record)
x={"name": "abhay"}
print("Press 1 to clear the data from the dictionary")
user=input()
if x =={}:
    print("Dictionary is already empty")
else:
    x.clear()
    print("dictionary cleared", x)

#9. items()

x={"name": "abhay", "city": "ghaziabd"}
i= x.items()    
print(i)

#10. copy()

x={"name": "abhay", "city": "ghaziabad"}
c = x.copy()
print(c)
print(x)