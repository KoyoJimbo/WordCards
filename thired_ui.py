import ui_modules
import second_ui

class SecondUI(ui_modules.UIModule):
    def __init__(self):
        self.sec_ui = second_ui.SecondUI()
        pass

    def returner(self, except_words, remain_words, w_j, w_e, personal_exception,
           your_weak, random_key, weak_key, second_weak_call):
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
                        if weak_key == None:
                            return self.ui(except_words, remain_words, w_j,
                                           w_e, personal_exception,
                                           your_weak,random_key="randomize")
                        else:
                            return self.ui(except_words, remain_words,
                                           w_j, w_e, personal_exception,
                                           your_weak,random_key="randomize",
                                           weak_key="weak mode",
                                           second_weak_call="second_call")
                elif ans == "weak mode" and weak_key == None:
                        if random_key == None:
                            return self.ui(except_words, remain_words, w_j,
                                           w_e, personal_exception,
                                           your_weak, weak_key="weak mode")
                        else:
                            return self.ui(except_words, remain_words, w_j,
                                           w_e, personal_exception,
                                           your_weak,
                                           random_key="randomize",
                                           weak_key="weak mode")
                elif ans == "end random":
                    if random_key != None and weak_key != None:
                        return self.ui(except_words, remain_words, w_j, w_e,
                                       personal_exception,your_weak,
                                       weak_key=="weak mode")
                    elif random_key != None:
                        return self.ui(except_words, remain_words, w_j, w_e,
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
