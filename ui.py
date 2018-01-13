import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Module:
    def __init__(self):
        pass

    def ui(self, except_words, remain_words, w_j, w_e, personal_exception,your_weak, randam_key=None, weak_key=None, second_weak_call=None):
        previous_num = None
        if weak_key != None:
            if second_weak_call == None:
                for per_weak in range(len(w_e)):
                    if per_weak not in your_weak:
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words,  per_weak)
        for time in range(1024):
            num = self.rand_or_not(time,w_e,randam_key)
            if num == 0 and randam_key == None:
                print("残り: " + str(len(remain_words))+ "/" + str(len(w_e)))
            if num in except_words or (previous_num == num and randam_key != None and len(remain_words) != 1):
                if len(remain_words) == 0:
                    return personal_exception, your_weak
                continue
            else:
                print("\n")
                if randam_key != None:
                    print(Fore.GREEN + "random mode")
                if weak_key   != None:
                    print(Fore.GREEN + "weak mode")
                for per_ans in range(2):
                    print(str(num) + ": " + str(w_j[num]))
                    ans = str(input("答えて："))
                    if ans == "random mode" and randam_key == None:
                            if weak_key == None:
                                return self.ui(except_words, remain_words, w_j, w_e, personal_exception,your_weak,randam_key="randamize")
                            else:
                                return self.ui(except_words, remain_words,
                                    w_j, w_e, personal_exception,your_weak,randam_key="randamize",
                                    weak_key="weak mode",second_weak_call="second_call")
                    elif ans == "weak mode" and weak_key == None:
                            if randam_key == None:
                                return self.ui(except_words, remain_words, w_j, w_e, personal_exception, your_weak, weak_key="weak mode")
                            else:
                                return self.ui(except_words, remain_words, w_j, w_e, personal_exception,your_weak, randam_key="randamize", weak_key="weak mode")
                    elif ans == "end r":
                        return self.ui(except_words, remain_words, w_j, w_e, personal_exception,your_weak)
                    elif ans == "rm s" and per_ans == 0:
                        print(Fore.GREEN + '\nあなたが除いた単語を全て復活させます')
                        return [], your_weak
                    elif ans == "rm wp" and per_ans == 0:
                        print(Fore.GREEN + '\nあなたの弱点としてセーブされていた単語を全て消去します')
                        return personal_exception, []
                    elif ans == "e" and per_ans == 0 and previous_num != None:
                        if previous_num not in personal_exception:
                            personal_exception.append(previous_num)
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words, num)
                        break
                    elif ans == "wp":
                        if previous_num not in your_weak:
                            your_weak.append(previous_num)
                        break
                    elif ans == "s":
                        except_words, remain_words =\
                            self.add_del(except_words, remain_words, num)
                        break
                    elif ans == w_e[num]:
                        self.right(except_words, remain_words, num ,w_e)
                        break
                    else:
                        self.wrong(w_e, num)
                        break
                previous_num = num
                if len(remain_words) == 0:
                    return personal_exception, your_weak

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
