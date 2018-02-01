import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess

class UIModule:
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

    def wrong_LP(self, w_e, num, ans):
        self.LP(w_e, num, ans)
        print(Fore.BLUE + str(w_e[num]))
        for i in range(100):
            trash = str(input("練習して："))
            if(trash == w_e[num]):
                break
            print(Fore.BLUE + str(w_e[num]))
            self.LP(w_e, num, trash)

    def LP(self, w_e, num, ans):
        if len(ans) > 0:
            # forward
            forward = ''
            j = 0
            while j < min(len(ans),len(w_e[num])) and ans[j] == w_e[num][j]:
                forward += ans[j]
                j += 1
            # back
            back = ''
            ans_tail = len(ans) - 1
            w_e_tail = len(w_e[num]) - 1
            # while 前方の条件２つはw_e[-1]となりw_eの後方を検索しないためです。
            while ans_tail >= 0 and  w_e_tail >= 0 and\
                ans[ans_tail] == w_e[num][w_e_tail]:
                back += ans[ans_tail]
                ans_tail -= 1
                w_e_tail -= 1
            # middle
            next_middle = ''
            if 1 < len(ans)-len(forward)-len(back):
                middle = ''
                for i in range(len(ans)-len(forward)-len(back)):
                    middle += ans[i+len(forward)]
                middleP2 = [middle[i:i+2] for i in range(len(middle)-1)]
                w_eP2 = [w_e[num][i:i+2] for i in range(len(w_e[num])-1)]
                for i in range(len(middleP2)):
                    if middleP2[i] in w_eP2:
                        next_middle += Fore.GREEN + middleP2[i][0]
                    else:
                        if i != 0 and (middleP2[i-1] in w_eP2):
                            next_middle += Fore.GREEN + middleP2[i][0]
                        else:
                            next_middle += Fore.RED +  middleP2[i][0]
                next_middle += middleP2[-1][1]
            elif 1 == len(ans)-len(forward)-len(back):
                next_middle += ( Fore.RED + str(ans[len(forward)]))
            else:
                next_middle += Fore.RED
                for i in range(len(w_e[num])-len(forward)-len(back)):
                    next_middle += '_'

            print(str(forward) + Fore.RED +\
                str(next_middle) + Fore.RESET + str(back[::-1]))

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
    ans = 'commplimentary'
    uim = UIModule()
    uim.wrong_LP(dfs,1,ans)
