#basic print statement for Hello World Check!
print("Vinayaka")

#Data types - float,int,boolean,str.
print(type(5.5))
print(type(1))
print(type(True))
print(type("Keerthana"))
print(len("Kalpana"))
print(type([1,2,3,4,5]))
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(False or True)

#List and indexing in Python : Indexing starts from 0.
list2 = [1,2,3,4,5]
print(len(list2))
list2.append(6)
print(list2)
print(list2[0])
print(list2[:])
print(list2[1:])
print(list2[1:3])
list2.insert(0,8)
print(list2)
list2.extend([7,9])
print(list2)
print(sum(list2))
print(list2.pop(0))
print(list2)
list2.insert(9,1)
print(list2)
print(list2.count(1))
print(min(list2))
print(max(list2))
print(list2*2)

#Set{} and operations - A collection of data items with unqiue elements, cannot perform indexing.
set_1 = {1,1,2,3,3,4}
print(set_1)
set_1.add(5)
print(set_1)
set_2 = {3,3,4,5,6,6}
set_diff = set_1.difference(set_2)
print(set_diff)
set_intersection = set_1.intersection(set_2)
print(set_intersection)

#Dictionaries{} - A key value pair that unique elements.
my_dict = {"Car1":"Audi","Car2":"Benz"}
print(my_dict["Car1"])

#Tuple() - An immutable data structure that stores duplicate values.
tuple = (1,1,2,3,3,4)
print(tuple)
print(tuple.count(1))

#Numpy - An open source Python library that supports mathematical operations.
import numpy as np
a=np.array([1,2,3,4])
print(a)
a[2:] = 100
print(a)
b = np.random.randn(4,4)
print(b)
c = np.random.randint(0,100,8).reshape(4,2)
print(c)

arr = np.array([11,12,13,14]) #Creating arrays
print(arr)

arr_zeros = np.zeros(2) #creates a new array filled with zeros
print(arr_zeros)

arr_ones = np.ones(2)#creates a new array filled with ones
print(arr_ones) 

arr_arange = np.arange(2,12,1) #start,stop,step of arange function gives values at mentioned regular intervals
print(arr_arange)

arr_linspace = np.linspace(1,10,100) #it gives no.of values mentioned to display from start,stop, count of values
print(arr_linspace)

#array properties
array = np.array([[1,2,3],[4,5,6]])
print(array.shape)
print(array.ndim)
print(array.size)
print(array.dtype)

#reshaping and flattening
reshape = np.arange(12).reshape(3,4)
print(reshape)
flat = reshape.flatten()
print(flat)
trans = reshape.T
print(trans)

#indexing and slicing
index = np.array([10,20,30,40,50])
print(index[1:4]) #Slicing
matrix = np.array([[1,2],[3,4],[5,6]])
print(matrix)
print(matrix[:1]) #column
print(index > 25) # Boolean indexing
print(index[[0,2,4]])

#math operations
a1 = np.array([1,2,3])
b1 = np.array([4,5,6])
print(a1 + b1)
print(a1 * b1)
print(np.dot(a1,b1)) #performs a dot product between a1 and b1 arrays
print(np.sum(a1))
print(np.mean(a1))

#broadcasting
a2 = np.array([[1,2,3],[4,5,6]])
b2 = np.array([1,0,1]) #NumPy is broadcasting the smaller array (b2) across the larger array (a2) to make the shapes compatible — just like a radio broadcast goes out to fill a wider area.
print(a2 + b2)

#random module
np.random.seed(0) #Without the seed, you’d get different numbers each time as random is a random number generation.
print(np.random.randint(1,6,3)) # this give [5,1,4] values only how ever times we execute the code as it is locked with seed above.
print(np.random.rand(2,3,4))
print(np.random.randn(3)) #gives randomly only mentioned number of values
print(np.random.randint(1,6,size = 5)) # this is same as np.random.randint()
print(np.random.choice([10,20,30],size = 30)) #randomly selects 30 values from the list [10, 20, 30], with replacement, and prints them as a NumPy array.

#aggregation with axis
a3 = np.array([[1,2,3],[4,5,6]])
print(np.sum(a3,axis = 0)) #sums columns
print(np.sum(a3,axis = 1)) #sums rows
print(np.mean(a3,axis = 1)) # gives average of rows
print(np.mean(a3,axis = 0)) #gives average of columns

#logical and comparison
b3 = np.array([[1,2,3],[4,5,6]])
print(np.array(b3 > 3))
print(np.any(b3 > 4)) #just gives true if any one value is > 4 in b3
print(np.all(b3 > 4)) #just gives true if all values are > 4 in b3

#useful utility functions
a5 = np.array([10,20,10,70,60,30,40,50,50,50,40])
print(np.unique(a5))
print(np.sort(a5))
b5 = np.array([1,2,3])
c5 = np.array([4,5,6])
print(np.concatenate((b5,c5))) #concatenate
print(np.stack((b5,c5))) # just stacking 2 diff arrays of b5 and c5 into one single array.
print(np.where(a5>25,"Yes","No"))


#shape and reshape an array
#using .shape keyword to change the dimension of the array.
array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array.shape)
array.shape = (5,2)
print(array)

array_1 = np.array([1,2,3,4,5,6,7,8])
print(array_1.shape)
array_1.shape = (4,2)
print(array_1)

#conditional statments
# 1. if statement : used when test expression is true
a = 10
if a > 0 :
    print("The variable is greater than 0")
a = -10
if a > 0:
    print("The variable is greater than 0")
print("The variable is outside the if statement")
# 2. else statement : used when test expression is false
b = 10
if b>0:
    print("b is greater than 0")
else:
    print("b is less than 0")
# 3. elif statement : used when there is more than 1 test expression
c = 0
if c > 0:
    print("c is greater than 0")
elif c < 0:
    print("c is less than 0")
else :
    print("c is equal to 0") 

# 4. nested if else statement : used when multiple level of logics are to be checked.
# one codintion is put inside another condition 
x = 5
if x > 0:
    print("x is a positive number")
    if x % 2 == 0 :
        print("x is an even number")
    else:
        print("x is an odd number")
else:
    print("x is a negative number")       

#Loops in Python
# 1.while : we can execute a set of statements as long as the condition is true.
n = int(input("Please enter a number : "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print("The sum of first {} natural numbers is {}".format(n,total))

# 2.for : used for iteration over a sequence. i.e either a list, a tuple, a dictionary,a set or a string.
tools = ["Python","SQL","Power BI"]
for x in tools:
    print(x)

# break : used to break the loop. It terminates the current loop
# and resumes the execution at the next statement.
list_1 = ['a','b','c','d','e']
for i in list_1:
    if i == 'b':
        print("i is equal to a")
    break
print("i is not equal to a")

# continue - used in loops. It skips the current iteration and 
# goes to the next one.
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# pass - it's a placeholder. A do-nothing statement, 
# python will run it and move on.
for i in range(1,6):
    if i == 3:
        pass
    print(i)

# function - A reusable block of code that performs a specific task.
# Instead of writing the same code again and again, you define it 
# once and call it whenever you need it.
def greet():
    print("I am greeting")
greet()

# recursion - a function calling by itself to solve a smaller part 
# of a bigger problem.
def sum_recursive(n):
    if n == 1:
        return 1 #base class - check below note
    else :
        return n + sum_recursive(n-1) 
print(sum_recursive(5)) 

#Note - What is a Base Class in Recursion?
#In recursion, the base class is the condition that stops 
# the function from calling itself.
#Think of it like the "exit door" of a recursive loop.
#Without a base case, the recursion would keep going forever, 
# eventually causing a crash (stack overflow).
def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1) #here countdown is function name which is 
        #being called itself again in the def countdown() function - 
        # so this is the sign of a recursion.
countdown(5)
   
# lambda - a quick function with single expression with a syntax of lambda arguments : expression.
def myfunction(n):
    return lambda a: a * n
function_output = myfunction(2)
print(function_output(3))

# map() - A function that is applied to every item in the list.
map_list = [1,2,3,4,5]
double = map(lambda x:x*2,map_list)
print(list(double))

# reduce() - A function that reduces a list to a single value
from functools import reduce
values = [1,2,3,4,5]
single_value = reduce(lambda x,y:x+y,values)
print(single_value)

# sorted() - A function that returns a new sorted list with ascending order by default. Use reverse = True to get descending order.
scores = [98,79,60]
sorted_scores = sorted(scores, reverse = True)
print(sorted_scores)

#filter() - A function that filters the list by keeping only the items that met the condition.
numbers = [1,2,3,4,5,6,7,8,9,10]
filtered = filter(lambda x : x%2 == 0, numbers)
print(list(filtered))

print("\n")
 
#Index of a string : In python, indexing starts at 0
string1 = "Great Learning"
print(string1.index("L"))

#slicing in Python - A way of extracting a specific portion of a sequence like list, string or tuple.
my_list = [1,2,3,4,5]
print(my_list[0:3])
my_str = " Keerthana is Shuddi Ayodhya"
print(my_str[1:10])

#Pandas - A python library used to perform data analysis and manipulation.
#It is used in data cleaning, data filling, data normalization, merging and joining,
#data visualization, statistical analysis, data inspections, loading and saving data.
#Two imp data types of pandas are - series and dataframes.
#series - A 1-D (1 - Dimentionsional) list of values with index.
#dataframe - A 1 or more series (2 - D or multi dimensional).
import pandas as pd
authors = ['a','b','c','d']
sample_series = pd.Series(authors)
print(sample_series)

import matplotlib.pyplot as plt # type: ignore
plt.plot([1,2,3],[4,5,6])
plt.show()

#creating a sample dataframe
authors_list = ['a','b','c','d','e']
novels = [5,9,3,2,4]
authors_series = pd.Series(authors_list)
novels_series = pd.Series(novels)
sample_df = {'Author Name': authors_series,'# Novels Written': novels_series}
result = pd.DataFrame(sample_df)
print(result)

#sample dataframe with random integers
import numpy as np
import pandas as pd
nos = np.random.randint(0,10,size = (5,1))
print(nos)
values = np.random.randint(0,100,size = (10,10))
df = pd.DataFrame(values,columns = list('abcdefghij'))
print(df)

#drop from a dataframe
df.drop(['i','j'],axis = 1, inplace = True)
print(df)

#append to a dataframe
new_row = {'a':5,'b':5,'c':5,'d':5,'e':5,'f':5,'g':5,'h':5}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df)

#class - A class is a blueprint(Ex, a blueprint of house before building)
#A class can have data and functions
#object - An object is a house that is built using the blueprint of a class.
#an object is a real world entity.
#we create or call an object to use the blueprint of a class.
#with help of an object only one can access data and function of a class.

#method - A method is a function that is specifically tied to an object.
#method is associated to an object(dependent)
#method definition always includes 'self' as it's first parameter.

class car:
    def car_method(self):
        print("We are the cars!")
obj_car = car()
obj_car.car_method()

#type casting in python - converts one data type to another.
#implicit type casting - converts the data type automatically
x = 5
y = 10.0
z = x + y
print(z) #here, z is printed as 15.0 automatically
#explicit type casting - manually need to convert the data type using str(),int(),float() etc
x = "10"
y = int(x)
z = 5 + y
print(z) #here, z is printed as 15

a = " I am learning"
b = a.replace("I","We")
print(b)
b = b.replace("am","are")
print(b)

#method over loading : Same method name with different number of parameters.
class Greet:
    def hello(self,name = None):
        if name:
            print(f"Hello,{name}")
        else :
            print("Hello!")
g = Greet()
g.hello()
g.hello("Arun!")           

#method over riding : When a class provides a new version of method is already defined in the parent class.
class Animal():
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self): #overriding the parent method
        print("Bark!")

d = Dog()
d.sound()

#constructor - A special function that is used to initialize an object.
#In Python, a constructor is declared as : __init__()
#A constructor automatically runs when we create an object.
class person():
    def __init__(self,name,age): #constructor
        self.name = name
        self.age = age

p1 = person("Keerthana",25) #creating an object

print(p1.name)
print(p1.age)

#POLYMORPHISM - Implementing same things in different ways. It can be achived by the 
# concepts of method over loading ad method over riding.

#Key understanding and differences on method overloading and method over riding :
#1. Method Over Loading - It is of two types : Operator over loading and method over loading.
# a) Operator Over Loading:'+' symbol is an operator that performs addition(numbers) and 
# concatenation(string).
a = 'Keerthana '
b = 'Singupuram'
print(a+b) #here it concatenates both a and b with + operator as they both belong to string 
#mentioned in single qoutes.

c = 10
d = 20
print(c+d) #here it adds both c and d with + operator as they both belong to int data types(numbers)

# b) Method Over Loading:The method name should be same but the number of aruguments must be different.
class MethodOverLoad():
    def method(self, a = None, b = None): #here we have declared dafault parameters, so that while calling object even if we dont specify arguments, it considers these default parameters.
        print(a,b)
M_obj = MethodOverLoad()
M_obj.method() #as no parameters are given, it takes the default parameters.
M_obj.method(a="Present")
M_obj.method(a='Present',b = 'Absent')  

#2. Method Over Riding : The method name and number of arguments both should be same.
#A method after creating in a base class is over rided by the child class.
class Father():
    def Transportation(self,a):
        print("Cycle")
class Son(Father):
    def Transportation(self,a):#here method name and arguments both are same as base class
        print("Bike")    
obj = Son()
obj.Transportation(a)

#Exception Handling : An exception is an event which occurs during execution of a program
#disrupting the normal flow of a program's instructions.
try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

#The try block runs code that may raise an error.
#The except blocks catch specific errors like ZeroDivisionError, ValueError.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("That's not a valid number!")

except Exception as e:
    print("An unexpected error occurred:", e)

#🔹 1. What is Compilation?
#Compilation means converting human-readable code into machine code (0s and 1s) before execution.
#Languages like Java or C++ use compilers for this process.
#🔹 2. Does Python Compile?
#Python is an interpreted language, but it does a quick compilation to bytecode (not machine code).
#It checks syntax before running the program — this acts like a mini compilation step.
#🔹 3. Compile-Time Error vs Run-Time Error
#Compile-Time Error: Happens before the program runs (e.g., syntax mistakes like missing brackets).
#Run-Time Error: Happens while the program is running (e.g., dividing by zero, using a variable 
#that doesn't exist).
#🔹 4. Error vs Exception in Python
#Error: More serious problems (like syntax or indentation errors) that crash the 
#program before it runs.
#Exception: Unexpected situations during execution (e.g., file not found, index 
#out of range) — which can be handled using try-except.