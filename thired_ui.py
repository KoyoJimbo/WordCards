import ui_modules
import second_ui
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class ThiredUI(ui_modules.UIModule):
    def __init__(self):
        self.sec_ui = second_ui.SecondUI()
        pass

    def change_arg(self, ans, random_key, weak_key):
        ans = ans[1:]
        if ans == "random mode" and random_key == None:
            random_key = "randomize"
        elif ans == "weak mode" and weak_key == None:
            weak_key = "weak mode"
        elif ans == "end random" and random_key != None:
            random_key = None
        else:
            return random_key,weak_key,None 
        return random_key, weak_key,"do"

    def print_remain_num(self,num,random_key,ans,remain_words,w_e):
        if (num == 0 and random_key == None) or ans == "s":
            print("残り: " + str(len(remain_words)) + "/" + str(len(w_e)))
        print("\n")

    def show_q(self,num,random_key,w_j):
        if random_key == None:print(str(num) + ": " + str(w_j[num]))
        else:print(" " + "  " + str(w_j[num]))
        ans = str(input("答えて："))
        return ans

    def show_mode(self,random_key,weak_key):
        pass
        #if random_key != None:print(Fore.GREEN + "random mode")
        #if weak_key   != None:print(Fore.GREEN + "weak mode")

    def rmer(self,ans,per_ans,personal_exception,your_weak):
        ans = ans[1:]
        if ans == "rm e" and per_ans == 0:
            self.sec_ui.talk(1)
            return [], your_weak
        elif ans == "rm wp" and per_ans == 0:
            self.sec_ui.talk(2)
            return personal_exception, []
        elif ans == "exit" and per_ans == 0:
            self.sec_ui.talk(3)
            return personal_exception, your_weak
        else:
            return None, None
