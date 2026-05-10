# Проект FitLife - MVP версия 1.0


# 1. Знакомство

print('Привет, это бот FitLife!')

name = input('Введи свое имя:')
name = name.title()
user_name = name
print(f'Привет, {user_name}!')

user_age = int(input('Введи свой возраст:'))


# 2. Сбор данных

user_weight = float(input('Введи свой вес в кг:'))
while True:
    user_height = input('Введи свой рост в м (например: 1.70):')
    try:
        user_height = float(user_height)
        if user_height < 100:
            break
        else:
            print('Убедись, что введено значение в метрах (используй точку)')
    except ValueError:
        print('Введи числовое значение в метрах (используй точку)')


# 3. Расчеты:
#  Индекса массы тела (ИМТ)
BMI = user_weight / (user_height ** 2)

# Расчет нормы потребления воды
# Объявляем константы:
ML_PER_KG = 30
ML_TO_L = 1000
water_needed = user_weight * ML_PER_KG / ML_TO_L

# Отчет

print(f'Отчет для пользователя: {user_name} {user_age} г.', f'ИМТ: {BMI:.1f}',
      f'Рекомендуемая норма воды: {water_needed:.1f} л. в день',
      'Расчет окончен. Будьте здоровы!', sep='\n')
