# Function

# Basic function
def func1():
    print("I am a function")

# func1()
# print(func1()) # The output for this will be none why because, The function is not having the return value

# error
# print(func1) 

#Function with arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

func2(10, 20)
print(func2(10, 20)) # The output for this will be none why because, The function not having the return value

#Function that return a value
def cube(x):
    return x * x * x
    
cube(3)
print(cube(3)) # This will print the correct output because its having the return value.


#Function with default value for an argument.

def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result    

print(power(2))
print(power(2, 3))

print(power(x=3, num=2))



#Function with variable number of arguments
def multi_add(*args): # * denotes to varible number of arguments. we can give so many arguments for this function 
    result = 0
    for x in args:
        result = result + x
    return result    

print(multi_add(4,5,10,4,10))