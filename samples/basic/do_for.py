# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)

for item in 'accccd':
    print(item);



    for a in range(10):
        # fp = open("/Users/zhangxixiang/Downloads/test"+str(a),'w');
        if(a % 2 == 0):
            print(a);


def invest(amount,rate,time):
    return amount*(1+rate)*time;

print('投资回报'+str(invest(1000,0.05,2)));



import random

point1 = random.randrange(1,22);
point2 = random.randrange(1,22);
point3 = random.randrange(1,22);
point4 = random.randrange(1,22);
point5 = random.randrange(1,22);

print(point1,point2,point3,point4,point5);




