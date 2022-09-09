'''
anastasiya_kholyavka
HW_6_task_1

The greatest number

Write a Python program to get the largest number from a list of 
random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers

'''
import random

# Не змогла зробити список випадкових чисел по-іншому :(
# Не зрозуміла як використати while loop :( Дмитро показав своє завдання, але моє теж працює без вайл

numbers = [(random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9))]
print('Список випадкових чисел: ' + str(numbers))
print('Найбільше з них: ' + str(max(numbers)))