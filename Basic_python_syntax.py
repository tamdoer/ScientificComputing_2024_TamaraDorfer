# Showing that normal math works
print(1 + 1) # using our first function, print(), the argument is in round brakets
			 # need to use print() to actually see output on terminal

2/3
2 * 5

#defining variables
a = 2
b = 3
a*b

c = 2.5 # this is a float
a * c

"abc2" # this is a string
d = "abc2"
e = "4"
f = 4*e

print(f) #resulting is mathematically wrong, as we are multiplying a string


#You can execute a single line or several lines in a script by "activating" them and using:
#
#	 option – shift – e on Mac
#	 alt – shift – e on Windows
#
# code will be executed in python console and you can inspect the different variables in the
# variable explorer then

## Introducing lists
integer_list = [1,2,3,4,5]
mixed_type_list = ["a",1,1.23]
print(integer_list)


#for loop syntax
#for x in iterable_item:
#   your action with x
#important to include colon
#indent with 4 empty spaces

for i in integer_list:
    print(i*2)
print(i)
# if we now only use print(i), python will only print the last variable that was i --> 5 in this case

fishies = ["halibut", "cod", "plaice", "shark"]
for fish in fishies:
    print(fish)

print(fishies[1])
#WATCH OUT: python starts counting at 0 so for halibut index 0

print(fishies[-1])
#when counting from the back, -1 does actually chose the last one (kinda duh, you can't have -0)

print(fishies[2:4])
#prints number the first number and the one BEFORE the last number

print(integer_list[:3])
