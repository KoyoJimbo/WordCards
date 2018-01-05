import pandas as pd
import csv as csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

class Module:
    def __init__(self):
        self._df_num = 1

#   select
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

#   ui
    def ui(self, except_words, remain_words, w_j, w_e, personal_exception):
        for time in range(512):
            num = time % len(w_e)
            if num == 0:
                print("未習得単語数:" + str(len(remain_words)))
            if num in except_words:
                if len(remain_words) == 0:
                    return personal_exception
                continue
            else:
                for per_ans in range(2):
                    print(str(time) + ":" + str(w_j[num]))
                    ans = str(input("答えて："))
                    if (ans == "e") and (per_ans == 0):
                        if(num>0):
                            personal_exception.append(pervious_num)
                    elif ans == "s":
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words, num)
                        break
                    elif (ans == w_e[num]):
                        self.right(except_words, remain_words, num ,w_e)
                        break
                    else:
                        self.wrong(w_e, num)
                        break
                print("\n")
                pervious_num = num
                if len(remain_words) == 0:
                    return personal_exception

    def add_del(self, except_words, remain_words, word):
        if word not in except_words:
            except_words.append(word)
        if word in except_words:
            remain_words.remove(word)
        return except_words, remain_words

    def right(self, except_words, remain_words, num ,w_e):
        print(w_e[num])
        except_words, remain_words =\
            self.add_del(except_words, remain_words, num)
 
    def wrong(self, w_e, num):
        print(w_e[num])
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break
