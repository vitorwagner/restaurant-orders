from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    cheese_1 = Ingredient("queijo gorgonzola")
    cheese_2 = Ingredient("queijo gorgonzola")
    ham_1 = Ingredient("presunto")

    assert cheese_1.name == "queijo gorgonzola"
    assert cheese_1.restrictions == {Restriction.LACTOSE,
                                     Restriction.ANIMAL_DERIVED}
    assert repr(cheese_1) == "Ingredient('queijo gorgonzola')"
    assert hash(cheese_1) == hash("queijo gorgonzola")
    assert hash(cheese_1) == hash(cheese_2)
    assert hash(cheese_1) != hash(ham_1)
    assert cheese_1 == cheese_2

    with pytest.raises(TypeError):
        Ingredient()
