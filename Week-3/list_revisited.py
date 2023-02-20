#usr/bin/env python3

myfavouritefruits=["banana,pineapple,apple,mango,guava"]
for fruit in myfavouritefruits:
    print (fruit)

    print(len(myfavouritefruits))
    #len=number of element in a list

friends=["Ezra","Alvin","Sam","Martin","Malcom","Swabir"]
print(friends)

friends[0] ="Mary"
print(friends) 
numbers=["petr,water"]
print(numbers)



#append()=adds an element at the end of the list
#clear()=removes all elements from the list
#copy()=returns a copy 
#insert()=adds an element
#sort()= sorts the list in alphabetical order
#reverse()=reverses the sorting
#remove()=removes the specified value
#pop()=removes the element at a specified position
#extend()=adds an element at the end of the list
print(friends)
print("-------------------------------------")
new_friends=friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)




