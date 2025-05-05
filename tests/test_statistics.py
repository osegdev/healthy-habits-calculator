from datetime import date
from app.domain.record import Record
from app.services.statistics import summarize_records

def test_summarize_records():
    records = [
        Record("Agua", 2.0, date(2025, 5, 4)),
        Record("Agua", 3.0, date(2025, 5, 5)),
        Record("Pasos", 1000, date(2025, 5, 5)),
    ]
    result = summarize_records(records)
    assert "Agua" in result
    assert "Pasos" in result
    assert "promedio = 2.50" in result