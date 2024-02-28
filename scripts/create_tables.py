import sqlite3

# 1. Создать подключение к базе данных
conn = sqlite3.connect('calorie_tracker.db')

# 2. Создать курсор
cursor = conn.cursor()

# 3. Создать таблицу Products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT,
        CaloriesPer100g REAL
    )
''')

# 4. Создать таблицу Meals
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Meals (
        MealID INTEGER PRIMARY KEY,
        MealName TEXT
    )
''')

# 5. Создать таблицу MealComponents
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MealComponents (
        ComponentID INTEGER PRIMARY KEY,
        MealID INTEGER,
        ProductID INTEGER,
        Quantity REAL,
        FOREIGN KEY (MealID) REFERENCES Meals(MealID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
''')

# 6. Закрыть соединение с базой данных
conn.commit()
conn.close()