import os
import datetime
import shutil
from glob import glob

#memoフォルダ内の全ての拡張子.txtのファイルをリストとして取得
list_of_file = glob("memo/*.txt")
#リストのファイル1つ1つに対して実施
for file_path in list_of_file:

    created_time = os.path.getmtime(file_path)
    #ファイルの作成日時を取得
    created_time = datetime.datetime.fromtimestamp(created_time)

    #必要なファイルの作成の年、月、日を取得する
    year = created_time.year
    month = created_time.month
    day = created_time.day

    #パスからファイル名のみを抽出
    file_name = file_path.split("\\")[1]
    #新しいファイル名を設定
    new_file_name = f"{year}年{month}月{day}日_{file_name}"
    #新しいファイル名にリネームする。
    os.rename(file_path, f"memo/{new_file_name}")

    #所定のフォルダが存在しなければ作成する。
    if not os.path.exists(f"議事録/{year}年/{month}月"):
        os.makedirs(f"議事録/{year}年/{month}月")

    #移動前と移動先のファイルパスを設定し、ファイルを移動する。
    file_path_before_move = f"memo/{new_file_name}"
    file_path_after_move = f"議事録/{year}年/{month}月/{new_file_name}"
    shutil.move(file_path_before_move, file_path_after_move)

print("全てのファイルを所定の場所へ格納しました。")
