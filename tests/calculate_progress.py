def test_calculate_progress():
    h = Habit("Agua", "litros", 2.0, "agua")
    r = Record("Agua", 1.5, date.today())
    result = calculate_progress(r, [h])
    assert "75%" in result