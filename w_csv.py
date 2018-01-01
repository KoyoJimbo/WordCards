import pandas as pd
import csv as csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys

_df_num = 1
save_data_name = 'your_data.txt'

# input df
def select():
    print("words--0")
    print("personality--1")
    try:
        df = int(input("which?: "))
    except ValueError:
        print(Fore.RED + "[Error]:数値を入力して下さい")
        sys.exit()
    parrot_no_df(df)
    return df

#  例外処理 for imput
def parrot_no_df(q):
    assert 0 <= q <= _df_num, Fore.RED + \
        "x shulde be between 0 and " + str(_df_num)

def input_df(target_df):
    df = [
         "words.csv",
         "personality.csv"
         ]
    return df[target_df]

def gein_csv(taget_df):
    word_df = pd.read_csv(input_df(taget_df), header=0)
    w_e = word_df['english']
    w_j = word_df['japanese']
    return w_e, w_j

def add_del(except_words, remain_words, word):
    except_words.append(word)
    remain_words.remove(word)
    return except_words, remain_words

def input_except_words(taget_df):
    if taget_df == 0 :
        except_words = [1,5,7,10,11,15,24] #for word.csv
    elif taget_df == 1:
        except_words = [] #for personality.csv
    return except_words

def join_your_exception2original(except_words, personal_exception):
    except_words.extend(personal_exception)
    except_words = f7(except_words)
    return except_words

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

def input_remain_words(except_words, w_e):
    remain_words = []
    for i in range(len(w_e)):
        if i not in except_words:
            remain_words.append(i)
    return remain_words

def read_personal_exception():
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

def save_personal_exception(personal_exception):
    try:
        f = open(save_data_name, 'w')
        for num in personal_exception:
            f.write(str(num)+"\n")
    except Exception as e:
        print(e)
    finally:
        f.close()

def right(except_words, remain_words, num ,w_e):
    print("OK")
    print(w_e[num])
    except_words, remain_words =\
        add_del(except_words, remain_words, num)

def wrong(w_e, num):
    print("NO")
    print(w_e[num])
    '''
    for i in range(100):
        trash = str(input("練習して："))
        if(trash == w_e[num]):
            break
    '''

def ui(except_words, remain_words, w_j, w_e, personal_exception):
    for time in range(512):
        num = time % len(w_e)
        if num == 0:
            print("未習得単語数:" + str(len(remain_words)))
        if num in except_words:
            continue
        else:
            print(str(time) + ":" + str(w_j[num]))
            ans = str(input("答えて："))
            if ans == "u":
                except_words, remain_words =\
                    add_del(except_words, remain_words, num)
            elif ans == "unko":
                if(num>=1):
                    personal_exception.append(num-1)
                    except_words, remain_words =\
                        add_del(except_words, remain_words, num)
            elif ans == w_e[num]:
                right(except_words, remain_words, num ,w_e)
            else:
                wrong(w_e, num)
            print("\n")
            if len(remain_words) == 0:
                return personal_exception


def main():
    personal_exception = read_personal_exception()
    taget_df = select()
    w_e, w_j = gein_csv(taget_df)
    except_words = input_except_words(taget_df)
    except_words =\
    join_your_exception2original(except_words, personal_exception)
    remain_words = input_remain_words(except_words, w_e)
    personal_exception =\
    ui(except_words, remain_words, w_j, w_e, personal_exception)
    save_personal_exception(personal_exception)

main()
