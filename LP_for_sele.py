import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys
import re

class ForSelect():
    def __init__(self,dfs):
        self.dfs = dfs

    def cut_num(self,texts): 
        pattern = r'(\D+)'
        nonum_texts = [re.findall(pattern,line) for line in texts]
        print(nonum_texts)

    def cut_overlap(self,texts):
        cp_texts = texts
        for namenum in range(texts):
            cp_texts[namenum] = ''
            if texts[namenum] in cp_texts
            


    def LP(self):
        digit_dfs = len(list(map(int, str(len(self.dfs)))))
        df_names = []
        for df_num in range(len(self.dfs)):
            df_names += [str(self.dfs[df_num].split('.')[0])]
        print(df_names)
        self.cut_num(df_names)
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

if __name__ == '__main__':
    dfs = [
             'law.csv'
            ,'personality.csv'
            ,'science.csv'
            ,'math.csv'
            ,'unit5.csv'
            ,'unit6.csv'
            ,'unit8.csv'
            ,'unit9.csv'
            ,'unit10.csv'
            ,'original_words.csv'
            ,'linear_algebra.csv'
            ,'type.csv'
          ]
    for_select = ForSelect(dfs)
    df = for_select.LP()
