import json
import os
from datetime import datetime, date
from typing import List, Dict

LOG_DIR = ".devtrack_logs"


def _ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def _get_today_file():
    today = date.today().isoformat()
    return os.path.join(LOG_DIR, f"{today}.json")


def _load_log(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        return json.load(f)


def _save_log(file_path: str, entries: List[Dict]):
    with open(file_path, "w") as f:
        json.dump(entries, f, indent=2)


def log_activity(task_id: int, notes: str) -> Dict:
    """
    Log a development activity for a task.
    """

    _ensure_log_dir()

    file_path = _get_today_file()
    entries = _load_log(file_path)

    entry = {
        "task_id": task_id,
        "notes": notes,
        "timestamp": datetime.now().isoformat(),
    }

    entries.append(entry)
    _save_log(file_path, entries)

    return entry


def get_today_logs() -> List[Dict]:
    """
    Retrieve today's activity logs.
    """

    _ensure_log_dir()

    file_path = _get_today_file()
    return _load_log(file_path)


def get_logs_by_date(log_date: str) -> List[Dict]:
    """
    Retrieve logs for a specific date.
    Date format: YYYY-MM-DD
    """

    _ensure_log_dir()

    file_path = os.path.join(LOG_DIR, f"{log_date}.json")
    return _load_log(file_path)


def get_all_logs() -> Dict[str, List[Dict]]:
    """
    Retrieve all logs grouped by date.
    """

    _ensure_log_dir()

    logs = {}

    for filename in os.listdir(LOG_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(LOG_DIR, filename)
            logs[filename.replace(".json", "")] = _load_log(file_path)

    return logs


def print_today_summary():
    """
    Print a human-readable summary of today's work.
    """

    logs = get_today_logs()

    if not logs:
        print("No work logged today.")
        return

    print("Today's Work Log")
    print("----------------")

    for entry in logs:
        time = entry["timestamp"][11:16]
        print(f"[{time}] Task {entry['task_id']} - {entry['notes']}")
