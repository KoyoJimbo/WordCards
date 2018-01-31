import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

class Select:
    def __init__(self):
        pass

    def select(self, dfs):
        digit_dfs = len(list(map(int, str(len(dfs)))))
        dfs_num_for_print = str(len(dfs)).ljust(digit_dfs+2,'-')
        print(' ' + Fore.GREEN + dfs_num_for_print + 'instructs')
        for df_num in range(len(dfs)):
            dfs_num_for_print = str(df_num).ljust(digit_dfs+2, '-')
            print(' ' + dfs_num_for_print + str(dfs[df_num].split('.')[0]))
        try:
            df = int(input(' ' + "which? :"))
        except ValueError:
            print(Fore.RED + "[Error]:数値を入力して下さい")
            sys.exit()
        self.parrot_no_df(df,dfs)
        if df == len(dfs):
            self.instructions()
            df = self.select(dfs)
        return df

    def parrot_no_df(self, q ,dfs):
        assert 0 <= q <= (len(dfs)),\
            Fore.RED + "x shulde be between 0 and " + str(len(dfs))

    def instructions(self):
        print("\n")
        print("  特殊コマンド")
        print("    e             一つ前の単語が以降表示されなくなります")
        print("    s             スキップします")
        print("    rm s          eコマンドで除いた単語を復活させ")
        print("                  プログラムを終了します")
        print("    :random mode  以降ランダムに出題します")
        print("    :end random   ランダム出題を停止します")
        print("    :weak mode    苦手な単語のみ出題します")
        print("    wp            苦手な単語を保存できます")
        print("    rm wp         wpコマンドで保存した単語を全て消去します")
        print("\n")
