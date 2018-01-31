import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess

class UIModule:
    def __init__(self):
        pass

    def rand_or_not(self,time,w_e,previous_num,remain_words,random_key):
        if random_key == None:
            num = time % len(w_e)
            return num
        else:
            while(True):
                num = random.randint(0, len(w_e)-1)
                if num in remain_words and\
                    (num != previous_num or len(remain_words)==1):
                    return num

    def add_del(self, add_list, del_list, word):
        if word not in add_list:
            add_list.append(word)
        if word in del_list:
            del_list.remove(word)
        return add_list, del_list

    def right(self, except_words, remain_words, num ,w_e,random_key):
        print(Fore.BLUE + str(w_e[num]))
        except_words, remain_words =\
            self.add_del(except_words, remain_words, num)
        if random_key!=None:
            print("残り: " + str(len(remain_words))+\
                  "/" + str(len(w_e)))

    def wrong(self, w_e, num):
        print(Fore.BLUE + str(w_e[num]))
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break

    def speaker(self, previous_num, w_e):
        if previous_num is not None:
            args = ['espeak', '-s', '125', '-v', 'en+f5']
            args.append(str(w_e[previous_num]))
            res = subprocess.check_call(args)
