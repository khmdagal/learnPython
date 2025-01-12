
# Sets are unordered collection for unique elements.
# ==== Sets ====
# 1 set is unordered collection
# 2 Set only holds unique elements, not duplicates 
# 3 You can loop of the the sets
# 4 they are indexed

# One of the use cases of the sets is using for memberships

read_more_sets = 'https://docs.python.org/2/library/sets.html'

set1 = {0,1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}



for n in set1:
    n = 2
    # print(n)

# ===== ===== Operations ===== =====
# 1 ==== len ==== method

len(set1) # we should get 5

# 2  ==== in ==== method

3 in set1  # True

# 3 ==== not in ==== method
4 not in set1 # False because 4 in set1
6 not in set1 # True because 6 is not in set1


# 4 ==== s.issubset(t) same as s <= t ==== method
# test whether every element in set1 is in set2
print("Line 37",set1.issubset(set2))  # False
print("Line 38",set1 <= set2) # False, because every element in set1 is not in set2


# 5 ==== s.issuperset(t) same as s >= t ==== method
# test whether every element in set2 is in set1

print("line 44", set2.issuperset(set1)) # False
print("line 45", set2 >= set1) # False, because every element in set2 is not in set1


# 6 ==== s.union(t) same as s | t ==== method
# This union() built-in method will create a new set consists of both sets, with unique elements
union1 = set1.union(set2)
union2 = set1 | set2
print("line 52",union1) # {1, 2, 3, 4, 5, 6, 7, 8} not duplicated 4,5 and 6 which are element of both sets
print("line 53",union2)

# 7 ==== s.intersection(t) same as s & t ==== method
common_elements1 = set1.intersection(set2)
common_elements2 = set1 & set2

print("line 59", common_elements1)
print("Line 60",common_elements2) # these two sets share these {4, 5, 6} elements 

# 8 ==== s.difference(t) same as s - t ==== method
difference1 = set1.difference(set2)
difference2 = set1 - set2
# we expect here to see all element in set1 but not in set2
print("line 65",difference1) # {0, 1, 2, 3}
print("line 66",difference2) # {0, 1, 2, 3}
# set1 = {0,1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
# If you look closely element 0,1,2,3 are in set1 but not in set2


# 9 ==== s.symmetric_difference(t) same as s ^ t ==== method
# This method will create a new set that consists off element that both sets don't share
symmetrical_diff1 = set1.symmetric_difference(set2)
print("line 76",symmetrical_diff1) # {0, 1, 2, 3, 7, 8, 9}
# we expect to see {0,1,2,3,7,8,9}
# set1 = {0,1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}


# ===============  EXAMPLES ======================

engineers = set(['Khadar','Ahmed','Yusuf'])
programmers = set(['Haroon','Salah','Kesi','Sarah'])
managers = set(['Alicia','Salah','Sarah','Barny'])
employees = engineers.union(programmers,managers)
# we can use engineers | programmers | managers and we can achieve same result, with more cleaner syntax
print(employees)


# === Task 1 ===
# now we want to find out employees who are programmers and managers
# So, we should find out the intersection of engineers and managers sets
# we can achieve this 
#  1 engineers.intersection(managers) or engineers & managers
programmers_managers = programmers & managers
print("line 97",programmers_managers) 


# === Task 2 Full time managers  ========
# Now we need to find out full_time managers 
# So, we need to find the difference between programmers and manager
# possible method programmers.difference(managers) or programmers - managers
full_time_managers1 = programmers.difference(managers) 
print(full_time_managers1)
print(f"****  Wrong result *** {'Kesi', 'Haroon'}, we don't want full time programmers, but full time managers")


full_time_managers2 = managers - programmers
print(full_time_managers2) # {'Alicia', 'Barny'}
print(f"****  Right result *** {'Alicia', 'Barny'}, are the full time managers")
# THE IMPORTANT THING TO REMEMBER WHEN DOING THIS OPERATION SO WHAT IS LEFT AND WHAT IS RIGHT



# === Task 3 Updating engineers and reconciling with employees ========

print("==Before extra element or engineer added to the engineers list ===",employees.issuperset(engineers)) # True
engineers.add('Alton')
print(engineers)
print("== before updated employees list === ",employees >= engineers) # False, because every element or engineer is not in the list of employees, So we need to update employees list

print("Before updated employees list", employees)
employees.update(engineers)

print("After updated employees list", employees)
# Now we updated the employees list so the following method will evaluate True
print("==After updated ===",employees.issuperset(engineers))



# === Task 4 Looping through the difference groups at same time and doing some operation ========

for group in [engineers, programmers, managers,employees]:
    group.discard('Sarah')
    print(group)


for employee in employees:
    if(employees == 'Haroon'):
        employees.discard(employee)
    print(employee)