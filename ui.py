import ui_modules
import second_ui
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Ui(ui_modules.UIModule):
    def __init__(self):
        self.sec_ui = second_ui.SecondUI()
        pass

    def ui(self, except_words, remain_words, w_j, w_e, personal_exception,
           your_weak, random_key=None, weak_key=None):
        previous_num = None
        ans = None
        except_words, remain_words =\
            self.sec_ui.apply_weak(except_words, remain_words, w_e,
                                   your_weak,random_key, weak_key)
        for time in range(1024):
            num = super().rand_or_not(time,w_e,random_key)
            if num in except_words or\
                (previous_num == num and\
                    random_key != None and\
                    len(remain_words) != 1):
                if len(remain_words) == 0:
                    return personal_exception, your_weak
                continue
            else:
                if (num == 0 and random_key == None) or ans == "s":
                    print("残り: " + str(len(remain_words)) +\
                          "/" + str(len(w_e)))
                print("\n")
                if random_key != None:print(Fore.GREEN + "random mode")
                if weak_key   != None:print(Fore.GREEN + "weak mode")
                for per_ans in range(2):
                    if random_key == None:print(str(num) + ": " + str(w_j[num]))
                    else:print(" " + "  " + str(w_j[num]))
                    ans = str(input("答えて："))
                    if ans == "random mode" and random_key == None:
                        return self.ui(except_words, remain_words,
                                       w_j, w_e, personal_exception,
                                       your_weak,
                                       random_key = "randomize",
                                       weak_key = weak_key)
                    elif ans == "weak mode" and weak_key == None:
                        return self.ui(except_words, remain_words, w_j,
                                       w_e, personal_exception,
                                       your_weak,
                                       random_key = random_key,
                                       weak_key = "weak mode")
                    elif ans == "end random" and random_key != None:
                        return self.ui(except_words, remain_words, w_j, w_e,
                                       personal_exception,your_weak,
                                       random_key = None,
                                       weak_key=weak_key)
                    elif ans == "rm e" and per_ans == 0:
                        self.sec_ui.talk(1)
                        return [], your_weak
                    elif ans == "rm wp" and per_ans == 0:
                        self.sec_ui.talk(2)
                        return personal_exception, []
                    else:
                        self.sec_ui.branch(ans,per_ans,num,previous_num,
                                           except_words,remain_words,w_e,w_j)
                        break
                if len(remain_words) == 0:return personal_exception, your_weak
                previous_num = num
