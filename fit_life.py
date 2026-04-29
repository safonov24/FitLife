# Проект FitLife - MVP версия 1.0

print('Привет! Предлагаю сразу на "ты"\n')
# Спрашиваем имя и сохраняем в переменную user_name
user_name = input('Как тебя зовут?\n')
print()
# Узнаем возраст и сохранияем в переменную user_age
user_age = int(input('Сколько тебе лет?\n'))
print()
# Спрашиваем вес (в кг) и сохраняем в user_weight
user_weight = float(input('Какой у тебя вес в кг?\n'))
print()
# Узнаем рост в метрах
user_height = float(input('Какой у тебя рост в метрах? Например, 1.75\n'))
print()
# Рассчитаваем bmi (Индекс массы тела)
bmi = round(user_weight / user_height ** 2, 1)
# Рассчитываем норму воды - water_needed
water_needed = (user_weight * 30) / 1000
# Выводим результат
print(f'Привет, {user_name}! Твой отчет готов.')
print(f'Возраст: {user_age}\n'
      f'Индекс массы тела: {bmi}\n'
      f'Рекомендуемая норма'
      f' воды {water_needed} л. в день\n\n'
      f'Расчет окончен. Будь здоров!')
