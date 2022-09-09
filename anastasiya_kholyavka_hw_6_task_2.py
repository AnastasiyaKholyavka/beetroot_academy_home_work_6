'''
anastasiya_kholyavka
HW_6_task_2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers between 
the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers

'''
import random

# Не змогла зробити список випадкових чисел по-іншому :(
# Не зрозуміла як використати while loop :( І без вайл працює, але мабуть щось не так.

numbers_1 = [(random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10))]
numbers_2 = [(random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10))]

numbers_3 = set((numbers_1) + (numbers_2))

print('Перший список випадкових чисел: ' + str(numbers_1))
print('Другий список випадкових чисел: ' + str(numbers_2))
print('Поєднання двох попередніх списків без дублікатів: ' + str(list(numbers_3))) 