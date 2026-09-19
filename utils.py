"""Вспомогательные функции ввода."""

from datetime import datetime


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str):
    """Запросить у пользователя дату в формате ДД.ММ.ГГГГ."""
    while True:
        try:
            value = input(prompt)
            return datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            print("Ошибка: используйте формат ДД.ММ.ГГГГ.")
