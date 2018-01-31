import ui_modules
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import threading

class SecondUI(ui_modules.UIModule):
    def __init__(self):
        pass

    def apply_weak(self, except_words, remain_words,
                   w_e, your_weak, random_key=None,
                   weak_key=None):
        if weak_key != None:
            for per_weak in range(len(w_e)):
                if per_weak not in your_weak:
                    except_words, remain_words =\
                        super().add_del(except_words, 
                                        remain_words,per_weak)
        return except_words, remain_words

    def branch(self,ans,per_ans,num,previous_num,
               except_words,remain_words,w_e,w_j,random_key,personal_exception,your_weak):
        done = None
        if ans == "e" and per_ans == 0 and previous_num != None:
            if previous_num not in personal_exception:
                personal_exception.append(previous_num)
            except_words, remain_words =\
                super().add_del(except_words, remain_words, num)
        elif ans == "wp":
            if num not in your_weak:
                your_weak.append(num)
        elif ans == "s":
            except_words, remain_words =\
                super().add_del(except_words, remain_words, num)
        elif ans == w_e[num]:
            super().right(except_words, remain_words,
                          num ,w_e,random_key)
            done = "done"
        else:
            super().wrong(w_e, num)
            done = "done"
        return done

    def talk(self,talknum):
        if talknum == 1:
            talk = '\nあなたが除いた単語を全て復活させます'
        elif talknum == 2:
            talk = '\nあなたの弱点としてセーブされていた単語を全て消去します'
        elif talknum == 3:
            talk = '\n単語帳を終了します'
        print(Fore.GREEN + talk)
