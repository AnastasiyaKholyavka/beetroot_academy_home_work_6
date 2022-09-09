'''
anastasiya_kholyavka
HW_6_task_3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all 
integers from the list that are divisible by 7 but not a multiple of 5, 
and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration

'''
'''
Псевдокод:
    1. Створюємо список
    2. Знайти всі числа, які діляться на 7
    Для цього потрібно могти викликати для перевірки кожне число. 
    Як називати кожне чило?
    Чи можна задати щось як "х" у рівнянні?
    3. Якщо х ділиться на 7 і не кратне 5, то внести х у новий список.
    
'''
# Не можу виконати

numbers = list(range(1, 101))
new_numbers = list(numbers.sort( // 7) and numbers.sort( % 5))