from datetime import date


request_id = 1001
room_name = "Офис 205"
floor = 2
category = "сантехника"
description = "Протечка крана у раковины"
priority = "высокий"
status = "новая"
created_date = date(2026, 9, 10)
executor_name = ""
comment = ""


def create_request_details(
    request_id,
    room_name,
    floor,
    category,
    description,
    priority,
    status,
    created_date,
):
    """Создание и отображение заявки на обслуживание помещения."""
    request_number = str(request_id)
    floor_info = str(floor)
    return (
        f"Заявка №{request_number}\n"
        f"Помещение: {room_name} (этаж {floor_info})\n"
        f"Категория: {category}\n"
        f"Описание: {description}\n"
        f"Приоритет: {priority}\n"
        f"Статус: {status}\n"
        f"Дата создания: {created_date}"
    )


def executor_and_update_status(current_status, executor, new_status):
    """Назначение исполнителя и изменение статуса заявки."""
    if current_status == "отклонена":
        return current_status, executor, "Нельзя изменить отклонённую заявку"
    if current_status == "выполнена":
        return current_status, executor, "Заявка уже выполнена"
    if executor == "":
        return current_status, executor, "Исполнитель не указан"
    if new_status not in ("новая", "в работе", "выполнена", "отклонена"):
        return current_status, executor, "Недопустимый статус"
    return new_status, executor, f"Исполнитель {executor} назначен, статус изменён на «{new_status}»"


def add_comment(existing_comment, new_comment):
    """Добавление комментария к заявке для отслеживания хода выполнения."""
    if new_comment == "":
        return existing_comment, "Комментарий не может быть пустым"
    if existing_comment == "":
        return new_comment, "Комментарий добавлен"
    updated_comment = existing_comment + " | " + new_comment
    return updated_comment, "Комментарий добавлен"



print("--- Создание заявки ---")
print(create_request_details(
    request_id, room_name, floor, category, description, priority, status, created_date
))


print()
print("--- Назначение исполнителя ---")
executor_name = "Иванов А.С."
status, executor_name, assign_message = executor_and_update_status(
    status, executor_name, "в работе"
)
print(assign_message)

print()
print("--- Добавление комментария ---")
comment, comment_message = add_comment(comment, "Запчасти заказаны, работы начнутся завтра")
print(comment_message)
print(f"Комментарии: {comment}")

