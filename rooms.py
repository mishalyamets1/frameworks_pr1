"""Функции для работы с помещениями."""


def add_room(
    rooms: dict[int, dict],
    name: str,
    floor: int,
    room_type: str,
) -> None:
    """Добавить помещение в словарь rooms."""
    room_id = max(rooms.keys(), default=0) + 1
    rooms[room_id] = {
        "id": room_id,
        "name": name,
        "floor": floor,
        "type": room_type,
    }


def find_room(rooms: dict[int, dict], query: str) -> list[dict]:
    """Найти помещения по подстроке названия."""
    query = query.lower()
    result = []
    for room in rooms.values():
        if query in room["name"].lower():
            result.append(room)
    return result
