from datetime import datetime 
# Функція, яка розраховує кількість днів між заданою датою і поточною датою.
def get_days_from_today(date):        
    try: 
        entered_date = datetime.strptime(date, "%Y-%m-%d").date() 
        current_date = datetime.today().date() 
        days_since = current_date.toordinal() - entered_date.toordinal()    
        return days_since
    except ValueError:
        return None     

# Запит з перевіркою формату вхідних даних
while True:
     user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

     if get_days_from_today(user_input) is not None:
        print(f"Кількість днів між {user_input} та сьогодні: {get_days_from_today(user_input)}")
        break
     else:
        print("Неправильний формат дати. Спробуйте ще раз (приклад: 2023-03-13).")


 