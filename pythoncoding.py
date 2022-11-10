#Python Coding Basics – Part 3
"# For Loops"

"# Iterating over a sequence (list, tuple, dictionary, set, string)"

"# Executed once for each item in the list"



my_list = [1, 2,4, 3]

for i in my_list:

    print(i)



for i in my_list:

    print("Hello thaakkaa")

    print(i)



my_list = ["apple", "peach","malt", "pear", "plum"]

for i in my_list:

    print(i)



for i in "apples":

    print(i)



for element in my_list:

    print(element)



for i, element in enumerate(my_list):

    print(i, element)



"# Break a Loop / Continue"

"# break()"

"# continue()"



my_list = ["apple", "peach", "pear", "plum"]

for i in my_list:

    print(i)

    if i == "pear":

        break



"# Range"

"# Generates a list of numbers to iterate over with for loops"

"# range(0,10) generates integers from 0 up to, but not including 10"



for i in range(16):

    if i % 2 == 0:

        continue

    print(i)



for i in range(6):

    print(i)



"# While Loop"

"# To execute a set of statements as long as some coditions hold true"



i = 0

while i <= 10:    

    print(i)

    i += 1



i = 0
while True:

    print(i)

    i = i + 1

    if i >= 10:

        break



"# Nested Loop" "# Loop that exists inside the body of another loop"

"# Function"

"# A block of code that can run whenever it is called"

"# Data or arguments can be passed to the function or returned from the function"



def square(x):

    return x ** 2

    print(square(6))



"# Built-in Functions"



my_list_1 = [2, 4, 6]

my_list_2 = [3, 6, 9]

for i, j in zip(my_list_1, my_list_2):

    print(i + j)



"# Lambda Expression"

"# Create small anonymous functions (no name)"

"# Use with filter(), map(), and reduce()"

"# Many number of arguments but only one expression"



def my_function_square(x):

    return x ** 2

print(my_function_square(9))



y = lambda x:x**2

print(y(3))



result = lambda x, y, z : x + y + z

print(result(1, 2, 3))



"# Map"

"# map() takes in a function and a list"

"# performs an operation on the entire list and returns a new list"



def summation(a,b):  

   return a + b


a = [1, 3, 5, 7, 9]

b = [2, 4, 6, 8, 10]



x = list(map(summation, a, b))



print(x)



my_list = [ 1, 2, 3, 4]

output_list = list(map( lambda x: x**2 , my_list))



print(output_list)



"# Filter"

"# Select elements within a list and apply the function to the selection"



my_list = [1, 2, 3, 4, 5]



output_list = list(filter( lambda x: (x % 2 == 0) , my_list))



print(output_list)



"# Numpy"

"# Linear algebra library"

"# Use for multidimensional arrays"



import numpy as np



my_list = [5, 3, 10]

print(my_list)



y = np.array(my_list)

print(y)

print(type(y))



matrix = np.array([[1, 2], [3, 4]])

print(matrix)



"# Built in Methods and Functions"



x = np.random.rand(3)

print(x)



x = np.random.randn(2)

print(x)



x = np.random.randint(1, 10)

print(x)



x = np.arange(1, 10, 2)

print(x)



x = np.eye(5)

print(x)



"# Shape, Length, and Type of Numpy Arrays"



my_list = [5, 3, 10]

print(my_list)



y = np.array(my_list)

print(y)

print(len(y))

print(y.shape)



y = np.array(my_list)

print(y)



matrix = np.array([[1, 2], [3, 4]])

print(matrix)

print(matrix.shape)

print(matrix.dtype)



y = np.array([1, 3, 5, 7])

print(y.reshape(2, 2))



"# Max and Min Values and their Index"


print(y.max())

print(y.min())

print(y.argmax())

print(y.argmin())



"# Mathematical Operations"



x = np.arange(1, 5)

print(x)



y = np.arange(1, 5)

z = x + y
print(z)



"# Element Slicing and Indexing"



x = np.random.randint(1,10, 10)

print(x)

print(x[0])

print(x[3])



matrix = np.random.randint(1,10, (5,5))

print(matrix)

print(matrix[2])



"# Matplotlib"



import matplotlib.pyplot as plt

import numpy as np

x = np.arange(1, 10, .2)

print(x)


y = np.sin(x)

print (y)


plt.plot(x, y)

plt.xlabel("Time")

plt.ylabel("Sin Wave")

plt.title("Sin Wave")



plt.show()

import random

X = np.random.randn(600)

Y = np.random.randn(600)



plt.scatter(X,Y)

plt.show()



import numpy as np

import matplotlib.pyplot as plt



t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', linewidth=5.0)

plt.show()