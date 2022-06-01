import random


class FormattingOptions:
    HEADER = '\033[95m'
    RED = "\033[1;31m"
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    def _(self, format: str, text: str):
        return format + text + self.ENDC

def stars(n: int, s: int = 0): return (' '*s).join(['*' for _ in range(n)]) # line

LIST_OF_BANNERS = [
    """
  ___ __  __ ___   ___ ___  _   __  __ __  __ ___ ___ 
 / __|  \/  / __| / __| _ \/_\ |  \/  |  \/  | __| _ \\
 \__ \ |\/| \__ \ \__ \  _/ _ \| |\/| | |\/| | _||   /
 |___/_|  |_|___/ |___/_|/_/ \_\_|  |_|_|  |_|___|_|_\\

              2022 (c) {}""",
    """
____ _  _ ____    ____ ___  ____ _  _ _  _ ____ ____ 
[__  |\/| [__     [__  |__] |__| |\/| |\/| |___ |__/ 
___] |  | ___]    ___] |    |  | |  | |  | |___ |  \ 

            2022 (c) {}""",
    """
           ____  __  __ ____  
          / ___||  \/  / ___| 
          \___ \| |\/| \___ \ 
           ___) | |  | |___) |
          |____/|_|  |_|____/ 
                              
  ____   ___  __  __ ____  _____ ____  
 | __ ) / _ \|  \/  | __ )| ____|  _ \ 
 |  _ \| | | | |\/| |  _ \|  _| | |_) |
 | |_) | |_| | |  | | |_) | |___|  _ < 
 |____/ \___/|_|  |_|____/|_____|_| \_\\

        2022 (c) {}""",
]


def banner(r: str): return random.choice(LIST_OF_BANNERS).format(r) # random banner

">> https://www.youtube.com/watch?v=VeUlxU2qXDk <<"

fo = FormattingOptions()

def main_menu(): # text
    from .functions import clear_terminal
    
    clear_terminal()
    print(banner('Musaffo SKY'))
    print(
        f'{fo.WARNING}\nMax. 1000ta va min. 10ta SMS donasini sonda belgilash mumkin.\n'
        f'1000dan oshiq son kiritilsa avtomatik 10ga tenglanadi!\n{fo.ENDC}'
    )
    print(fo._(fo.BOLD, "Chiqish uchun exit/quit yoki [Ctrl]+[C] kombinatsiyasini kiriting!\n"))
