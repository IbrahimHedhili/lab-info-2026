import numpy as np

a_list = [4, 4, 3]
an_array = np.array(a_list)
print(an_array)


arr = np.array([x**2 for x in range(5)])
print(arr)

an_array = np.zeros(3)
print(an_array)

an_array = np.ones(3)
print(an_array)

an_array = np.empty(3)
print(an_array)

first = 1
last = 3
step = 1
an_array = np.arange (first, last, step)
print(an_array)

number = 5
an_array = np.linspace (first, last, number)
print(an_array)

a_list = range(0,4)
print(a_list)

an_array3 = np.empty(4)
print(an_array3)

for i in a_list:
    an_array3[i] = i + 3


print(an_array3) 

an_array3 = 0
print(an_array3)

an_array3 = np.empty(4)
print(an_array3)



