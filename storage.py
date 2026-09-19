"""Загрузка и сохранение данных в JSON-файлах."""

import json
from datetime import date
from pathlib import Path


def load_rooms(filename: str | Path) -> dict[int, dict]:
    """Загрузить помещения из JSON-файла."""
    path = Path(filename)
    try:
        with path.open(encoding="utf-8") as file:
            rooms_list = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise ValueError(f"Некорректный JSON в файле {path}")

    return {room["id"]: room for room in rooms_list}


def save_rooms(filename: str | Path, rooms: dict[int, dict]) -> None:
    """Сохранить помещения в JSON-файл."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(list(rooms.values()), file, ensure_ascii=False, indent=2)


def load_requests(filename: str | Path) -> list[dict]:
    """Загрузить заявки из JSON-файла."""
    path = Path(filename)
    try:
        with path.open(encoding="utf-8") as file:
            requests_list = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError(f"Некорректный JSON в файле {path}")

    for request in requests_list:
        if isinstance(request["created_date"], str):
            request["created_date"] = date.fromisoformat(
                request["created_date"]
            )
    return requests_list


def save_requests(filename: str | Path, requests: list[dict]) -> None:
    """Сохранить заявки в JSON-файл."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for request in requests:
        item = dict(request)
        if isinstance(item["created_date"], date):
            item["created_date"] = item["created_date"].isoformat()
        data.append(item)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
