import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class UIModule:
    def __init__(self):
        pass

    def rand_or_not(self,time,w_e,randam_key):
        if randam_key == None:
            num = time % len(w_e)
            return num
        else:
            num = random.randint(0, len(w_e)-1)
            return num

    def add_del(self, add_list, del_list, word):
        if word not in add_list:
            add_list.append(word)
        if word in del_list:
            del_list.remove(word)
        return add_list, del_list

    def right(self, except_words, remain_words, num ,w_e):
        print(Fore.BLUE + w_e[num])
        print("残り: " + str(len(remain_words))+ "/" + str(len(w_e)))
        except_words, remain_words =\
            self.add_del(except_words, remain_words, num)

    def wrong(self, w_e, num):
        print(Fore.BLUE + w_e[num])
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break
