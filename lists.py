my_list = []

#appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("after append:", my_list)

#inserting a value
my_list.insert(2, 15)
print("after insert:", my_list)

#Extend with another list
another_list = [50,60,70]
my_list.extend(another_list)
print("after extend:", my_list)

#Removing the last element
my_list.remove(70)
print("after remove:", my_list)

#sorting the list in ascending order
my_list.sort()
print("after sort:", my_list)

#get index of specified number
index = my_list.index(30)
print(index)