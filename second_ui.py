import ui_modules

class SecondUI(ui_modules.UIModule):
    def __init__(self):
        pass

    def apply_weak(self, except_words, remain_words, w_e, your_weak, random_key=None, weak_key=None, second_weak_call=None):
        if weak_key != None and second_weak_call == None:
                for per_weak in range(len(w_e)):
                    if per_weak not in your_weak:
                        except_words, remain_words =\
                            super().add_del(except_words, remain_words,  per_weak)
        return except_words, remain_words
