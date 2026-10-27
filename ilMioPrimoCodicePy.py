 # Import the time module, which provides time-related functions like sleep()
import time
# Loop over a range of numbers from 1 to 5 (inclusive)
for i in range(1, 6):
    # Print a loading message with a percentage that updates on the same line
    print(f"\rLoading... {i*20}%", end="")
    # Pause the execution for 1 second to simulate a loading delay
    time.sleep(0.1)
print("\nDone!")

#
name = "Ibrahim"

print(f"Ciao, {name}")

tipo = type(name)
print(type(name))

number = 10
print(number**2)

func = lambda x : x**2
print(func(3))

lista = [2, 3, 4, 5, 6, 7, "a", 'b', '&']
lista_num =[1, 2, 3, 4, 5, 6]
print(lista[0:len(lista):1])
print(min(lista_num))
print(max(lista_num))
print(len(lista))

for i in lista : print(i)

stringa = """stringa"""
print(stringa)

"""
s1 = {1,2,3,4,5,6,7,8,9}
print(set1)
print(set1)
s2 = {1,2,3,4,5,6,7,8,9}
print(s2)
print(s2)

def square (x):
	return x*x

square1 = square(s1[0])
print(square1)
"""

def my_function(*args, **kwargs):
   print(args)
   print(kwargs)

my_function( (1,2,3), a = 1, b = 'wow', c= (4,5,6))
ab = range(10)
print(ab)
for i in ab: print(i)

for i in range(0,10,2): print(i)




import sys

def squared (x) :
  return x*x

if __name__ == "__main__":

  number = float (sys.argv[1])
  print ('the square power of ' + str (number) + ' is: ' + str (squared (number)))

