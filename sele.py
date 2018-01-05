import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

class Select:
    def __init__(self):
        self._df_num = 1

    def select(self):
        print("law--0")
        print("personality--1")
        try:
            df = int(input("which?: "))
        except ValueError:
            print(Fore.RED + "[Error]:数値を入力して下さい")
            sys.exit()
        self.parrot_no_df(df)
        return df

    def parrot_no_df(self, q):
        assert 0 <= q <= self._df_num, Fore.RED +\
            "x shulde be between 0 and " + str(self._df_num)
