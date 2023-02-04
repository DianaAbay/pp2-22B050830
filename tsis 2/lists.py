thislist = ["apple", "banana", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

#Negative Indexing
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry

#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword also removes the specified index

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Loop Through a List
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
"""Output:
apple
banana
cherry"""

#Loop Through the Index Numbers
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Using a While Loop
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using List Comprehension
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #['apple', 'banana', 'mango']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)  #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)  #['hello', 'hello', 'hello', 'hello', 'hello']
 
 #Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  #['apple', 'orange', 'cherry', 'kiwi', 'mango']


#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  #[23, 50, 65, 82, 100]

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Customize Sort Function
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]

#Case Insensitive Sort
#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  #['Kiwi', 'Orange', 'banana', 'cherry']

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)  #['banana', 'cherry', 'Kiwi', 'Orange']


#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  #['cherry', 'Kiwi', 'Orange', 'banana']


#Copy a List
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']

#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  #['a', 'b', 'c', 1, 2, 3]

#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)  #['a', 'b', 'c', 1, 2, 3]

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  #['a', 'b', 'c', 1, 2, 3]
