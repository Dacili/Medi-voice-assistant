# This is a project for medi to play with
# needed to install python first
# then I installed py charm
# now exploring other things

"""
this is a multi line comment heheh
"""

print('medi hehhe')
a = 5
b = a*2
print (b)
if a > b:
    print('a is greater than b')
elif b>a:
    print('b is greater than a')
else:
    print('a and b are equal')

#Short Hand If
if a>b : print("a")
#Short Hand If ... Else - ternary operator ()? :
print("a") if a>b else print("b")


a, b, c = 'hello', "world", "woow"
print(a, b, c)
x = y = 9
y = 'cao'
print(x,y)

def mediFunction(parameterMedi):
    global squareParam #we cannot do the assignment in this line,
    # we can merge these 2 lines, with using ;
    squareParam = parameterMedi*parameterMedi #to be available outside of the function scope
    print(parameterMedi)

mediFunction(x)
print(squareParam)
print(type(squareParam))


def mediFunctionWithXParams(parametri):
   pass #da ne baci error da nije implemented

import random
print(random.randrange(0,10))
# casting
floatNum = float(2)
print(floatNum)
print('medi'+ " playin with strings")
stringic = """I am
here for
multiline string hehe
""" #or we could use '''
print(stringic)

for x in "medi":
    print(x)
print(len("med"))
print("medi" in "medina") #is substring of
print("x" not in "medina") #not substring of

# slicing
print(stringic[2:5]) #from position 2 till 5
print(stringic[:5]) #until 5th
print(stringic[2:]) #from 2nd char till end

print(a.upper())
print(a.replace('h', 'HHHH'))
print('    kkk    '.strip()) # trim
print('hej medi'.split(' '))

#escaping chars
print("ja sam \"medi\"")

# == or !=
if(4 and 5):
    print('yes')
if(not(4 and 0)):
    print('no')

#list can contain diff types
medi = ['apple', 5, 'hehe']
print(medi)
medi.append(8) #push at the end
medi.insert(1, 7) #push at 1 index
print(medi)
medi.remove(7)
medi.pop() #remove the last
#medi.clear()#deletes all elements
print(medi)
newMedi = [x for x in medi if x == 5]
print(newMedi)
#shallow copy is medi = newMedi
# deep copy
deepCopy = medi.copy() #or deepCopy = list(medi)
deepCopy[0]='APle'
print(deepCopy)
print(medi)

'''
List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 mytuple = ("apple", "banana", "cherry")

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. 
myset = {"apple", "banana", "cherry"}

Dictionary is a collection which is ordered** and changeable. No duplicate members.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'''

class Medii :
    def __init__(mediObj, name, age):
        # init is actually a constructor, the first param is reference to the instance of that class
        mediObj.name = name
        mediObj.age = age

m1 = Medii('medi name', 20)
print(m1.name)

#PIP is a package manager for Python packages
#pip list  -> to list all installed pkgs

# import module sys to get the type of exception
import sys
try:
    print('9')
    raise Exception('medi error')
except Exception as e:
    print('exception was thrown ' + str(e))
else:
    print('all good')
finally:
    print('i\'m executed always')

username = input('Pls enter username:')
print('Your username is '+ username)

#if I want to export all libriaries in some file, (like package.json), choose name what you want
# run this in cmd
#python -m pip freeze > requirements.txt

#if you want to install them
#python -m pip install -r requirements.txt
