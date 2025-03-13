'''
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
如果庄家获胜，玩家就会输掉自己下注的金额。
游戏结束的条件是玩家破产（输光所有的赌注）。
'''
import random
import numpy as np
import pandas as pd



a_lst=[]
b_lst=[]
c_lst=[]
result=[]
out_in=[]
money_lst=[]
num_lst=[]


num=0
money=1000
while money>0 and num<1000:
    choice = min(random.randint(20, 50), money)  # 确保下注不超过当前资金
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=a+b

    if c in [7,11]:
        print("玩家胜")
        result.append("玩家胜")
        money+=choice
        out_in.append(choice)
        money_lst.append(money)
        a_lst.append(a)
        b_lst.append(b)
        c_lst.append(c)
        num+=1
        num_lst.append(num)
    elif c in [2,3,12]:
        print("庄家胜")
        result.append("庄家胜")
        money-=choice
        out_in.append(-choice)
        money_lst.append(money)
        a_lst.append(a)
        b_lst.append(b)
        c_lst.append(c)
        num+=1
        num_lst.append(num)
    else:
        print("未分出胜负，重新摇")
        while True:
            a1=random.randint(1,6)
            b1=random.randint(1,6)
            c1=a1+b1
            if c1==7:
                print("庄家胜")
                result.append("庄家胜")
                money-=choice
                out_in.append(-choice)
                money_lst.append(money)
                a_lst.append(a)
                b_lst.append(b)
                c_lst.append(c)
                num+=1
                num_lst.append(num)
                break
            elif c1==c:
                print("玩家胜")
                result.append("玩家胜")
                money+=choice
                out_in.append(choice)
                money_lst.append(money)
                a_lst.append(a)
                b_lst.append(b)
                c_lst.append(c)
                num+=1
                num_lst.append(num)
                break
            else:
                print("未分出胜负，重新摇")
                continue

print(f"money={money},\n,num={num}")

colomns_lst=["局数","a","b","c","本局结果","流水","剩余金额"]
datas=[num_lst,a_lst,b_lst,c_lst,result,out_in,money_lst]


data_dict=dict(zip(colomns_lst,datas))

df=pd.DataFrame(data=data_dict)
df.to_csv("./赌博记录.csv",index=False)

import seaborn as sns
import matplotlib.pyplot as plt
# 设置 Matplotlib 全局字体为支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
sns.scatterplot(df,x="局数",y="剩余金额",hue="本局结果")
plt.show()
