import sqlite3

'''
Функция для расчета калорий на 100 гр продукта.
На вход принимает название продукта.
Возращает число - количество калорий на 100гр, если продукт найден в БД.
Иначе None
'''
def find_calories_by_ingredient(ingredient_name):
    ################################################################################################
    ### Задание 1. Напишите функцию, которая по названию продукта выводит количество калорий в нем.
    ################################################################################################
    conn = sqlite3.connect('calorie_tracker.db')
    cursor = conn.cursor()
    query = """
        SELECT Products.CaloriesPer100g 
        FROM Products
        WHERE Products.ProductName = ?
    """
    cursor.execute(query, (ingredient_name, ))
    
    ### fetchone 
    result = cursor.fetchone()[0]
    
    if result:
        return result
    else:
        return None


'''
Функция для вывода ингредиентов заданного блюда.
На вход принимает название блюда. Или часть названия блюда.
Если хотя бы одно блюдо найдено в БД, возращает словарь формата: 
{
    блюдо1: [ингредиент1, ингредиент2], 
    блюдоn: [ингредиентX, ингредиентY]
}.
Иначе None.
'''
def get_ingredients_by_meal(meal_name):
    conn = sqlite3.connect('calorie_tracker.db')  
    cursor = conn.cursor()

    try:
        query = """
            SELECT Products.ProductName, Meals.MealName 
            FROM Products
            JOIN MealComponents ON Products.ProductID = MealComponents.ProductID
            JOIN Meals ON MealComponents.MealID = Meals.MealID
            WHERE Meals.MealName LIKE ?
        """

        cursor.execute(query, (f"%{meal_name}%",))        
        ##################################################################    
        ### Задание 2. Обработайте и верните значения в корректном формате.
        ##################################################################
        result = cursor.fetchall()

        if result:
            res_dict = {}
            for row in result:
                if row[1] in res_dict.keys():
                    res_dict[row[1]].append(row[0])
                else:
                    res_dict[row[1]] = [row[0]]
            return res_dict
        else:
            return None

    finally:
        # Закрытие соединения с базой данных
        conn.close()


'''
Функция для подсчета калорий во всем блюде.
На вход принимает название блюда полностью и проверяет только полное совпадение с названием в БД.
Возвращает общее количество калорий в блюде, если оно найдено в БД.
Иначе None. 
'''
def calculate_calories_for_meal(meal_name):
#     # Подключение к базе данных
#     conn = sqlite3.connect('calorie_tracker.db')  
#     cursor = conn.cursor()

#     try:
#         ###################################################################################
#         # Задание 3. Напишите запрос для получения общего количества калорий в блюде
#         ###################################################################################

#         # Выполнение запроса с параметром
#         cursor.execute(query, (meal_name,))

#         # Получение результата
#         result = cursor.fetchone()

#         if result:
#             return result[0]  # Возвращаем общее количество калорий в блюде
#         else:
#             return None  # Блюдо не найдено

#     finally:
#         # Закрытие соединения с базой данных
#         conn.close()

