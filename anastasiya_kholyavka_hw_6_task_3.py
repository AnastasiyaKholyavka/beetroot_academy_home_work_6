'''
anastasiya_kholyavka
HW_6_task_3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all 
integers from the list that are divisible by 7 but not a multiple of 5, 
and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration

'''
# Змогла зробити тільки після пояснення на уроці :(

first_list = list(range(1,101))
second_list = []

i = 1 

while i < len(first_list):
    if first_list[i] % 7 == 0 and first_list[i] % 5 != 0:
        second_list.append(first_list[i])
    i += 1

print(second_list)
