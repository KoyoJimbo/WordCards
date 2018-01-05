import ui 
import file_manager
import original_exception
import sele

class Main:
    def __init__(self):
        self.dfs = [
                    "law.csv",
                    "personality.csv"
                   ] 

    def main(self):
        f_manager = file_manager.FileManeger(self.dfs)
        module = ui.Module()
        org_except = original_exception.OriginalException()
        select = sele.Select(self.dfs)

        # 練習に使うデータを対話的に選びます
        taget_df = select.select()

        # 個人データのファイル名を取得します
        save_data_name = f_manager.name_case_for_txtfile(taget_df)

        # 個人データを読み込みます
        personal_exception = f_manager.read_personal_exception(save_data_name)

        # 練習に使うデータフレームを読み込みます
        w_e, w_j = f_manager.gein_csv(taget_df)

        # 単語を練習に使うものと使わないものに分けます
        except_words, remain_words =\
            org_except.main(taget_df, personal_exception, w_e)

        # 練習が始まります
        personal_exception =\
        module.ui(except_words, remain_words, w_j, w_e, personal_exception)

        # 個人データをファイルに書き込みます
        f_manager.save_personal_exception(personal_exception, save_data_name)


if __name__ == '__main__':
    main = Main()
    main.main()
