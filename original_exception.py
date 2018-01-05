class OriginalException:
    def __init__():
        pass

    def main(self, taget_df, personal_exception, w_e):
        # 練習に使わない単語を取得します
        except_words = self.except_words_folder(taget_df)
        # 個人データを練習に使ない単語のデータに適用させます
        except_words =\
        self.adapt_your_exception2original(except_words, personal_exception)
        # 練習に使う単語のデータを作成します
        remain_words = self.remain_words_maker(except_words, w_e)
        return except_words, remain_words

    def except_words_folder(self, taget_df):
        if taget_df == 0 : # for law.csv
            except_words = [1,5,7,10,11,15,24]
        elif taget_df == 1: # for personality.csv
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
