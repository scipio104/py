import pandas as pd
import numpy as ny
import csv
import sys, codecs
import copy

path='kekka2.csv'
with open(path,encoding='utf-8') as f:
    f=csv.reader(f)
    all_csv=[row for row in f]
    csv_r=len(all_csv)
    csv_c=len(all_csv[0])
    print(csv_c,csv_r)
#スパン数
    xspn=[i for i in all_csv if 'Xスパン数' in i]
    xs=int(xspn[0][2])
    yspn=[i for i in all_csv if 'Yスパン数' in i]
    ys=int(yspn[0][2])
    ay=xs+1
    ax=ys+1
    print(xs,ys)
    print(ax,ay)
#軸力表摘出
    target="name=支持力検討用軸力表（グリッド形式）"
    hit= [i for i in all_csv if target in i]
    row_s=all_csv.index(hit[0])
    row_e=all_csv.index(hit[1])
    print(row_s,row_e)#行番号name=支持力検討用軸力表（グリッド形式）
    v_force_list=all_csv[row_s:row_e+1]#軸力表
    #print(v_force_list)
#通り摘出用リスト
    long_list=[i for i in v_force_list if 'L' in i]
    r_x_index=copy.deepcopy(long_list)
    r_y_index=copy.deepcopy(long_list)#通り摘出長期軸力摘


#Y通り摘出
    y_name=v_force_list[1]
    while '' in y_name:
        y_name.remove('')
    print(y_name)

    for i in r_y_index:
        del i[ay+2:]
        del i[:2]
    #print(r_y_index)
    aylen=[[len(j) for j in i]for i in r_y_index]
    #print(aylen)
    y_point=[]
    for i in aylen:
        temp=[]
        for j in i:
            if j>0:
                temp.append(j/j)
            else:
                temp.append(0)
        y_point.append(temp)
    #print(y_point)#支点有無 [1or0]
    y_list=[]
    for i in range(ax):
        for j in range(ay):
            temp=y_point[i][j] * int(y_name[j])
            y_list.append(temp)
    print(y_list)
    y_num=[]
    for i in y_list[:]:
        if i>0:
            y_num.append(i)
    print(y_num)

#X通り摘出
    x_name=[]
    for i in r_x_index:
        temp=i[0]
        x_name.append(temp)
    print(x_name)#Y方向通り

    for i in r_x_index:
        while 'L' in i:
            i.remove('L')
    for i in r_x_index:
        while '' in i:
            i.remove('')
    N_hit=[]
    for i in r_x_index:
        N_hit.append(len(i))
    print(N_hit)    #通り支点数＋１
    print(ay)
    x_list=[]
    for i in range(ax):
        i1=x_name[i]
        i2=N_hit[i]-1
        i3=i1*i2
        x_list.append(i3)
    print(x_list)
    x_num=[]
    for i in r_x_index:
        while '' in i:
            x_num.remove('')
    x_num=[n for ni in x_list for n in ni]
    print(x_num)

#軸力整理
    def pikup(list,mark):
        pikup=[i for i in list if mark in i]
        return(pikup)

    def del_text(list):
        for i in list:
            del(i[0:2])
        return(list)

    def del_sp(list):
        while '' in list:
            list.remove('')

    def aone(list):
        aone=[n for ni in list for n in ni]
        return(aone)

    L_N_=pikup(v_force_list,'L')
    LpEx=pikup(v_force_list,'L+Ex')
    LmEx=pikup(v_force_list,'L-Ex')
    LpEy=pikup(v_force_list,'L+Ey')
    LmEy=pikup(v_force_list,'L-Ey')

    del_text(L_N_)
    del_text(LpEx)
    del_text(LmEx)
    del_text(LpEy)
    del_text(LmEy)

    L_N_=aone(L_N_)
    LpEx=aone(LpEx)
    LmEx=aone(LmEx)
    LpEy=aone(LpEy)
    LmEy=aone(LmEy)

    del_sp(L_N_)
    del_sp(LpEx)
    del_sp(LmEx)
    del_sp(LpEy)
    del_sp(LmEy)

    print('----')

    with open("jikuryoku.csv",'w') as fw:
        wr=csv.writer(fw)
        wr.writerow(y_num)
        wr.writerow(x_num)
        wr.writerow(L_N_)
        wr.writerow(LpEx)
        wr.writerow(LmEx)
        wr.writerow(LpEy)
        wr.writerow(LmEy)
