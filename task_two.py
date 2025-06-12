import random

def get_numbers_ticket(min, max, quantity): 
    if (min >= 1 & max <= 1000) & (1 <= quantity <= 1000):
        numeric_list = random.sample (range (min, max), quantity)
        return sorted(numeric_list)
    else:
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)