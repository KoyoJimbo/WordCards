import pandas as pd
import csv as csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

_df_num = 1

class Main:
    def __init__(self):
        pass

    def input_df(self, target_df):
        df = [
                "law.csv",
                "personality.csv"
             ]
        return df[target_df]

    def input_your_data(self, target_df):
        your_data = [
                "your_law.txt",
                "your_personality.txt"
             ]
        return your_data[target_df]

    def input_except_words(self, taget_df):
        if taget_df == 0 :
            except_words = [1,5,7,10,11,15,24] #for word.csv
        elif taget_df == 1:
            except_words = [] #for personality.csv
        return except_words

    def select(self):
        print("words--0")
        print("personality--1")
        try:
            df = int(input("which?: "))
        except ValueError:
            print(Fore.RED + "[Error]:数値を入力して下さい")
            sys.exit()
        self.parrot_no_df(df)
        return df

#  例外処理 for select
    def parrot_no_df(self, q):
        assert 0 <= q <= _df_num, Fore.RED + \
            "x shulde be between 0 and " + str(_df_num)

    def gein_csv(self, taget_df):
        word_df = pd.read_csv(self.input_df(taget_df), header=0)
        w_e = word_df['english']
        w_j = word_df['japanese']
        return w_e, w_j

    def add_del(self, except_words, remain_words, word):
        if word not in except_words:
            except_words.append(word)
        if word in except_words:
            remain_words.remove(word)
        return except_words, remain_words

    def join_your_exception2original(self, except_words, personal_exception):
        except_words.extend(personal_exception)
        except_words = self.f7(except_words)
        return except_words

    def f7(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if x not in seen and not seen_add(x)]

    def input_remain_words(self, except_words, w_e):
        remain_words = []
        for i in range(len(w_e)):
            if i not in except_words:
                remain_words.append(i)
        return remain_words

    def read_personal_exception(self, save_data_name):
        except_words_personal = []
        try:
            f = open(save_data_name)
            try:
                lines  = f.readlines()
                for line in lines:
                    except_words_personal.append(int(line.replace('\n','')))
            finally:
                f.close()
        except Exception as e:
            print(e,'error occurred')
        return except_words_personal

    def save_personal_exception(self, personal_exception,save_data_name):
        try:
            f = open(save_data_name, 'w')
            for num in personal_exception:
                f.write(str(num)+"\n")
        except Exception as e:
            print(e)
        finally:
            f.close()

    def right(self, except_words, remain_words, num ,w_e):
        print("OK")
        print(w_e[num])
        except_words, remain_words =\
            self.add_del(except_words, remain_words, num)

    def wrong(self, w_e, num):
        print("NO")
        print(w_e[num])
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break

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
                    if (ans == 'e') and (per_ans == 0):
                        if(num>=1) and ((num-1) not in personal_exception):
                                personal_exception.append(num-1)
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words, num)
                    elif ans == 's':
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
                if len(remain_words) == 0:
                    return personal_exception

    def main(self):
        # 練習に使うデータを選びます
        taget_df = self.select()
        # 個人データのファイル名を取得します
        save_data_name = self.input_your_data(taget_df)
        # 個人データを読み込みます
        personal_exception = self.read_personal_exception(save_data_name)
        # 練習に使うデータフレームを読み込みます
        w_e, w_j = self.gein_csv(taget_df)
        # 練習に使わない単語のデータを読み込みます
        except_words = self.input_except_words(taget_df)
        # 個人データを練習に使ない単語のデータに適用させます
        except_words =\
        self.join_your_exception2original(except_words, personal_exception)
        # 練習に使う単語のデータを作成します
        remain_words = self.input_remain_words(except_words, w_e)
        # 練習が始まります
        personal_exception =\
        self.ui(except_words, remain_words, w_j, w_e, personal_exception)
        # 個人データをファイルに書き込みます
        self.save_personal_exception(personal_exception, save_data_name)

if __name__ == '__main__':
    main = Main()
    main.main()
