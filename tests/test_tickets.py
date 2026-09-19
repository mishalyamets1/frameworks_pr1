from datetime import date

from tickets import (
    add_comment,
    create_request,
    executor_and_update_status,
)


def test_create_request():
    requests = []
    request = create_request(
        requests,
        room_id=1,
        category="сантехника",
        description="Протечка крана",
        priority="высокий",
        created_date=date(2026, 9, 10),
    )
    assert len(requests) == 1
    assert request["status"] == "новая"


def test_executor_and_update_status():
    status, executor, message = executor_and_update_status(
        "новая",
        "Иванов А.С.",
        "в работе",
    )
    assert status == "в работе"
    assert executor == "Иванов А.С."
    assert "назначен" in message


def test_add_comment():
    comment, message = add_comment("", "Работы начаты")
    assert comment == "Работы начаты"
    assert message == "Комментарий добавлен"
