def for_upp_case():
    a  = input("Enter the string: \n")
    if a.isupper():
        print("Already is in upper case \n")
    else:
        b = a.upper()
        print(b)

def for_low_case():
    a = input("\n Enter the string: \n")
    if a.islower():
        print("Already is in lower case")
    else:
        b = a.lower()
        print(b)

def search():
    a = input("enter the string : \n")
    i = input("enter string you want to find : \n")
    if i in a:
     print(a.index(i))
    else:
     print("not found")
search()
