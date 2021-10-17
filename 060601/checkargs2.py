#checkargs2.py
#コマンドライン引数が２個以上であることをチェックする
import sys
if len(sys.argv)<3:
    print("引数として２つの整数が必要です。")
    exit()
print("引数チェックOK！")
