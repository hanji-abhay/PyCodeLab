a = "I am learning c++"
b = a.replace("c++", "Python")
print(b)

def replace_word():
    a= input("Enter a string : \n")
    b = input("\n Enter the word you want to replace : \n")
    if b in a :
        c = input("\n Enter the word you want to replace the word with : \n ")
        print(a.replace(b,c))
    else:
        print("Didn't find the string")
replace_word()

a = "I am learning c++, c++ is a good language. But I left c++"
b = a.count("c++")
print(b)

string = input("Enter the string  : \n")
find =  input("\n Enter the word you want to count  : \n")
if find in string:
    print("\n The count of the word is : ", string.count(find))
else:
    print("The word is not in the string")
