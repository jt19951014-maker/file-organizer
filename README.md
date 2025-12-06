# file-organizer
File sorting automation tool
# 🗂 File Organizer ― 自動ファイル整理ツール

## 📌 概要
散らばったドキュメント／議事録ファイルを、自動で整理・フォルダ分類する Python スクリプトです。  
作成日時から年・月情報を取得し、正しい階層へ整理します。

## ✨主な機能
| 機能 | 詳細 |
| 📅 日付取得 | 作成日時を取得 |
| 🏗️ フォルダ自動生成 | 年／月フォルダを自動作成 |
| 🚚 自動仕分け | 所定フォルダへファイル移動 |
| 🔍 重複ファイル検知（予定） | 同名ファイルへ対応 |

## 🚀 使い方
本スクリプト (`file_organizer.py`) と **同じ階層**に  
整理対象フォルダ `memo/` を設置してください。

以下の構成になります👇

project_root/
├ file_organizer.py
└ memo/
├ 会議A.txt
├ 会議B.txt
└ ... 

```bash
python file_organizer.py
