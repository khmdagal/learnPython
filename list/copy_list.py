# ========  Shallow Copy ============
list1 = [12,9,3,7,5,4]
list2 = list1.copy() # copy() method is used shallow copy of list
# print(id(list1)) # 2364299231104
# print(id(list2)) # 2364301125376
# As you can see they are not the same thing in momory, but they have 
# the same values


# ======== Deep Copy ============

import copy 
list1 = [12,9,3,7,5,4]
list2 = copy.deepcopy(list1) 
# deepcopy() method is used deep copy of list
print(id(list1)) 
print(id(list2))
