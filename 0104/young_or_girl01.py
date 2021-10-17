# young_or_girl01.py
import sys
age=int(sys.argv[1])
sex=sys.argv[2]
if age<18:
    if sex=="F":
        print("いらっしゃいませ！")
    else:
        print("お引き取りください！")
else:
    print("お引き取りください！")
