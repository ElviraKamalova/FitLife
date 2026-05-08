# Проект FitLife - MVP версия 1.0


# 1. Знакомство

print('Привет, это бот FitLife!')

name = input('Введи свое имя:')
name = name.title()
user_name = name
print(f'Привет, {user_name}!')

age = input('Введи свой возраст:')
user_age = int(age)


# 2. Сбор данных

weight = input('Введи свой вес в кг:')
user_weght = float(weight)

height = input('Введи свой рост в м (например, 1.70):')
user_height = float(height)


# 3. Расчеты:

#  Индекса массы тела (ИМТ)
BMI = user_weght / (user_height ** 2)

# Расчет нормы потребления воды
water_needed = (user_weght * 30) / 1000

# Отчет

print(f'Отчет для пользователя: {user_name},  ({user_age} г.)')
print(f'ИМТ: {round(BMI, 1)}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день.')

print("Расчет окончен. Будьте здоровы!")
