import ui 
import file_manager
import original_exception
import sele

class Main:
    def main(self):
        f_manager = file_manager.FileManeger()
        module = ui.Module()
        org_except = original_exception.OriginalException()
        select = sele.Select()
        # 練習に使うデータを対話的に選びます
        taget_df = select.select()
        # 個人データのファイル名を取得します
        save_data_name = f_manager.name_case_for_txtfile(taget_df)
        # 個人データを読み込みます
        personal_exception = f_manager.read_personal_exception(save_data_name)
        # 練習に使うデータフレームを読み込みます
        w_e, w_j = f_manager.gein_csv(taget_df)
        # 練習に使わない単語を取得します
        except_words = org_except.except_words_folder(taget_df)
        # 個人データを練習に使ない単語のデータに適用させます
        except_words =\
        org_except.adapt_your_exception2original(except_words, personal_exception)
        # 練習に使う単語のデータを作成します
        remain_words = org_except.remain_words_maker(except_words, w_e)
        # 練習が始まります
        personal_exception =\
        module.ui(except_words, remain_words, w_j, w_e, personal_exception)
        # 個人データをファイルに書き込みます
        f_manager.save_personal_exception(personal_exception, save_data_name)

if __name__ == '__main__':
    main = Main()
    main.main()
