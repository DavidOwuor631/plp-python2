my_list=[]

new_list=[10, 20, 30, 40]
my_list= new_list
print(my_list)

my_list[1]=15
print(my_list)

my_list.extend([50, 60, 70])
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)