def even_odd():
    a = [1,2,3,4,5,6,7,8]
    even  = [i for i in a if i%2==0]
    odd = [i for i in a if i%2!=0]
    print("even numbers list:", even)
    print("odd number list:", odd)
    print("\n")
even_odd()
