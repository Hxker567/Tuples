#Define Tuple
# A tuple is to store multiple items in single variable. Such elements of a tuple are enclosed in parethesis(). 
# For ex:
# t = (1,2,3,4,5)   # A tuple
# t1 = ()   # Empty tuple
# Please note:
# t1 = (1)   # This is the wrong to declare a tuple because the elements has no commas.
# t1 = (1,)   #This is the right to declare a tuple.

#Is tuple is a immutable data type ? Justify ? with example
# A tuple is a immutable data type because you can't change it after it has been created. If you do an attempt that lead to an error.
# For ex: 
# t1 = (1,2,3,4,5,6)
# t1[3] = 10  
# TypeError: 'tuple' object does not support item assignment

#Repetiton 
# This method is used to repeat the elements of a tuple. Depicted by the symbol of *.
# For ex:
# t1 = ("Vietnam","Dubai")
# t1*3
# print(t1*3)
# ('Vietnam', 'Dubai', 'Vietnam', 'Dubai', 'Vietnam', 'Dubai')

#Membership
# The in operator returns true if the element is present in the tuple, else it returns false.
# For ex:
# t1 = ('Red','Green','Blue')
# 'Green' in t1
# print('Green' in t1)
# True
# The not in operator returns true if the element is not present in the tuple, else it returns false.
# For ex:
# t1 = ('Red','Green','Blue')
# 'Green' not in t1
# print('Green' not in t1)
# False

#Slicing
# t1 = ("America","Vietnam","Thailand","Dubai","Bangkok","Singapore","Indoneasia","India")   #Tuple
# print(t1[2:7])   #elements from index 2 to index 6.
# ('Thailand', 'Dubai', 'Bangkok', 'Singapore', 'Indoneasia')
# print(t1[0:len(t1)])   #all elements of a tuple are printed
# ('America', 'Vietnam', 'Thailand', 'Dubai', 'Bangkok', 'Singapore', 'Indoneasia', 'India')
# print(t1[:5])   #slicing starts from zero index 
# ('America', 'Vietnam', 'Thailand', 'Dubai', 'Bangkok')
# print(t1[2:])   #slice is till end of the tuple
# ('Thailand', 'Dubai', 'Bangkok', 'Singapore', 'Indoneasia', 'India') 
# print(t1[0:len(t1):2])   
# ('America', 'Thailand', 'Bangkok', 'Indoneasia')
# print(t1[-6:-4])   #Negative indecies
# ('Thailand', 'Dubai')
# print(t1[::-1])   #tuple elements traversed in reversed order
# ('India', 'Indoneasia', 'Singapore', 'Bangkok', 'Dubai', 'Thailand', 'Vietnam', 'America')

#Tuple methods
# len()
# Returns the length of the tuple.
# For ex:
# t1 = (10,20,30,40,50)
# print(len(t1))
# 5
# count()
# Returns the no of times the given element appear in the tuple
# For ex:
# t1 = (10,20,10,30,10,40,50,10)
# print(t1.count(10))
# 4 
# index()
# Returns the index no of the first ocuurance of the element in the given element. Means the element in the tuple at which position or no.
# For ex:
# t1 = (10,20,30,40,50)
# print(t1.index(40))
# 3
# sorted()
# This method takes elements of tuple and sorted() them into alphabetical order and returns new sorted tuple. But sorted() method dosen't make changes into original tuple.
# For ex:
# t1 = ('Zara','Jatin','Soumya','Sianshi','Jonathan')
# print(sorted(t1))
# ['Jatin', 'Jonathan', 'Sianshi', 'Soumya', 'Zara']
# min()
# Returns minimum no. of element in the tuple
# For ex:
# t1 = (2,3,4,5,6)
# print(min(t1))
# 2
# max()
# Returns maximum no. of element in the tuple
# For ex:
# print(max(t1)) 
# 6
# sum()
# Returns the sum of all elements in the tuple.
# For ex:
# print(sum(t1)) 
# 20

#Tuple assignment
# record = ("Pooja","40","CS")
# (name,rollno,subject) = record
# print(name)
# Pooja
# print(rollno)
# 40
# print(subject)
# CS

#Nested tuples
# A tuple inside another tuple is called as nested tuple.
# For ex:
# (1,2,3,4,5,[7,8]) 

