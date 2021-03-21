print("**********Basic Python Programming*************")

print("this is a commented line in Python")
# this is a commented line in Python
'''This is a
     multiline
     comment.'''

#Python treats single quotes the same as double quotes.
print("Python treats single quotes the same as double quotes.")
x='Inceptez'
y="'Technologies'"
z="Pvt.\nLtd."
print("welcome " + x + y+z)
greet="Welcome to " \
      "Python"
greet1="""Welcome to 
Pyspark"""

print(greet)
print(greet1)

print("Data Types and characteristics")

flt=10.2345
print("The type of variable having value", flt, " is ", type(flt))
isins=isinstance(flt,float)
print(isins)

#strings are immutable

tmpstr = "Test"
#tmpstr[2]='r'

print ("strings are immutable" + tmpstr)

print("String & Num operations")
strdata = "this IS test data"
print("Convert to Upper Case:",strdata.upper())
print("Check upper:",strdata.isupper())
print("Convert to lower Case:",strdata.lower())
print("Check lower:",strdata.islower())
print("Check numeric:",strdata.isnumeric())
print("get no of occurances:",strdata.count("i"))
print("Starts with :",strdata.startswith("t"))
print("Ends with :",strdata.endswith("a"))

num1=100
num2=200
print(num1+num2)

print('Strongly typed')
#num1+str(num2)

print('Dynamic typed')
num1=100
print(num1)
num3=num1 + num2
num1="Inceptez"
print(num1)
#num1+200


print("Conditional Structures")
print("greatest of 3 numbers")
print("enter the input1")
a=int(input())
b=100
c=200

if a == b == c:
    print("all are equal")
elif a > b and a > c:
    print("a is greater..a value is %d :"%a)
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

print("Looping Constructs")
#loops in python

lst = [5,4,2,3,1]

for i in reversed(lst) :
    print(i)

#Nested Loops - A nested loop is a loop inside a loop.
characters = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in characters:
    for y in fruits:
        print(x, y)

# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Inceptez")
print("Loop completed")

#Using else statement with while loops: while loop executes the block until a condition is satisfied.
# When the condition becomes false, the statement immediately after the loop is executed.

# combining else with while
count = 5
while (count > 3):
    count = count - 1
    print("Inside while loop with count"+str(count))
else:
    print("In Else Block")

#Single statement while block
count = 1
while (count == 0): print("Hello Inceptez")


#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("loop with break completed here")

#With the continue statement we can stop the current iteration, and continue with the next:
i = 1
while i < 6:
    #increment operators are not allowed in python i++ or i-- instead we can use i += 1
    i += 1
    if i == 5:
        continue
    print(i)
print("loop with continue completed here")

print("Collections")
print("List")
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lst = [5,4,2,3,1]
print("slicing a list")
print(lst[0:3])
print(lst)
lst2 = [5,4,2,3,1]
print(lst2.clear)
print(lst.reverse())
lst=lst.__add__(weekdays)
print(lst.count(5))
print(len(lst))
print(lst)

print("Tuples")
tup = ('ready', 'fire', 'aim')
print('tuple starts with zero index ' + tup[0])
print(len(tup))

print("Set")
my_set = {1, 3, 5, 1}
print(my_set.__len__());
print(my_set.intersection(my_set))

print("Dictionaries")
my_dict = {'first_name': 'inceptez', 'last_name': 'tech','age': 6}
#Adding Items
my_dict["city"] = "chennai"
my_dict["last_name"] = "technologies"
print(my_dict)
#Removing an Item
my_dict.pop("age")

print(my_dict.keys());
print(my_dict['first_name'] + ' ' + my_dict['last_name'])

for key, value in my_dict.items():
 print('keys')
 print(key)
 print('values')
 print(value)

print("nested list")
e = ["mouse", [8, 4, 6], ['a']]
e1 = e[1][2]
print("E1:",e1)

print("nested tuples")
tup = (['hello','ready'], {'shoot': 'fire'}, ('aim','concentrate','focus'))
print(tup[0][1])
print(tup[1]['shoot'])
print(tup[2][2])