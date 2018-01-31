import ui_modules
import thired_ui
import second_ui
import random
class Ui(ui_modules.UIModule):
    def __init__(self):
        self.sec_ui = second_ui.SecondUI()
        self.thr_ui = thired_ui.ThiredUI()

    def ui(self, except_words, remain_words, w_j, w_e, personal_exception,
           your_weak, random_key=None, weak_key=None,sec_call=None):
        previous_num = ans = None
        if sec_call == None:
            except_words, remain_words =\
                self.sec_ui.apply_weak(except_words, remain_words,w_e,
                                       your_weak,random_key, weak_key)
        for time in range(1024):
            if len(remain_words) == 0:
                return personal_exception,your_weak
            num = super().rand_or_not(time,w_e,previous_num,
                                      remain_words,random_key)
            if num not in remain_words or num == previous_num:
                continue
            self.thr_ui.print_remain_num(num,random_key,ans,remain_words,w_e)
            self.thr_ui.show_mode(random_key,weak_key)
            ans = self.thr_ui.show_q(num,random_key,w_j)
            for per_ans in range(2):
                if len(ans) >= 1 and ans[0] == ":" and per_ans == 0:
                    # 再帰あり retun の枝
                    tmp_r,tmp_w,do_key =\
                        self.thr_ui.change_arg(ans, random_key, weak_key)
                    if do_key is not None:
                        return self.ui(except_words,remain_words,w_j,w_e,
                                       personal_exception,your_weak,tmp_r,
                                       tmp_w,sec_call='called_secondary')
                    else: # 再帰あり return の枝で処理が行われなかった時
                        # 再帰なし retun の枝
                        tmp_personal_exception, tmp_your_weak =\
                            self.thr_ui.rmer(ans,per_ans,personal_exception,
                                             your_weak)
                        if tmp_personal_exception or tmp_your_weak is not None:
                           return tmp_personal_exception,tmp_your_weak
                        else:continue
                # breakの枝
                if self.sec_ui.branch(ans,per_ans,num,previous_num,
                                      except_words,remain_words,w_e,
                                      w_j,random_key,personal_exception,your_weak) is not None:
                    break
            previous_num = num
