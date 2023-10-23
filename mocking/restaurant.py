import json
import random
import os



class Waiter:

    def getOrder(self):
        print("Waiter: Get order")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        meals_file_path = os.path.join(dir_path, 'meals.json')
        with open(meals_file_path, 'r') as f:
            meal_list = json.load(f)
        simplified_meal_list = [meal["name"] for meal in meal_list["meals"]]
        return random.choice(simplified_meal_list)
