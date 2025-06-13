from datetime import datetime, timedelta

# Функція що повертає список днів народження вперед на 7 днів, включаючи поточний день
def get_upcoming_birthdays(users):
    # список дат привітань вперед на 7 днів (включаючи поточну дату)
    congratulation_dates = []

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Проходимо по списку користувачів
    for user in users:
        # Конвертуємо дату народження у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Створення дати народження поточного року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, перенесення на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Перевірка, чи припадає день народження на наступний тиждень (1-7 днів)
        if today <= birthday_this_year <= today + timedelta(days=6):
            # Перевірка, чи припадає день народження на вихідні (субота / неділя)
            if birthday_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
                # Якщо так, переносимо на наступний понеділок
                days_to_next_monday = 7 - birthday_this_year.weekday()
                birthday_this_year += timedelta(days=days_to_next_monday)
            
            # Виведення списку словників з іменами користувачів та датами привітань
            congratulation_dates.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return congratulation_dates

# Приклад користувачів
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Tom Harris", "birthday": "1992.06.15"},
    {"name": "Olivia Taylor", "birthday": "1989.06.19"},
    {"name": "Sarah Davis", "birthday": "1988.06.20"},
    {"name": "Michael Brown", "birthday": "1993.06.21"},
    {"name": "Alice Brown", "birthday": "1980.05.12"}
]

# Використання функції 
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)