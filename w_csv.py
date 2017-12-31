import pandas as pd
import csv as csv

def gein_csv():
    word_df = pd.read_csv("words.csv", header=0)
    w_e = word_df['english']
    w_j = word_df['japanese']
    return w_e, w_j

def add_del(except_words, remain_words, word):
    except_words.append(word)
    remain_words.remove(word)
    return except_words, remain_words

def dominate():
    except_words = [1,5,7,10,11,15,24]
    remain_words = []
    for i in range(len(w_e)):
        if i not in except_words:
            remain_words.append(i)
    return except_words, remain_words

def right(except_words, remain_words, num ,w_e):
    print("正解")
    print(w_e[num])
    except_words, remain_words =\
        add_del(except_words, remain_words, num)

def wrong(w_e, num):
    print("不正解")
    print(w_e[num])
    '''
    for i in range(100):
        trash = str(input("練習して："))
        if(trash == w_e[num]):
            break
    '''

def ui(except_words, remain_words):
    for time in range(512):
        num = time % len(w_e)
        if num == 0:
            print("未習得単語数:" + str(len(remain_words)))
        if num in except_words:
            continue
        else:
            print(str(time) + ":" + w_j[num])
            ans = str(input("答えて："))
            if ans == "u":
                except_words, remain_words =\
                    add_del(except_words, remain_words, num)
            elif ans == w_e[num]:
                right(except_words, remain_words, num ,w_e)
            else:
                wrong(w_e, num)
            print("\n")
            if len(remain_words) == 0:
                break

w_e, w_j = gein_csv()
except_words, remain_words = dominate()
ui(except_words, remain_words)
