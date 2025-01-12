tasks = ['Trash', 'Dishes', 'Laundry','Dinner','Vacuum',"dinner",'dinner']

# Accessing 
tasks[0] 

# Updating List Elements
tasks[1] = 'Food'

# print("==Before ===>>",tasks)
# tasks.remove('Dinner')
# print("==After ===>>",tasks)

#=============== Count method
print(f"""The count of dinner is {tasks.count('dnner')} times""")

#========= reverse method
# tasks.reverse()
# print(tasks)
# ['dinner', 'dinner', 'Vacuum', 'Dinner', 'Laundry', 'Food', 'Trash']

#========= sort method
numbers = [1, 2, 3, 4, 5, 6, -7, -8, 9, 10]
print("Before Sorting",numbers)
print("After Sorted",sorted(numbers))
numbers.sort()
numbers.sort(reverse=True)
print("After Sorting",numbers)

nums= [1, 2, 3, 4]
nums.extend([5, 6, 7])
print(nums)