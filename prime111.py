tuple1 = (11, 22, 33, 44, 55 ,66) 
list1 =list(tuple1) 
new_list = [] 
for i in list1: 
   if i%2==0: 
       new_list.append(i) 
new_tuple = tuple(new_list) 
print(new_tuple)
