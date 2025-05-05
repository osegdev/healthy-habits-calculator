from datetime import date
from app.domain.habit import Habit
from app.domain.record import Record
from app.services.statistics import summarize_records

def test_summarize_records_end_to_end():
    records = [
        Record("Agua", 2.0, date.today()),
        Record("Agua", 2.5, date.today()),
        Record("Pasos", 3000, date.today())
    ]
    summary = summarize_records(records)
    assert "Agua" in summary
    assert "Pasos" in summary
    assert "promedio" in summary