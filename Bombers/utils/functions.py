import os
import platform

import random

from fake_useragent import UserAgent

ua = UserAgent()


def clear_terminal() -> int:
    os.system("cls") if platform.system().lower() == "windows" else os.system("clear")


def random_names() -> str:
    return random.choice(
        [
            'To\'lqin', 'Shirinbek', 'Hayotbek',
            'Zaynab', 'Shilqimbek', 'Jamila',
            'Temur', 'Kamol', 'Nazriddin', 'O\'lmas',
            'O\'roq', 'Parvozbek', 'Misha', 'Omadbek',
            'Qalqon', 'Olmosbek', 'Zavqiddin', 'Qimmat',
            'Toshtemir', 'Boymurod', 'Yusuf-M249', 'Oyjamol'
        ]
    )


def random_user_agent() -> str:
    return ua.random


def all_bombers() -> list:
    return [f for f in os.listdir('Bombers/') if f.endswith(".py")]
