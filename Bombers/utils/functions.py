import sys
import os
import platform

import random

from fake_useragent import UserAgent

from typing import Union

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
    return [f for f in os.listdir('Bombers/') if f.endswith(".py") and f != '__init__.py']

def super_input(**kwargs) -> Union[str, int, None]:
    from .decorations import FormattingOptions

    fo = FormattingOptions()
    i = None
    while True:
        try:
            value = input(kwargs['text'])
            if value.lower() in ['exit', 'back', 'chqish', 'quit']:
                clear_terminal()
                sys.exit()
            if kwargs['phone']:
                num = value
                i = num.replace('+998', '') \
                    if num.startswith('+998') \
                    else num
                if i.isdigit() and len(i) == 9:
                    break
                print(fo._(fo.FAIL, "Xato kiritildi!"))
                continue
            elif kwargs['amount']:
                amount = int(value)
                i = amount \
                    if amount <= 1000 and amount >= 10 \
                    else 10
                break
            elif kwargs['int_']:
                if value.isdigit() and int(value) > 0 and int(value) <= len(all_bombers()):
                    i = int(value)
                    break
                print(fo._(fo.FAIL, "Xato kiritildi!"))
                continue
        except ValueError:
            print(fo._(fo.FAIL, "Faqat son yozish kerak!")); continue
        except Exception as e:
            print('Siz ssenariyda bo\'lmagan xatolikka yo\'l qo\'ydingiz.\n'
                    'Ana endi mana bu xatolikni tarjima qilib, to\'g\'ri javob bering!\n'
                    f'{e}')
            break

    return i
