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

#len() function returns the length of the object. This function internally calls __len__() function of the object. So we can use len() function with any object that defines __len__() function.
print("Length of the sequence " + str(len(strdata)))

num1=100
num2=200
print(num1+num2)

print('Dynamic typed')
num1=100
num2=200
print(num1)
print(isinstance(num1,int))
num3=num1 + num2
num1="Inceptez" #dynamically typed
print(num1.isnumeric())
print(num1)

print('Strongly typed')
#num3=num1 + num2 #strongly typed

print("Conditional Structures")
print("greatest of 3 numbers")
print("enter the input1")
a=int(input())
b=100
c=200

if a == b == c:
    print("all are equal")
elif a > b or a > c:
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
#Do While is not available in Python and below code is the equivalent
i = 3
while True:
    print(i)
    if i <= 3:
        break
    i -= 1
print("Do while example loop with break completed here")

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

print("List Operations")
lst2 = ['a','e','x','o','u']
#The remove() method removes the first matching element (which is passed as an argument) from the list.
lst2.remove('x')
print(lst2)
lst2.insert(2,'i')
print(lst2)
#simply update
lst2[2]='i'
print(lst2)
lst2.reverse()
print(lst2)
lst2.clear()
print(lst2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lst = [5,4,2,3,1]
print(lst)
print("slicing a list")
print(lst[0:3])
print("Append lists")
lst=lst.__add__(weekdays)
print(lst.count(5))
print(len(lst))
print(lst)


print("Tuples")
tup = ('all your mark', 'set', 'go')
print('tuple starts with zero index ' + tup[0])
print(len(tup))
print("tuple doesn't support any add/update/delete operation")
#tup[0]='get ready' #object does not support item assignment
print(tup)
print('Workaround is convert to list and do the operation')
tuplst=list(tup)
tuplst.remove('set')
print(tuplst)
tuplst.insert(1,'get set')
print(tuplst)
#simply update
tuplst[1]='get set'
print(tuplst)
tup=tuple(tuplst)
print(tup)
#by default sorts and remove duplicates
my_set = {5,1, 3, 1}
print(my_set)
print(my_set.__len__());
print(my_set.intersection(my_set))
my_set.remove(3)
# remove & discard does the same thing. removes the element.
# difference is discard doesn't raise error while remove raise error if element doesn't exist in set
#my_set.discard(7)
print(my_set)
my_set.add(6)
print(my_set)
my_set2={2,3,4}
#my_set.update(2) #Set can't be updated with an element, rather we can update a set with another set
my_set.update(my_set2)
print(my_set)


print("Dictionaries")
my_dict = {'first_name': 'inceptez', 'last_name': 'tech','age': 6}
print(my_dict)
#Adding Items
my_dict["city"] = "chennai"
print(my_dict)
#Updating Items
my_dict["last_name"] = "technologies"
print(my_dict)
#Removing an Item
#pop() delete value and returns deleted value.
# The __delitem__ delete value and dont returns anything
print(my_dict.__delitem__("age"))
print(my_dict)
print(my_dict.pop("city"))
print(my_dict)

print(my_dict.keys());
print(my_dict['first_name'] + ' ' + my_dict['last_name'])

print("Dictionaries")
my_dict = {'first_name': 'inceptez', 'last_name': 'tech','age': 6}
print(my_dict)
#Adding Items
my_dict["city"] = "chennai"
print(my_dict)
#Updating Items
my_dict["last_name"] = "technologies"
print(my_dict)
#Removing an Item
#pop() delete value and returns deleted value.
# The __delitem__ delete value and dont returns anything
print(my_dict.__delitem__("age"))
print(my_dict)
print(my_dict.pop("city"))
print(my_dict)
for key,val in my_dict.items():
 print('keys')
 print(key)
 print('values')
 print(val)

print("nested list")
nestlst = ["some string", [1,2,3], ['x']]
nestlst1 = nestlst[1][2]
print(nestlst1)

print("Complex tuple1")
tup = (['hello','ready'], {'shoot': 'fire'}, ('aim','concentrate','focus'))
print(tup[0][1])
print(tup[1]['shoot'])
print(tup[2][2])

print("Complex Tuple2")
complextup=(1,"Madison's Family",[{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna"}}])
print("id is "+str(complextup[0]))
print("Family name is " + str(complextup[1]))
print("gender of first list element is " + complextup[2][0]["gender"])
print("relation of first list element is " + str(complextup[2][0]["Relation"]))
print("personalinfo of the first list element is " + str(complextup[2][0]["personalinfo"]))
print("personalinfo title of the first list element is " + str(complextup[2][0]["personalinfo"]["title"]))
print("personalinfo title of the first list element is " + str(complextup[2][0]["personalinfo"]["name"]))