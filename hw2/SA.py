import numpy as np
import random

step = 0.1  # 精度
nb = []  # neighbour，选在了x1,x2 [-5,5]这个范围里的所有点，step=0.01存的是(x1,x2)
min_ = -100  # 下界
max_ = 100  # 上界
T0 = 100  # initial T
r = 0.99  # 降温rate
Tf = 0.1  # 这样设置循环687次，感觉还行


def JDS(x1, x2):
    """test function J.D. Schaffer, also the fitness function"""
    fx = 4.5 - (pow(np.sin(np.sqrt(pow(x1, 2) + pow(x2, 2))), 2) - .5) / pow((1 + 0.001 * (pow(x1, 2) + pow(x2, 2))), 2)
    return fx


def E(x1, x2):  # energy要找min，JDS要找max，所以加了负号
    return -JDS(x1, x2)


def init():
    global x1, x2, nb
    x1, x2 = random.uniform(min_, max_), random.uniform(min_, max_)
    update_neighbour(x1, x2)
    return x1, x2


def update_neighbour(x1, x2):
    global nb
    nb = []
    t1, t2 = 0, 0
    for i in range(-50, 51):
        t1 = x1 + step * i
        for j in range(-50, 51):
            t2 = x2 + step * j
            nb.append((t1, t2))


def SA():
    x1, x2 = init()
    Tk=T0
    while Tk>=Tf:
        n=0
        Ecur=E(x1,x2)
        Enb=[E(t1,t2) for t1,t2 in nb]
        j=random.randint(0,len(Enb)-1)
        if Enb[j]-Ecur<0:
            x1,x2=nb[j]
        else:
            epsilon=random.random()
            if np.exp(-(Enb[j]-Ecur)/Tk)>epsilon:
                x1,x2=nb[j]
            else:





if __name__ == '__main__':
    pass
