import json
from datetime import date
from typing import List
import csv
from datetime import datetime
import shutil

from app.domain.habit import Habit
from app.domain.record import Record

HABITS_FILE = "habits.json"
RECORDS_FILE = "records.json"


def habit_to_dict(habit: Habit) -> dict:
    return habit.__dict__


def record_to_dict(record: Record) -> dict:
    return {
        "habit_name": record.habit_name,
        "value": record.value,
        "record_date": record.record_date.isoformat(),
    }


def dict_to_habit(data: dict) -> Habit:
    return Habit(**data)


def dict_to_record(data: dict) -> Record:
    return Record(
        habit_name=data["habit_name"],
        value=data["value"],
        record_date=date.fromisoformat(data["record_date"]),
    )


def save_habits(habits: List[Habit]):
    with open(HABITS_FILE, "w") as f:
        json.dump([habit_to_dict(h) for h in habits], f, indent=2)


def save_records(records: List[Record]):
    with open(RECORDS_FILE, "w") as f:
        json.dump([record_to_dict(r) for r in records], f, indent=2)


def load_habits() -> List[Habit]:
    try:
        with open(HABITS_FILE, "r") as f:
            data = json.load(f)
            return [dict_to_habit(d) for d in data]
    except FileNotFoundError:
        return []


def load_records() -> List[Record]:
    try:
        with open(RECORDS_FILE, "r") as f:
            data = json.load(f)
            return [dict_to_record(d) for d in data]
    except FileNotFoundError:
        return []

EXPORTS_FOLDER = "exports/"
BACKUPS_FOLDER = "backups/"

def export_records_to_csv(records: List[Record], filename="records_export.csv"):
    import os
    os.makedirs(EXPORTS_FOLDER, exist_ok=True)
    filepath = os.path.join(EXPORTS_FOLDER, filename)
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["habit_name", "value", "record_date"])
        for r in records:
            writer.writerow([r.habit_name, r.value, r.record_date.isoformat()])

def backup_data():
    import os
    os.makedirs(BACKUPS_FOLDER, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if os.path.exists("habits.json"):
        shutil.copy("habits.json", f"{BACKUPS_FOLDER}/habits_{timestamp}.json")
    if os.path.exists("records.json"):
        shutil.copy("records.json", f"{BACKUPS_FOLDER}/records_{timestamp}.json")