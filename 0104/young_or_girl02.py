# young_or_girl02.py
import sys
age=int(sys.argv[1])
sex=sys.argv[2]
if age<18 or sex=="F":
    print("いらっしゃいませ！")
else:
    print("お引き取りください！")
