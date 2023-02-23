
#mutable vs immutable
#mutable are data types 
# Add / remove elements
# immmutable -->data types 


#  1) list (immmutables)
friends  = ["malcom","alvin","darrell","brian"]
# or friends = [] for empty
# add ----> append() ,extend()
# remove---> del(), pop()
students = ["ezra","josh","steve"]
friends.extend(students)
friends.append("james")
friends.sort()
friends.reverse()
# 2) tuples (immutable)
# types of  list that are immutable
stationaries = ("pen","ink","sharpener","stapler")
#replace the whole tuple
stationaries = ("ruler","clipboard","eraser")
for stationary in stationaries:
    print(stationary)
numbers = (1,2,3,4,5,6,7,)
# 3)Dictinories aka dict


#key and key value par
students = {"name": "malcom", "age":24,"gender": "male", "height": "6'1"}
print(students["name"])
print(students["age"])
print(students["gender"])
print(students["height"])

print(students.values())
print(students.keys())


friends = {"favourites_colour":"yellow","hobby":"swimming","Team":"liverpool","course":"IT","weight":67,"height":6.1}
print(friends["favourites_colour"])
print(friends["hobby"])
print(friends["Team"])
print(friends["course"])
print(friends["weight"])
print(friends["height"])

print(friends.values())


my_fruits={"banana","watermelon","pawpaw","mango","guava"}
for fruits in my_fruits:
    print(fruits)


print(type(my_fruits))
print(len(my_fruits))





