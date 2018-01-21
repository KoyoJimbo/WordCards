from py_modules import file_manager

class Main:
    def __init__(self):
        self.dfs = [
                 'law.csv'
                ,'personality.csv'
                ,'science.csv'
                ,'math.csv'
                ,'unit5.csv'
                ,'unit6.csv'
                ,'unit8.csv'
                ,'unit9.csv'
                ,'unit10.csv'
                ,'original_words.csv'
                ,'linear_algebra.csv'
              ]

    def main_func(self):
        f_manager = file_manager.FileManeger(self.dfs)
        # 練習に使うデータフレームを読み込みます
        taget_df = 4
        w_e, w_j = f_manager.gein_csv(taget_df)
        return w_e, w_j
