"""Функции для работы с заявками на обслуживание."""

from datetime import date


def create_request_details(
    request_id: int,
    room_name: str,
    floor: int,
    category: str,
    description: str,
    priority: str,
    status: str,
    created_date: date,
) -> str:
    """Создание и отображение заявки на обслуживание помещения."""
    return (
        f"Заявка №{request_id}\n"
        f"Помещение: {room_name} (этаж {floor})\n"
        f"Категория: {category}\n"
        f"Описание: {description}\n"
        f"Приоритет: {priority}\n"
        f"Статус: {status}\n"
        f"Дата создания: {created_date}"
    )


def executor_and_update_status(
    current_status: str,
    executor: str,
    new_status: str,
) -> tuple[str, str, str]:
    """Назначение исполнителя и изменение статуса заявки."""
    if current_status == "отклонена":
        return current_status, executor, "Нельзя изменить отклонённую заявку"
    if current_status == "выполнена":
        return current_status, executor, "Заявка уже выполнена"
    if executor == "":
        return current_status, executor, "Исполнитель не указан"
    if new_status not in ("новая", "в работе", "выполнена", "отклонена"):
        return current_status, executor, "Недопустимый статус"
    message = (
        f"Исполнитель {executor} назначен, "
        f"статус изменён на «{new_status}»"
    )
    return new_status, executor, message


def add_comment(
    existing_comment: str,
    new_comment: str,
) -> tuple[str, str]:
    """Добавление комментария к заявке."""
    if new_comment == "":
        return existing_comment, "Комментарий не может быть пустым"
    if existing_comment == "":
        return new_comment, "Комментарий добавлен"
    return existing_comment + " | " + new_comment, "Комментарий добавлен"


def create_request(
    requests: list[dict],
    room_id: int,
    category: str,
    description: str,
    priority: str,
    created_date: date,
) -> dict:
    """Создать новую заявку и добавить её в список."""
    request_id = max((item["id"] for item in requests), default=1000) + 1
    request = {
        "id": request_id,
        "room_id": room_id,
        "category": category,
        "description": description,
        "priority": priority,
        "status": "новая",
        "executor": "",
        "comment": "",
        "created_date": created_date,
    }
    requests.append(request)
    return request
