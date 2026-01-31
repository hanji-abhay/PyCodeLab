a =  '''I am learning python'''
i = input("enter string you want to find : \n")
if i in a:
  print(a.index(i))
else:
  print("not found")
