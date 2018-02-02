import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess
import super_ui_modules

class UIModule(super_ui_modules.SuperUIModule):
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

    def speaker(self, previous_num, w_e):
        if previous_num is not None:
            args = ['espeak', '-s', '125', '-v', 'en+f5']
            args.append(str(w_e[previous_num]))
            res = subprocess.check_call(args)

    def wrong_LP(self, w_e, w_j, num, ans):
        super().LP(w_e, num, ans)
        print(Fore.BLUE + str(w_e[num]))
        for i in range(100):
            #trash = str(input("練習して："))
            trash = str(input(""))
            if(trash == w_e[num]):
                break
            print("\n")
            print(str(w_j[num]))
            super().LP(w_e, num, trash)
            print(Fore.BLUE + str(w_e[num]))

# debug for wrong_LP()
if __name__ == '__main__':
    dfs = [
             'law.csv'
            ,'complimentary'
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
    ans = '1com4444pli333mentary1'
    uim = UIModule()
    uim.wrong_LP(dfs,1,ans)
