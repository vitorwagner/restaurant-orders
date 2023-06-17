from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasagna = Dish("lasanha", 10.0)
    ravioli = Dish("ravioli", 10.0)
    cheese = Ingredient("queijo gorgonzola")
    ham = Ingredient("presunto")

    assert lasagna.name == "lasanha"
    assert lasagna.price == 10.0
    assert lasagna.recipe == {}
    assert repr(lasagna) == "Dish('lasanha', R$10.00)"
    assert hash(lasagna) == hash("Dish('lasanha', R$10.00)")

    lasagna.add_ingredient_dependency(cheese, 2)
    lasagna.add_ingredient_dependency(ham, 1)
    assert lasagna.recipe == {cheese: 2, ham: 1}

    assert lasagna.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert lasagna.get_ingredients() == {cheese, ham}

    assert lasagna == Dish("lasanha", 10.0)
    assert lasagna != ravioli

    with pytest.raises(TypeError):
        Dish("lasanha", "10.0")

    with pytest.raises(ValueError):
        Dish("lasanha", -10.0)
