import pytest

from app.use_cases.create_habit import create_habit


def test_create_valid_habit():
    habit = create_habit("Agua", "litros", 2.0, "agua")
    assert habit.name == "Agua"
    assert habit.unit == "litros"
    assert habit.goal == 2.0
    assert habit.type_ == "agua"


def test_create_habit_with_missing_fields():
    with pytest.raises(ValueError):
        create_habit("", "litros", 2.0, "agua")


def test_create_habit_with_invalid_goal():
    with pytest.raises(ValueError):
        create_habit("Dormir", "horas", -8, "sueño")
