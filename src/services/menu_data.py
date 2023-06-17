import csv
from models.dish import Dish
from models.ingredient import Ingredient
# https://docs.python.org/3/library/csv.html#csv.DictReader


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set(self._load_menu(source_path))

    def _load_menu(self, source_path: str):

        if not source_path or not source_path.endswith('.csv'):
            raise ValueError('Invalid source path')

        with open(source_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            dishes = {}
            for row in reader:
                if row['dish'] not in dishes:
                    dish = Dish(row['dish'], float(row['price']))
                    dishes[row['dish']] = dish
                dishes[row['dish']].add_ingredient_dependency(
                    Ingredient(row['ingredient']),
                    int(row['recipe_amount']))

        return dishes.values()
