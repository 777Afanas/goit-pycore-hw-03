import random

# Функція, що повертатє випадковий набір унікальних чисел у межах визначеного діапазону
def get_numbers_ticket(min, max, quantity):     
    if (min >= 1 or max <= 1000) or  (quantity > (max - min + 1)):            
        return []
    else:
        numeric_list = random.sample (range (min, max), quantity)
        return sorted(numeric_list)
        

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
lottery_numbers = get_numbers_ticket(10, 11, 6)
print("Ваші лотерейні числа:", lottery_numbers)

