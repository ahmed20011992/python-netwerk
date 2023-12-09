import math
import random
print("hej,Ahmed")

if 70 < 100:
    print("yes it is bigger")

# this is a comment here
x = "Ahmed"  # here we can change the type of data for variables
x = 1992


w = str(3)
y = int(3)
z = float(3)

print(w)
print(y)
print(z)
print(type(w))
print(type(y))
print(type(z))


a = 3
a = 'ahmed'
print(a)
my_name = his_name = theName = '1ahmed Elhasan'
print(my_name)

# Python allows you to extract the values into variables. This is called unpacking.
names = ['ahmed', 'aziza', 'salsabil']
x, y, z = names
print(x)
print(y)
print(z)

j = 'here is my text'  # it is an global variable


def myFunc():
    j = 'i will deny that'
    print(j + 'i like to swimm')


myFunc()
print(j + ' i do not like to swimm')


def func():
    global x
    x = 'dont lie'


func()
# här betyder det att jag kan definera global variable inom function som global
print(x + ' for me i know you who you are')

o = 2j  # why it is not work if i add j and then 2
print(o)
print(type(o))

mylist = ['x', 'y', 'z']  # vi kallar den for en list data type
print(type(mylist))

mytuple = ('my', 'she', 'it', 'hem')
print(type(mytuple))  # den här är tuble data type

x = range(10)
print(x)
print(type(x))

x = {"name": "John", "age": 36}  # dict

# display x:
print(x)

# display the data type of x:
print(type(x))

x = {"name", "age", "tall"}   # det här är set
print(type(x))


x = frozenset({"apple", "banana", "cherry"})  # frozenset
# display x:
print(x)
# display the data type of x:
print(type(x))

x = b"Hello"
# display x:
print(x)
# display the data type of x:
print(type(x))

x = bytearray(10)
print(x)
print(type(x))

x = memoryview(bytes(1))
print(x)
print(type(x))

x = None

# display x:
print(x)

# display the data type of x:
print(type(x))

print(5j + 3j)

#####
print(random.randrange(0, 2000))


b = """hej """
print(b)
print(b[2])
print(len(b))


# loop
for x in "sssss":
    print(x)
    print(len(x))

helsning = "hej mitt namn ahmed"
if "ahmed" in helsning:
    print("ja, den är rätt")


b = "Hello World!"
print(b[2:5])
print(b[:5] + "hhh")
print(b[5:])


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


age = 36
txt = "My name is John, and I am {}"
# se the format() method to insert numbers into strings:
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


thisset = {'ahmed', 'aziza', 'salsabil'}
if 'ahmed' in thisset:

    print(True)


thisset.add('Fadel')
print(thisset)
otherset = {'adulrahem', 'ghassan', 'abdulsattar'}
thisset.update(otherset)
print(thisset)
mylist = ['mamma', 'huda']
thisset.update(mylist)
print(thisset)
thisset.remove('ahmed')  # or we can use discard
print(thisset)

# brimaNumber = range(1,1000)
# def isPrime(num):
#     for z in range(2,num):
#         if(num%z) == 0 :
#             return False
#         return True
# primes = list(filter(isPrime,brimaNumber))
# print(primes)

original_range = range(1, 6)
reversed_range = list(original_range[::-1])
print(reversed_range)
# Output: [5, 4, 3, 2, 1]


myPrima = range(1, 10)


def prime(num):
    if (num % 2 == 0):
        return False
    return True


this = list(filter(prime, myPrima))
print(this)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# The union() method returns a new set with all items from both sets:
set3 = set1.union(set2)
print(set3)


def x(a, b, c): return a*b*c


print(x(200, 300, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()


class minclass:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def myfunc(abc):
        print('hej det här är mitt ' + abc.name + ' ' + abc.lname)


a = minclass('Ahmed', 'Elhasan')
a.myfunc()

x = pow(6, 10)  # det 6 upheit till 10
print(x)


x = math.sqrt(64)
print(x)


powers_of_two = [2**i for i in range(11)]
print(powers_of_two)

power_of_three = [3**i for i in range(10)]
print(power_of_three)

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Printing all key/data pairs
for key, value in my_dict.items():
    print("Key: {key}, Value: {value}")
    print(key, value)

if (20 <= age <= 60):
    print("vad håller du på med")


# # Opening a text file for reading
# file_path = ''  # Specify the path to your text file
# with open(file_path, 'r') as file:
#     # Reading and printing all the rows
#     for line in file:
#         print(line.strip())  # Use strip() to remove extra whitespace (like '\n') at the end of each line
