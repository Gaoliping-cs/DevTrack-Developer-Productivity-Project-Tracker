import json
import os
from datetime import datetime
from typing import List, Optional

DEVTRACK_FILE = ".devtrack.json"


class Task:
    def __init__(
        self,
        id: int,
        title: str,
        description: str = "",
        status: str = "todo",
        created_at: Optional[str] = None,
        completed_at: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()
        self.completed_at = completed_at
        self.tags = tags or []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "todo"),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at"),
            tags=data.get("tags", []),
        )


def _load_data():
    if not os.path.exists(DEVTRACK_FILE):
        return {"tasks": []}

    with open(DEVTRACK_FILE, "r") as f:
        return json.load(f)


def _save_data(data):
    with open(DEVTRACK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def _get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(title: str, description: str = "") -> Task:
    data = _load_data()

    task_id = _get_next_id(data["tasks"])
    task = Task(id=task_id, title=title, description=description)

    data["tasks"].append(task.to_dict())
    _save_data(data)

    return task


def list_tasks(status: Optional[str] = None, tag: Optional[str] = None) -> List[Task]:
    data = _load_data()
    tasks = [Task.from_dict(t) for t in data["tasks"]]

    if status:
        tasks = [t for t in tasks if t.status == status]

    if tag:
        tasks = [t for t in tasks if tag in t.tags]

    return tasks


def get_task(task_id: int) -> Optional[Task]:
    data = _load_data()

    for t in data["tasks"]:
        if t["id"] == task_id:
            return Task.from_dict(t)

    return None


def update_task(updated_task: Task):
    data = _load_data()

    for i, t in enumerate(data["tasks"]):
        if t["id"] == updated_task.id:
            data["tasks"][i] = updated_task.to_dict()
            break

    _save_data(data)


def start_task(task_id: int) -> Optional[Task]:
    task = get_task(task_id)
    if not task:
        return None

    task.status = "doing"
    update_task(task)
    return task


def complete_task(task_id: int) -> Optional[Task]:
    task = get_task(task_id)
    if not task:
        return None

    task.status = "done"
    task.completed_at = datetime.now().isoformat()

    update_task(task)
    return task


def add_tag(task_id: int, tag: str) -> Optional[Task]:
    task = get_task(task_id)
    if not task:
        return None

    if tag not in task.tags:
        task.tags.append(tag)

    update_task(task)
    return task


def delete_task(task_id: int) -> bool:
    data = _load_data()

    new_tasks = [t for t in data["tasks"] if t["id"] != task_id]

    if len(new_tasks) == len(data["tasks"]):
        return False

    data["tasks"] = new_tasks
    _save_data(data)

    return True
