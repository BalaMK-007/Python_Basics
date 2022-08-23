# basic data types

# Numbers

myint = 5
myfloat = 13.2

#Strings
mystr = "This is a string"

#Boolean
mybool = True

#lsit
mylist = [0, 1, "two", 3.2, False]

#tuple
mytuple = (0, 1, 2)

#dict
mydict = {"one" : 1, "Two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

#redirecting
# myint = "abc"
# print(myint)

#to access a member of sequence use []
# print(mylist[2])
# print(mytuple[1])

#use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2])

#use slice to reverse a sequence
# print(mylist[::-1])

#Dictionaries are accessed via keys
# print(mydict["one"])

#Error: Variables of different types cannot be combined so use 'str'.
# print("string type" + str(123))

#Global vs local vaiables in function

#local varibale
def someFunction():
    #To make varibale global use global keyword.
   # global mystr
    mystr = "def"
    print(mystr)

someFunction()

#global variable
print(mystr)