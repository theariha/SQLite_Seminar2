
from functions import *

while True:
    print("\nВыберите действие:")
    print("1. Найти количество калорий в ингредиенте")
    print("2. Получить ингредиенты в блюде")
    print("3. Рассчитать общее количество калорий в блюде")
    print("0. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        ingredient_name = input("Введите название ингредиента: ").capitalize()
        calories = find_calories_by_ingredient(ingredient_name)
        if calories is not None:
            print(f"Количество калорий в {ingredient_name}: {calories} ккал на 100 грамм")
        else:
            print(f"Ингредиент {ingredient_name} не найден")

    elif choice == '2':
        meal_name = input("Введите название блюда: ").capitalize()
        meal_ingredients = get_ingredients_by_meal(meal_name)
        if meal_ingredients:
            for meal_name in meal_ingredients.keys():
                print(f"Ингредиенты в блюде '{meal_name}':")
                for ingredient in meal_ingredients[meal_name]:
                    print(f"---{ingredient}")
        else:
            print(f"Блюдо '{meal_name}' не найдено")

    elif choice == '3':
        meal_name = input("Введите название блюда: ").capitalize()
        total_calories = calculate_calories_for_meal(meal_name)
        if total_calories is not None:
            print(f"Общее количество калорий в блюде '{meal_name}': {total_calories} ккал")
        else:
            print(f"Блюдо '{meal_name}' не найдено")

    elif choice == '0':
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите корректное действие.")