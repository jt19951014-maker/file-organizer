# 🗂 File Organizer ― 自動ファイル整理ツール

## 📌 概要
散らばったドキュメント／議事録ファイルを、自動で整理・フォルダ分類する Python スクリプトです。  
作成/更新日時から年・月情報を取得し、正しい階層へ整理します。

---

## ✨主な機能
| 機能 | 詳細 |
|---|---|
| 📅 日付取得 | 作成日時を取得しファイル名へ付与 |
| 🏗️ フォルダ自動生成 | 年／月フォルダを自動作成 |
| 🚚 自動仕分け | 正しいフォルダ階層へ移動 |

---

## 🚀 使用方法
本スクリプト（file_organizer.py）と同じ階層に  
整理対象フォルダ `memo/` を設置してください。

```bash
フォルダ構成例：
project_root/
├ file_organizer.py
└ memo/
  ├ 会議A.txt
  ├ 会議B.txt
```
以下のコマンドを実行：

```bash
python file_organizer.py
```

実行後、自動的に 議事録/年/月/ フォルダへ分類されます。
スクリプト実行前後のファイル構成を例示すると、以下のようになります。
```bash
↓実行前
project_root/
├ file_organizer.py
├ memo/
│ ├ doc1.txt
│ └ doc2.txt
│ └ doc3.txt
│ └ doc4.txt
├ 議事録

↓実行後
project_root/
├ file_organizer.py
├ memo
├ 議事録
  ├ 2025年
    ├11月
    │ ├ 2025年11月12日_doc1.txt
    │ └ 2025年11月26日_doc2.txt
    ├12月
      ├ 2025年12月10日_doc3.txt
      └ 2025年12月24日_doc4.txt
```
    
⚠️ 注意点
Windowsでは、ファイルコピーで作成日が更新される場合があります

## 🧰動作環境
- Python 3.12  
- OS ごとの動作確認必要

🧑‍💻 使用技術
Python（os / shutil / datetime / glob）

🔧 今後の改善予定（あなたの書いた内容そのまま）
GUI対応
ログ出力追加
重複ファイル検知

👤 作者
津崎潤（Jun Tsuzaki）
Python自動化エンジニア志望

