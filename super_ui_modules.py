import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class SuperUIModule:
    def __init__(self):
        pass

    def LP(self, w_e, num, ans):
        if len(ans) > 0:
            forward     = self.forward_fanc(ans, w_e, num)
            back        = self.back_fanc(ans, w_e, num)
            next_middle = self.middle_func(ans, w_e, num, forward, back)
            print(str(forward) + Fore.RED +\
                str(next_middle) + Fore.RESET + str(back[::-1]))

    def  forward_fanc(self, ans, w_e, num):
        forward = ''
        j = 0
        while j < min(len(ans),len(w_e[num])) and ans[j] == w_e[num][j]:
            forward += ans[j]
            j += 1
        return forward

    def back_fanc(self, ans, w_e, num):
        back = ''
        ans_tail = len(ans) - 1
        w_e_tail = len(w_e[num]) - 1
        # while 前方の条件２つはw_e[-1]となりw_eの後方を検索しないためです。
        while ans_tail >= 0 and  w_e_tail >= 0 and\
            ans[ans_tail] == w_e[num][w_e_tail]:
            back += ans[ans_tail]
            ans_tail -= 1
            w_e_tail -= 1
        return back

    def middle_func(self, ans, w_e, num, forward, back):
        next_middle = ''
        if 1 < len(ans)-len(forward)-len(back):
            middle = ''
            for i in range(len(ans)-len(forward)-len(back)):
                middle += ans[i+len(forward)]
            w_e_middle = self.make_w_e_middle(w_e, num, forward, back)
            middleP2 = [middle[i:i+2] for i in range(len(middle)-1)]
            w_eP2 = [w_e_middle[i:i+2] for i in range(len(w_e_middle)-1)]
            for i in range(len(middleP2)):
                if middleP2[i] in w_eP2:
                    next_middle += Fore.GREEN + middleP2[i][0]
                else:
                    if i != 0 and (middleP2[i-1] in w_eP2):
                        next_middle += Fore.GREEN + middleP2[i][0]
                    else:
                        next_middle += Fore.RED +  '_'# insted middleP2[i][0]
            next_middle += Fore.RED + '_' # insted middleP2[-1][1]
        elif 1 == len(ans)-len(forward)-len(back):
            next_middle += Fore.RED + '_' # insted str(ans[len(forward)])
        else:
            next_middle += Fore.RED
            for i in range(len(w_e[num])-len(forward)-len(back)):
                next_middle += '_'
        return next_middle

    def make_w_e_middle(self, w_e, num, forward, back):
        w_e_middle = w_e[num][len(forward):len(w_e[num])-len(back)]
        return w_e_middle
