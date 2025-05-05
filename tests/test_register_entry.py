from datetime import date

import pytest

from app.use_cases.register_entry import register_entry


def test_register_valid_entry():
    record = register_entry("Agua", 2.0, date(2025, 5, 5))
    assert record.habit_name == "Agua"
    assert record.value == 2.0
    assert record.record_date == date(2025, 5, 5)


def test_register_entry_with_negative_value():
    with pytest.raises(ValueError):
        register_entry("Agua", -1.0, date.today())


def test_register_entry_with_empty_name():
    with pytest.raises(ValueError):
        register_entry("", 2.0, date.today())
