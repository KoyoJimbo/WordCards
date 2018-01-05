class OriginalException:
    def except_words_folder(self, taget_df):
        if taget_df == 0 : # for law.csv
            except_words = [1,5,7,10,11,15,24]
        elif taget_df == 1: # for personality.csv
            except_words = []
        return except_words

    def remain_words_maker(self, except_words, w_e):
        remain_words = []
        for i in range(len(w_e)):
            if i not in except_words:
                remain_words.append(i)
        return remain_words

    def adapt_your_exception2original(self, except_words, personal_exception):
        except_words.extend(personal_exception)
        except_words = self.f7(except_words)
        return except_words

    # join_your_exception2original にて使用しました
    def f7(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if x not in seen and not seen_add(x)]
