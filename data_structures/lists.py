# data structure provided in python : - 1. list[], 2. tuple(), 3. dictionary {:}, 4. set{}

# a. list : - ordered, changeable, allows duplicate members
# Methods used in list:- 1. append  2. len() 3. copy() 4. count() 5. insert() 6. pop() 7. remove() 8. del 9. index() 10. Sort() 11. reverse()
#working with list
x= [1,2,3.14,"Ram"]   #created list
print(x)              #printed list
print(type(x))        
print(x[0])           #printing different values on different index number of a list
print(x[0:3])         #printing different values on different index number of a list
print(x[ :3])         #printing different values on different index number of a list
print(x[0: ])         #printing different values on different index number of a list

#list with if_else and loop
name= ["Abhay","Kartick",]
print("Enter name")
n = input()
if n in name:
  print("Name already exists")
else:
  print("doesn't exist")
data = [1,2,3,4,3.11,"Abhay"]
for i in data:
    print(i)

#list with loop
x = [2,4,5,6,7]
sum = 0
for i in x:
 sum = sum + i
print(sum)

#to print reverse list items
x=[1,2,3]
print(x[-1])   

#1. append  

x=[1,2,]
l= len(x)
if l>=5:
 print("List is full")
else:
 n= eval(input("Enter number to add in list: "))
 x.append(n)
 print(x)

 #2.len()
 x = [1,2,3,4]
 l = len(x)
 print(l)

#3. copy()
x=[3,1,4,2]
c=x.copy()
print("Original list:",x)
print("Copied list:",c)

#4. count()
x=[1,2,3,2,4,2]
a= x.count(2)
print("Count of 2 is:",a)

#5. insert()
x=[1,2,4,2,3,4,5]
print("Enter index no.")
i= int(input())
print("Enter value to insert:")
d= eval(input())
if x[i]==d:
  print("Data already exists")
else:
  x.insert(i,d)
print(x)

#6. pop()
x=[1,2,3,4,5]
p = x.pop(1)
print(p)
print(x)

#7. remove
x=[3,1,4,2,5,7,8]
x.remove(4)
print(x)

#8. del
x=[5,2,8,1,4]
del x
print(x)

#9. index()
x=[1,2,3,4,5]
i= x.index(4)
print("Index of 4 is:",i)

#10. sor()
x=[5,2,8,1,4]
x.sort()
print(x)

#11. reverse()
x=[1,2,3,4,5]
x.reverse()
print(x)

