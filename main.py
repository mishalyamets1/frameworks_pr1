"""Точка запуска приложения."""

from pathlib import Path

import tickets
import rooms
import storage
import utils

DATA_DIR = Path(__file__).parent / "data"
ROOMS_FILE = DATA_DIR / "rooms.json"
REQUESTS_FILE = DATA_DIR / "requests.json"


def show_rooms(rooms_data: dict[int, dict]) -> None:
    """Вывести список помещений."""
    for room in rooms_data.values():
        print(
            f"№{room['id']}: {room['name']} "
            f"(этаж {room['floor']}, {room['type']})"
        )


def show_requests(
    requests: list[dict],
    rooms_data: dict[int, dict],
) -> None:
    """Вывести список заявок."""
    for item in requests:
        room = rooms_data.get(item["room_id"], {})
        print(
            tickets.create_request_details(
                item["id"],
                room.get("name", "неизвестно"),
                room.get("floor", 0),
                item["category"],
                item["description"],
                item["priority"],
                item["status"],
                item["created_date"],
            )
        )
        print("-" * 30)


def main() -> None:
    """Точка запуска приложения."""
    rooms_data = storage.load_rooms(ROOMS_FILE)
    requests = storage.load_requests(REQUESTS_FILE)

    while True:
        print("\n=== Система учета заявок на обслуживание ===")
        print("1. Показать помещения")
        print("2. Добавить помещение")
        print("3. Найти помещение")
        print("4. Показать заявки")
        print("5. Создать заявку")
        print("6. Назначить исполнителя / изменить статус")
        print("7. Добавить комментарий")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_rooms(rooms_data)

        elif choice == "2":
            name = input("Название: ")
            floor = utils.input_int("Этаж: ")
            room_type = input("Тип (офис, переговорная и т.д.): ")
            rooms.add_room(rooms_data, name, floor, room_type)
            storage.save_rooms(ROOMS_FILE, rooms_data)
            print("Помещение добавлено.")

        elif choice == "3":
            query = input("Название помещения: ")
            found = rooms.find_room(rooms_data, query)
            for room in found:
                print(f"№{room['id']}: {room['name']}")

        elif choice == "4":
            show_requests(requests, rooms_data)

        elif choice == "5":
            room_id = utils.input_int("ID помещения: ")
            category = input("Категория: ")
            description = input("Описание: ")
            priority = input("Приоритет: ")
            created_date = utils.input_date("Дата (ДД.ММ.ГГГГ): ")
            tickets.create_request(
                requests, room_id, category, description,
                priority, created_date,
            )
            storage.save_requests(REQUESTS_FILE, requests)
            print("Заявка создана.")

        elif choice == "6":
            request_id = utils.input_int("ID заявки: ")
            for item in requests:
                if item["id"] == request_id:
                    executor = input("Исполнитель: ")
                    new_status = input("Новый статус: ")
                    status, executor, message = (
                        tickets.executor_and_update_status(
                            item["status"], executor, new_status,
                        )
                    )
                    item["status"] = status
                    item["executor"] = executor
                    print(message)
                    storage.save_requests(REQUESTS_FILE, requests)
                    break
            else:
                print("Заявка не найдена.")

        elif choice == "7":
            request_id = utils.input_int("ID заявки: ")
            for item in requests:
                if item["id"] == request_id:
                    new_comment = input("Комментарий: ")
                    comment, message = tickets.add_comment(
                        item["comment"], new_comment,
                    )
                    item["comment"] = comment
                    print(message)
                    storage.save_requests(REQUESTS_FILE, requests)
                    break
            else:
                print("Заявка не найдена.")

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
