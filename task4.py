# Завдання 4

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.



# Вимоги до завдання:

# Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


# Рекомендації для виконання:

# Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт — datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
# Визначте поточну дату системи за допомогою datetime.today().date().
# Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
# Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
# Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
# Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
# Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
# Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.


# Критерії оцінювання:

# Актуальність та коректність визначення днів народження на 7 днів вперед.
# Правильність обробки випадків, коли дні народження припадають на вихідні.
# Читабельність та структурованість коду.


# Приклад:

# Припустимо, у вас є список users:

# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# Використання функції get_upcoming_birthdays:

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)

# Якщо сьогодні 2024.01.22 результатом може бути:

# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
# ]

# Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.18"}
]

DAYS_BD_MAX_RANGE = 7
SATURDAY = 5
SUNDAY = 6

def get_upcoming_birthdays(users):
    upcoming_birthdays = []

    if not isinstance(users, list):
        print('Users parameter should be a list')
        return upcoming_birthdays

    if len(users) == 0:
        print('Users list should not be empty')
        return upcoming_birthdays
        
    today_date = datetime.today().date()
    for user in users:
        try:
            if not user.get("name") or not user.get("birthday") or not isinstance(user["name"], str) or not isinstance(user["birthday"], str):
                print('User should have name and birthday as strings')
                upcoming_birthdays = []
                break

            user_bd_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            next_birthday = datetime(today_date.year, user_bd_date.month, user_bd_date.day).date()
            if next_birthday < today_date:
                next_birthday = datetime(
                    today_date.year + 1,
                    user_bd_date.month,
                    user_bd_date.day
                ).date()

            days_until_birthday = (next_birthday - today_date).days
            if days_until_birthday <= DAYS_BD_MAX_RANGE:
                birthday_weekday = next_birthday.weekday()

                if birthday_weekday == SATURDAY:
                    next_birthday = next_birthday + timedelta(days=2)
                elif birthday_weekday == SUNDAY:
                    next_birthday = next_birthday + timedelta(days=1)

                upcoming_birthdays.append({"name": user["name"], "congratulation_date": next_birthday.strftime("%Y.%m.%d")}) 
        except ValueError:
            print("Birthday date is not in required format - YYYY.MM.DD")
            upcoming_birthdays = []
            break
    return upcoming_birthdays




upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.30"}
]))

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.09.30"}
]))

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.16"},
    {"name": "Jane Smith", "birthday": "1990.09.30"}
]))

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.16"},
    {"birthday": "1990.09.30"}
]))

print(get_upcoming_birthdays([]))
print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.16"},
    {"name": 214124, "birthday": "1990.09.30"}
]))

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": 12412412},
    {"name": "Jane Smith", "birthday": "1990.09.30"}
]))

print(get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985106"},
    {"name": "Jane Smith", "birthday": "1990.09.30"}
]))