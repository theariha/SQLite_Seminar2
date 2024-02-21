import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='calorie_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params is not None:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

class IngredientService:
    def __init__(self, db):
        self.db = db

    def find_calories_by_ingredient(self, ingredient_name):
        query = """
            SELECT Products.CaloriesPer100g
            FROM Products
            WHERE Products.ProductName = ?
        """
        result = self.db.execute_query(query, (ingredient_name,))
        return result[0][0] if result else None

class MealService:
    def __init__(self, db):
        self.db = db

    def get_ingredients_by_meal(self, meal_name):
        query = """
            SELECT Products.ProductName, Meals.MealName 
            FROM Products
            JOIN MealComponents ON Products.ProductID = MealComponents.ProductID
            JOIN Meals ON MealComponents.MealID = Meals.MealID
            WHERE Meals.MealName LIKE ?
        """
        result = self.db.execute_query(query, (f"%{meal_name}%",))

        if result:
            meals_ingredients = {}
            for row in result:
                if row[1] in meals_ingredients:
                    meals_ingredients[row[1]].append(row[0])
                else:
                    meals_ingredients[row[1]] = [row[0]]
            return meals_ingredients
        else:
            return None

    def calculate_calories_for_meal(self, meal_name):
        query = """
            SELECT SUM(Products.CaloriesPer100g * MealComponents.Quantity / 100)
            FROM Meals
            JOIN MealComponents ON Meals.MealID = MealComponents.MealID
            JOIN Products ON MealComponents.ProductID = Products.ProductID
            WHERE Meals.MealName = ?
        """
        result = self.db.execute_query(query, (meal_name,))
        return result[0][0] if result else None

class ConsolePrinter:
    @staticmethod
    def print_result(message):
        print(message)

class Application:
    def __init__(self, ingredient_service, meal_service, printer):
        self.ingredient_service = ingredient_service
        self.meal_service = meal_service
        self.printer = printer

    def run(self):
        while True:
            print("\nВыберите действие:")
            print("1. Найти количество калорий в ингредиенте")
            print("2. Получить ингредиенты в блюде")
            print("3. Рассчитать общее количество калорий в блюде")
            print("0. Выход")

            choice = input("Введите номер действия: ")

            if choice == '0':
                break

            user_input = input("Введите название: ").capitalize()

            if choice == '1':
                calories = self.ingredient_service.find_calories_by_ingredient(user_input)
                self.printer.print_result(f"Количество калорий в {user_input}: {calories} ккал на 100 грамм" if calories is not None else f"Ингредиент {user_input} не найден")
            elif choice == '2':
                result = self.meal_service.get_ingredients_by_meal(user_input)
                if result:
                    for meal_name, ingredients in result.items():
                        self.printer.print_result(f"Ингредиенты в блюде '{meal_name}':")
                        for ingredient in ingredients:
                            self.printer.print_result(f"---{ingredient}")
                else:
                    self.printer.print_result(f"Блюдо '{user_input}' не найдено")
            elif choice == '3':
                total_calories = self.meal_service.calculate_calories_for_meal(user_input)
                self.printer.print_result(f"Общее количество калорий в блюде '{user_input}': {total_calories} ккал" if total_calories is not None else f"Блюдо '{user_input}' не найдено")
            else:
                self.printer.print_result("Некорректный ввод. Пожалуйста, выберите корректное действие.")


db = DatabaseConnection()
ingredient_service = IngredientService(db)
meal_service = MealService(db)
printer = ConsolePrinter()
app = Application(ingredient_service, meal_service, printer)
app.run()
db.close_connection()
