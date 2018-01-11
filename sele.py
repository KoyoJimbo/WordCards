import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

class Select:
    def __init__(self, dfs):
        self.dfs = dfs

    def select(self):
        print(' ' + Fore.GREEN + str(len(self.dfs)) + '--instructs')
        for df_num in range(len(self.dfs)):
            print(' ' + str(df_num) + '--' + str(self.dfs[df_num].split('.')[0]))
        try:
            df = int(input(' ' + "which? :"))
        except ValueError:
            print(Fore.RED + "[Error]:数値を入力して下さい")
            sys.exit()
        self.parrot_no_df(df)
        if df == len(self.dfs):
            self.instructions()
            df = self.select()
        return df

    def parrot_no_df(self, q):
        assert 0 <= q <= (len(self.dfs)),\
            Fore.RED + "x shulde be between 0 and " + str(len(self.dfs))

    def instructions(self):
        print("\n")
        print("  特殊コマンド")
        print("    e         一つ前の単語が以降表示されなくなります")
        print("    s         スキップします")
        print("    new game  コマンドで除いた単語を復活させ")
        print("              プログラムを終了します")
        print("    r         以降ランダムに出題します")
        print("\n")
