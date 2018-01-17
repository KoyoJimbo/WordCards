import second_ui
import ui

class ThiredUI(ui.Ui):
    def __init__(self):
        pass

    def returner(self, except_words, remain_words, w_j, w_e,
                 personal_exception,your_weak, random_key,
                 weak_key, second_weak_call,
                 num,previous_num,ans):
        if random_key == None:print(str(num) + ": " + str(w_j[num]))
        else:print(" " + "  " + str(w_j[num]))
        ans = str(input("答えて："))
        if ans == "random mode" and random_key == None:
            if weak_key == None:
                return super().ui(except_words, remain_words, w_j,
                               w_e, personal_exception,
                               your_weak,random_key="randomize")
            else:
                return super().ui(except_words, remain_words,
                               w_j, w_e, personal_exception,
                               your_weak,random_key="randomize",
                               weak_key="weak mode",
                               second_weak_call="second_call")
        elif ans == "weak mode" and weak_key == None:
            if random_key == None:
                return super().ui(except_words, remain_words, w_j,
                               w_e, personal_exception,
                               your_weak, weak_key="weak mode")
            else:
                return super().ui(except_words, remain_words, w_j,
                               w_e, personal_exception,
                               your_weak,random_key="randomize",
                               weak_key="weak mode")
        elif ans == "end random":
            if random_key != None and weak_key != None:
                return super().ui(except_words, remain_words, w_j, w_e,
                               personal_exception,your_weak,
                               weak_key=="weak mode")
            elif random_key != None:
                return super().ui(except_words, remain_words, w_j, w_e,
                               personal_exception,your_weak)
        elif ans == "rm e" and per_ans == 0:
            print(Fore.GREEN + '\nあなたが除いた単語を' +\
                  '全て復活させます')
            return [], your_weak
        elif ans == "rm wp" and per_ans == 0:
            print(Fore.GREEN +\
                  '\nあなたの弱点としてセーブされていた単語' +\
                  'を全て消去します')
            return personal_exception, []
        else:
            return None, None
