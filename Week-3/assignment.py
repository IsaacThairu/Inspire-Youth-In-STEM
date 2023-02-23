#create a list of sporting activities
#create an empty list of favourite musicians
#using forloop add 5 musicians
#copy to a new list called celebs
#sort the list
#pop out 2 celebrities from the list
#count the remaining celebrities in the 


fav_musicians = []

#using for loop add five new musicians



for musician in range(0,3):
    the_musicians = input("Enter name:")
    print(the_musicians)
    fav_musicians.append(the_musicians)

print(fav_musicians)

#copy the list to a new list called celebs 
celebs = fav_musicians.copy()
print(celebs)

#sort the list
celebs.sort()
print(celebs)

#pop out two celebrities
celebs.pop()
celebs.pop()
print(celebs)

#count the remaining celebrities in the list
print(len(celebs))


















