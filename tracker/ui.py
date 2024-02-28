class ConsolePrinter:
    @staticmethod
    def print_result(message):
        print(message)


class Presenter:
    def __init__(self, ingredient_service, meal_service, view):
        self.ingredient_service = ingredient_service
        self.meal_service = meal_service
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()

            choice = self.view.get_user_input()

            if choice == '0':
                break

            user_input = self.view.get_user_input("Введите название: ").capitalize()

            if choice == '1':
                self.view.show_result(
                    f"Количество калорий в {user_input}: {self.ingredient_service.find_calories_by_ingredient(user_input)} ккал на 100 грамм")
            elif choice == '2':
                result = self.meal_service.get_ingredients_by_meal(user_input)
                if result:
                    for meal_name, ingredients in result.items():
                        self.view.show_result(f"Ингредиенты в блюде '{meal_name}':")
                        for ingredient in ingredients:
                            self.view.show_result(f"---{ingredient}")
                else:
                    self.view.show_result(f"Блюдо '{user_input}' не найдено")
            elif choice == '3':
                total_calories = self.meal_service.calculate_calories_for_meal(user_input)
                self.view.show_result(
                    f"Общее количество калорий в блюде '{user_input}': {total_calories} ккал" if total_calories is not None else f"Блюдо '{user_input}' не найдено")
            else:
                self.view.show_result("Некорректный ввод. Пожалуйста, выберите корректное действие.")


class View:
    @staticmethod
    def show_menu():
        print("\nВыберите действие:")
        print("1. Найти количество калорий в ингредиенте")
        print("2. Получить ингредиенты в блюде")
        print("3. Рассчитать общее количество калорий в блюде")
        print("0. Выход")

    @staticmethod
    def get_user_input(prompt="Введите номер действия: "):
        return input(prompt)

    @staticmethod
    def show_result(message):
        print(message)