# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
np.loadtxt("C:/Users/Silvio/Documents/Career/Harvard/best_text_ever.txt",dtype=int)

y = [x**2 for x in range(5)]

import math
math.pi

numbers=[2,4,6,8]#A LIST: can find how many objects in list using len
numbers[0:2]
numbers.    (10)
numbers
x=[12,14,16]
x+numbers#adding lists
Out[6]: [12, 14, 16, 2, 4, 6, 8, 10]
numbers.reverse()#REVERSE
numbers

names=["B","A","C","D"]
names.sort()
names
sorted_names=sorted(names)
names
sorted_names#sorted, while other is not

len(names)

#Tuples are a type of sequence
T=(1,3,5,7)
len(T)
T+(9,11)
x=2
y=3
coordinate=(x,y)
type(coordinate)#UNPACKING TUPLES
coordinates=[(0,0),(1,1),(2,4),(3,9),(4,16)]
for (x,y) in coordinates: 
    print(x,y)
c=(2,)#SINGLE OBJECT TUPLE
type(c)
##

type((2,))

x=(1,2,3)
count(x)
x.count(3)##COUnts

##RANGES
list(range(5))
list(range(1,15,2))
list(range(7,32,5))

##Strings
S="Python"
S[-3:]#slice and take out hon
"Y" in S#FALSE 
"hello"+" aliens"
3*S#PythonPythonPython
"eight equals " +str(8)
str.replace?
namewrong="Sulvuo Martunez"
name_correct=namewrong.replace("u","i")
name_correct
names=name_correct.split(" ")
names[0].upper()#ALL CAPS UPPERCASE

"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"
str(range(10))
dir(str)
x=str(125000)
str.isdigit("125,000")

#SETS
ids=set([1,2,4,6,7,8,9])
ids.add(10)
ids
#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
ids.pop()#removes first number of set
ids=set(range(10))
males=set([1,2,6,9,10])
females=ids-males
females
everyone=males|females#Union
everyone & set([1,2,3])
word="antidisestablishmentarianism"
letters=set(word)
len(letters)

x={1,2,3}
y={2,3,4}
y-x#subtract sets, only take numbers from the set subtracting from
x.issubset(y)#check if all elements or objects in x are in y
x.symmetric_difference(y)#take all different elements between x and y

#Dictionaries
age=dict()
age={"Tim":29,"Jim":31,"Tyler":20,"David":23,"Jace":27,"Alicia":22}
age["Alicia"]=age["Alicia"]+1
age["Jace"]+=1
age["Jace"]
names=age.keys()
type(names)
#Add name to dictionary
age["Tom"]=37
names
ages=age.values()

#remove key from dictionary
age.pop('Tim',None)#returns value if it exists, and none if it doesn't
age.pop()

age["Tim"]
age[0]
ages
"Tom" in names
"Tom" in age#how to check if name in set, check membership
age

29 in ages
    
##TYPES
L=[1,2,3,4]
M=list(L)#Creates completely new object
M is L#false
M==L#True 
#OR
M=L[:]

#Copies
import copy
x = [1,[2]]
y = copy.copy(x)
z = copy.deepcopy(x)
y is z
z is x
x is y
x==y
x==z

#IF statements
if x > y:
    difference=x-y
    print("x is greater than y")
else:
    print("y is greater than x")
    
3%2==0
if n%2 == 0:
  print("even")
else:
  print("odd")
  
  #For loops
names=["Tyler","Danielle","Ula","Alicia","David","Jovaniel","Alexandra"]
names[0]
names[0].upper()
  for name in names:
      print(name.upper())
  #index to get names out
range(len(names))
  #iterate over all key values pairs in dictionary
  age.keys()#returns the keys of dictionary, which allow to access dictionary
  for name in age.keys():
      print(name,age[name])#prints out name specified by key, then value of object
  for name in age:#shorthand, don't need parentheses or .keys
      print(name,age[name])
for name in sorted(age):#alphabetical order
    print(name,age[name])
for name in sorted(age, reverse=True):#reverse alphabetical order
    print(name,age[name])
#for loop vs while loop: use while loop when don't know how many times running,
#and for loop when you know exactly how many times
 bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
  if bears[bear]=="friendly":#first call dictionary, then use for target to get value of object
   print("Hello, "+bear+" bear!")
else:
  print("odd")
  
  
  #list(range(2,100))
  is_prime = True
  n=17
for i in range(2,n):
   if n%i == 0:#if not prime
     is_prime= False   
print(is_prime)


N=20
for n in range(2,N):
   is_prime = True
   for i in range(2,n):
     if n%i == 0:#if not prime
         is_prime= False
   if is_prime:
       print(n)
   print(is_prime)
    

for i in range(2,n):
   if n%i == 0:#if not prime
     is_prime= False   
     print(is_prime)
print(is_prime)

for i in range(5):
    print(i)
8%2
9%2
21%3
137%7
137/7
19*7
3 /= 2

n=100
number_of_times = 0
while n >= 1:
   n /= 2
   number_of_times += 1
print(number_of_times)

sum=0
for i in range(10):
    sum=sum+i
    print(sum)

sum=0#For loop above is same as this while loop
i=0
while i<10:
    sum=sum+i 
    print(sum)
    i=i+1

color=["Blue","Silver","Orange"]
for i in color:
    print(i,"is one of Silvio's favorite colors.")

#LIST COMPREHENSIONS
numbers=range(10)
squares2=[number**2 for number in numbers]
squares2

list(range(0,10,2))
list(range(1,10,2))
sum([num**2 for num in range(1,10,2)])

sum([i**2 for i in range(3)])

#1.3.6 remove line breaks
#turn a file into a list
#read file
for line in open(filename):
    line=line.rstrip().split(" ")
    print(line)
    #output: ['first','line']
#can also add in text to a file by putting F.write("word\n") and F.close to complete.
#\n puts in line break

def addsub(a,b):
    mysum=a+b
    mysub=a-b
    return(mysum,mysub)
addsub(2,3)#returns tuple

def modify(mylist):
    mylist[0]*=10#Must use the = sign not just *
    
L=[1,2,3,4]
modify(L)
L

#Writing simple functions!
def intersect(s1,s2):
    res=[]
    for x in s1:
        if x in s2:
            res.append(x)
    return(res)

intersect([1,2,3,4,5],[3,4,5,6,7])

import random
random.choice([1,2,4,5,6])
"a"+"b"

def password(length):
    pw=str()
    characters="abcdefghijklmnopqrstuvwxyz"+"0123456789"
    for i in range(length):
        pw=pw+random.choice(characters)
    return(pw)
password(10)

def is_vowel(letter):
   if type(letter)==int:
        letter=str(letter)
   if letter in "aeiouy":
        return(True)
   else:
        return(False)
 
 is_vowel(1)
    
 def factorial(n):
     if n==0:
         return 1
     else:
         N=1
         for i in range(1,n+1):
             N*=i
         return(N)
     
        factorial(3)
        
"the answer is" +" 8"

#HW Week 1
import string
alphabet=string.ascii_letters   
alphabet
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letters={}
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:#
            count_letters[letter]+=1#adds 1 to existing letter
        else:
            count_letters[letter]=1#creates new letter with 1 value
print(count_letters)

for count_letters in sentence
     if count_letters.key()
##########
count_letters={i:sentence.count(i) for i in sentence if i in alphabet}
print(count_letters)
#counts letters
big= 'TTtt'
big.lower().count('t')
 ##################
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letters={}

# Create your function here!
import string
alphabet=string.ascii_letters   
alphabet
def counter(input_string):#counts unique letters & occurrences in inputted string
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter]+=1
            else:
                count_letters[letter]=1
    return(count_letters)
counter(sentence)
#make a function that computes the golden ratio; two numbers, 0 and 1
#repeatedly, one for loop or one while loop

counter('Jim')
alphabet
def counter(input_string):
    return{i: input_string.count(i) for i in input_string if i in alphabet}
print(counter(sentence))
 
address_count={}
address_count=counter(address)
print(address_count)
#count most frequent letter in address_count
address_count

def maxvalue(dic):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]
most_frequent_letter=(maxvalue(address_count))
print(most_frequent_letter)

vector(1,2,3)
v1

#TESTING
stats = {'a':1000, 'b':3000, 'c': 100}

def maxvalue(dic):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]
maxvalue(stats)
##############
import math
math.sqrt(4)

import numpy

x=(0,0)
y=(1,1)
print(math.sqrt(sum(numpy.square(numpy.subtract(y,x)))))
(numpy.square(y,x))


def distance(y,x):
   math.sqrt(sum(numpy.square((numpy.subtract(y,x)))))
print(distance(1,1))

####
x=(0,0)
#type(x)
#??????
y=(1,1)
math.sqrt(2)

k=[0,0]
l=[1,1]
def distance(x,y):
   return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
distance(k,l)


print(distance(0,1))
 print(distance(1,1))
math.sqrt(1**2+1**2)
math.sqrt(2)

c
x=[1,2,4,5]
mean(x)

import random
rand(0,2)
####
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand(x,y):
   # define `rand` here!
    return float(random.randrange(-100,101)/100)
rand(-100,101)

?random.uniform()

(.363)/(.406/math.sqrt(14))

import random
import decimal

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand(x,y):
     return random.uniform(x,y)
rand(-1,2)

random.uniform(1,2)



F = open("my_file.txt","w")
for i in range(10):
    F.write("Hello World"+"\n")
F.close()

F = open("myfile.txt","w")
F
for i in range(10):
    F.write(str(i)+"\n")
F.close()

import os
help(os)
os.getcwd()

def even(x):
    
    
    

    
    
    