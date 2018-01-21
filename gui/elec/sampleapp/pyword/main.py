import ui
import file_manager
import exception
import sele
import time

class Main:
    def __init__(self, dfs):
        self.dfs = dfs

    def main(self):
        f_manager = file_manager.FileManeger(self.dfs)
        module = ui.Ui()
        org_except = exception.OriginalException()
        select = sele.Select(self.dfs)

        # 練習に使うデータを対話的に選びます
        taget_df = select.select()

        # 個人データのファイル名を取得します
        save_data_name =\
            f_manager.name_case_for_txtfile(taget_df,'except_')
        your_f_name_weak =\
            f_manager.name_case_for_txtfile(taget_df,'your_weak_')

        # 個人データを読み込みます
        personal_exception =\
            f_manager.read_personal_exception(save_data_name)
        your_weak =\
            f_manager.read_personal_exception(your_f_name_weak)

        # 練習に使うデータフレームを読み込みます
        w_e, w_j = f_manager.gein_csv(taget_df)

        # 単語を練習に使うものと使わないものに分けます
        except_words, remain_words =\
            org_except.main(taget_df, personal_exception, w_e)

        start_time = time.time()
        # 練習が始まります
        personal_exception, your_weak =\
            module.ui(except_words, remain_words, w_j, w_e, personal_exception,your_weak)
        took_time = int(time.time() - start_time)
        print("elapsed_time: {0}:{0}:{0}"
            .format(int(took_time / 60 / 60))
            .format(int(took_time / 60))
            .format(int(took_time % 60)))

        # 個人データをファイルに書き込みます
        f_manager.save_personal_exception(personal_exception, save_data_name)
        f_manager.save_personal_exception(your_weak, your_f_name_weak)

if __name__ == '__main__':
    dfs = [
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
    main = Main(dfs)
    main.main()
