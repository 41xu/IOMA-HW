import random
import numpy as np

NG = 100  # 迭代次数
TL = int(np.sqrt(NG))  # tabu table length 禁忌长度
tabu = []  # tabu table, 存的也是(x1,x2)
min_ = -100  # 下界
max_ = 100  # 上界
best = 0  # 历史最优, 也是渴望水平
cur = 0  # 当前解
step = 0.1  # 精度
nb = []  # neighbour，选在了x1,x2 [-5,5]这个范围里的所有点，step=0.01存的是(x1,x2)
INF = -1000


def JDS(x1, x2):
    """test function J.D. Schaffer, also the fitness function"""
    fx = 4.5 - (pow(np.sin(np.sqrt(pow(x1, 2) + pow(x2, 2))), 2) - .5) / pow((1 + 0.001 * (pow(x1, 2) + pow(x2, 2))), 2)
    return fx


def init():
    global x1, x2, nb, best
    x1, x2 = random.uniform(min_, max_), random.uniform(min_, max_)
    best = JDS(x1, x2)
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


def update_tabu(x1, x2):
    global tabu
    if len(tabu) < TL:
        tabu.append((x1, x2))
    elif len(tabu) == TL:
        tabu = tabu[1:] + [(x1, x2)]


def TS():
    x1, x2 = init()
    global best, nb
    for _ in range(NG):
        # print(x1,x2,best)
        update_neighbour(x1, x2)
        cur = JDS(x1, x2)
        nbv = [JDS(t1, t2) for t1, t2 in nb]
        i = np.argmax(nbv)
        curb = nbv[i]  # 邻域当前最好解
        if curb > best:  # 满足渴望水平，更新best,cur,(x1,x2)
            best = curb
            cur = curb
            x1, x2 = nb[i]
        elif curb < best:
            while True:
                if nb[i] not in tabu:
                    cur = curb
                    x1, x2 = nb[i]
                    break
                else:
                    nbv[i] = INF  # 在禁忌表，重选邻域里最大的
                    i = np.argmax(nbv)
                    curb = nbv[i]
    print(x1, x2, best)


if __name__ == '__main__':
    TS()
    """
    res; 
    x1,x2, maxf(x1,x2): 0.018359276683048265 -0.025445725004183295 4.999014792499359
    """
