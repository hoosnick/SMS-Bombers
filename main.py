import requests

from Bombers import *
from Bombers.utils import (clear_terminal, main_menu)
from Bombers.utils import FormattingOptions, super_input

fo = FormattingOptions()
session = requests.session()


def dict_of_bombers():
    return {
        1 : OqtepaLavashBomber,
        2 : TashkentBomber,
        3 : BeelineBomber,
        4 : AbadUzBomber,
    }


def main():
    main_menu()
    _all_bombers = '\n'.join([
        f'{n}| {b.__name__}' for n, b in enumerate(
            iterable=list(dict_of_bombers().values()),
            start=1)])
    while True:
        try:
            bomber = super_input(
                text=fo._(fo.OKBLUE, f'Bomberni tanlang:\n{_all_bombers}\n> '),
                phone=False, amount=False, int_=True)
            phone = super_input(
                text=fo._(fo.OKBLUE, 'Telefon raqamni (+998)siz kiriting (namuna: 991234567)\n> '),
                phone=True, amount=False)
            amount = super_input(
                text=fo._(fo.OKBLUE, 'Nechta SMS borishini istaysiz? (max: 1000)\n> '),
                phone=False, amount=True)
            
            if all([elem is None for elem in [phone, amount]]):
                print(fo._(fo.FAIL, 'Ma\'lumotlar xato kiritildi!')); continue
                
            bomber = dict_of_bombers()[bomber](session)
            bomber.start_bombing(phone, amount)
        except KeyboardInterrupt:
            clear_terminal(); break
        except Exception as e:
            print(fo._(fo.FAIL, f'Qanaqadir noma\'lum, g\'alati xatolik yuz berdi!\n{e}')); break

if __name__ == '__main__':
    main()