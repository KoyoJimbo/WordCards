import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Module:
    def __init__(self):
        pass

    def ui(self, except_words, remain_words, w_j, w_e, personal_exception, randam_key=None):
        previous_num = None
        for time in range(1024):
            num = self.rand_or_not(time,w_e,randam_key)
            if num == 0 and randam_key == None:
                print("未習得単語数: " + str(len(remain_words)))
            if num in except_words or (previous_num == num and randam_key != None and len(remain_words) != 1):
                if len(remain_words) == 0:
                    return personal_exception
                continue
            else:
                for per_ans in range(2):
                    print(str(num) + ": " + str(w_j[num]))
                    ans = str(input("答えて："))
                    if ans == "e" and per_ans == 0 and previous_num != None:
                        personal_exception.append(previous_num)
                    elif ans == "r":
                        print("\n")
                        return self.ui(except_words, remain_words, w_j, w_e, personal_exception, "randamize")
                    elif ans == "s":
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words, num)
                        break
                    elif ans == w_e[num]:
                        self.right(except_words, remain_words, num ,w_e)
                        break
                    elif ans == "new game" and per_ans == 0:
                        print(Fore.GREEN + '\nあなたが除いた単語を復活させます')
                        return []
                    else:
                        self.wrong(w_e, num)
                        break
                print("\n")
                previous_num = num
                if len(remain_words) == 0:
                    return personal_exception

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
        print(w_e[num])
        except_words, remain_words =\
            self.add_del(except_words, remain_words, num)

    def wrong(self, w_e, num):
        print(w_e[num])
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break
