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