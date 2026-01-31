#take nothing return nothing
def even_odd():
    a = [1,2,3,4,5,6,7,8]
    even  = [i for i in a if i%2==0]
    odd = [i for i in a if i%2!=0]
    print("even numbers list:", even)
    print("odd number list:", odd)
    print("\n")
even_odd()    

#take nothing return something
def even_odd():
  a = [1,2,3,4,5,6,7,8]
  even  = [i for i in a if i%2==0]
  odd = [i for i in a if i%2!=0]
  return even, odd
k = even_odd()
print(k)
print("\n")

#take something return nothing
def even_odd(a):
  even  = [i for i in a if i%2==0]
  odd = [i for i in a if i%2!=0]
  print("even numbers list:", even)
  print("odd number list:", odd)
  print("\n")
a = [1,2,3,4,5,6,7,8,9]  
even_odd(a)

#take something return something
def even_odd():
  a = [1,2,3,4,5,6,7,8]
  even  = [i for i in a if i%2==0]
  odd = [i for i in a if i%2!=0]
  return even, odd
a = [1,2,3,4,5,6,7,8,9]  
k = even_odd()
print(k)
