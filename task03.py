import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
# Функція, що нормалізує телефонні номери до стандартного формату - тільки цифри та символ '+' на початку
def normalize_phone(phone_number): 
    # Залишаємо лише цифри та +
    standard_phone_number = re.sub(r"[^\d+]", "", phone_number)
    # Якщо номер починається з '+'
    if standard_phone_number.startswith('+'):
        if standard_phone_number.startswith('+380'):
            return standard_phone_number
        else:
            return standard_phone_number 
    else:
        # Якщо номер починається з '380' — додаємо тільки '+'
        if standard_phone_number.startswith('380'):
            return '+' + standard_phone_number
        else:
            return '+38' + standard_phone_number     # Інакше додаємо код країни '+38'
    
sanitized_numbers = [normalize_phone(num) for num in raw_numbers] 
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


  

