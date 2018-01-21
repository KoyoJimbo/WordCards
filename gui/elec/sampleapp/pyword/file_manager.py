import pandas as pd
import csv as csv
import os
class FileManeger:
    def __init__(self, dfs):
        self.dfs = dfs

    def join_path(self, file_name):
        file_path = os.path.join('../files/',file_name)
        return file_path

    # relate .txt
    def name_case_for_txtfile(self, target_df, head_name):
        your_files =\
            list(map(lambda x: head_name + x.replace('.csv','.txt'), self.dfs))
        return your_files[target_df]

    def read_personal_exception(self, save_data_name):
        save_data_name = self.join_path(save_data_name)
        except_words_personal = []
        try:
            f = open(save_data_name)
            try:
                lines  = f.readlines()
                for line in lines:
                    except_words_personal.append(int(line.replace('\n','')))
            finally:
                f.close()
        except Exception as e:
            print(e,'error occurred')
        return except_words_personal

    def save_personal_exception(self, personal_exception,save_data_name):
        save_data_name = self.join_path(save_data_name)
        try:
            f = open(save_data_name, 'w')
            for num in personal_exception:
                f.write(str(num)+"\n")
        except Exception as e:
            print(e,'error occurred')
        finally:
            f.close()

    # relate .csv
    def df_manager(self, target_df):
        df_path = self.join_path(self.dfs[target_df])
        return df_path

    def gein_csv(self, target_df):
        word_df = pd.read_csv(self.df_manager(target_df), header=0)
        w_e = word_df['english']
        w_j = word_df['japanese']
        return w_e, w_j
