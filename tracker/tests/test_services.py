import pytest
from unittest.mock import Mock, patch

from ..services import IngredientService
from ..database import DatabaseConnection


@pytest.fixture
def mocked_db():
    return Mock(spec=DatabaseConnection)


def test_find_calories_by_ingredient(mocked_db):
    mocked_db.execute_query.return_value = [(50,)]  # Mocking the database response
    ingredient_service = IngredientService(mocked_db)
    calories = ingredient_service.find_calories_by_ingredient("Carrot")
    assert calories == 50