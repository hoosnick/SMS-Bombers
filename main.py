from Bombers.utils import all_bombers
from Bombers.utils import (clear_terminal, banner, stars)
from Bombers.utils import FormattingOptions

fo = FormattingOptions()


if __name__ == '__main__':
    clear_terminal()
    print(banner('Musaffo SKY'))
    print(fo._(fo.OKGREEN, stars(17, 2)))
    bombers = all_bombers()
    for n, f in enumerate(bombers, start=1):
        print(n, f)