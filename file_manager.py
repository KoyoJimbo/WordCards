import pandas as pd
import csv as csv
class FileManeger:
    # relate .txt
    def name_case_for_txtfile(self, target_df):
        your_data = [
                "your_law.txt",
                "your_personality.txt"
             ]
        return your_data[target_df]

    def read_personal_exception(self, save_data_name):
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
        try:
            f = open(save_data_name, 'w')
            for num in personal_exception:
                f.write(str(num)+"\n")
        except Exception as e:
            print(e)
        finally:
            f.close()

    # relate .csv
    def df_manager(self, target_df):
        df = [
                "law.csv",
                "personality.csv"
             ]
        return df[target_df]

    def gein_csv(self, taget_df):
        word_df = pd.read_csv(self.df_manager(taget_df), header=0)
        w_e = word_df['english']
        w_j = word_df['japanese']
        return w_e, w_j
