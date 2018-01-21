class OriginalException:
    def __init__(self):
        pass

    def main(self, taget_df, personal_exception, w_e):
        except_words = self.except_words_folder(taget_df)
        except_words =\
            self.adapt_your_exception2original(except_words, personal_exception)
        remain_words = self.remain_words_maker(except_words, w_e)
        return except_words, remain_words

    def except_words_folder(self, target_df):
        if target_df == 0 : # for law.csv
            except_words = [1,5,7,10,11,15,24]
        elif target_df == 2: # for science.csv
            remain_words = [1,3,7,8,9,11,16,17,18,22,24,25,31,36,37]
            except_words = [x for x in range(40) if x+1 not in remain_words]
        else:
            except_words = []
        return except_words

    def remain_words_maker(self, except_words, w_e):
        return [x for x in range(len(w_e)) if x not in except_words]

    def adapt_your_exception2original(self, except_words, personal_exception):
        except_words.extend(personal_exception)
        except_words = self.f7(except_words)
        return except_words

    def f7(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if x not in seen and not seen_add(x)]

if __name__ == '__main__':
    uk = OriginalException()
    print(uk.except_words_folder(2))
