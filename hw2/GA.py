import random
import numpy as np


NP = 1000  # number of population 种群规模
NG = 200  # 最大代数
L = 11  # 染色体编码长度
CL = L * 2  # x1,x2
Pc = 0.9  # crossover rate 交叉率
Pm = 0.1  # mutation rate 变异率
min_ = -100  # 下界
max_ = 100  # 上界
"""
X~[-100,100], 好像不太适合binary code
编码精度C=0.01 200/(2^L-1)≤0.01 => L=11
由于是两个x1,x2因此L=11*2
"""


def JDS(x1, x2):
    """test function J.D. Schaffer, also the fitness function"""
    fx = 4.5 - (pow(np.sin(np.sqrt(pow(x1, 2) + pow(x2, 2))), 2) - .5) / pow((1 + 0.001 * (pow(x1, 2) + pow(x2, 2))), 2)
    return fx


def random_individual():
    x = [1 if random.random() > 0.5 else 0 for _ in range(CL)]
    x = np.array(x)
    return x


def population_init():
    populations = []
    for i in range(NP):
        populations.append(random_individual())
    return populations


def decode(x):
    """二进制编码变回十进制x
    x=min+二进制转的十进制x(max-min)/(2^L-1)
    input: x 二进制串
    """
    x = [str(_) for _ in x]
    x1 = x[:L]
    x2 = x[L:]
    x1 = int(''.join(x1), 2)
    x2 = int(''.join(x2), 2)
    tx1 = min_ + x1 * (max_ - min_) / (pow(2, L) - 1)
    tx2 = min_ + x2 * (max_ - min_) / (pow(2, L) - 1)
    return tx1, tx2


def selection(popus):
    """正比选择+旋转赌轮法选父本母本，return的结果是正比选择后的下一代"""
    fits = []
    next_popus = []
    for x in popus:
        x1, x2 = decode(x)
        fits.append(JDS(x1, x2))
    fits = np.array(fits)
    sumfit = sum(fits)
    ps = [_ / sumfit for _ in fits]  # 选择概率
    pps = [sum(ps[:i + 1]) for i in range(NP)]
    for i in range(NP):
        seed = random.random()
        tmp = 0
        for j in range(NP):
            if seed < pps[j]:
                tmp = j
                break
        next_popus.append(popus[tmp])
    return np.array(next_popus)


def crossover(popus):
    """做一个简单的双切点交叉"""
    res = []
    for i in range(NP // 2):
        father = popus[i]
        mather = popus[i + NP // 2]
        ft, mt = father, mather
        if random.random() < Pc:
            w = random.randint(0, 1)  # 在x1上交叉还是x2上交叉, 0 x1 1 x2
            p1 = random.randint(L * w, L * w - 2 + L)
            p2 = random.randint(p1 + 1, L * w - 1 + L)
            tmp1 = father[p1:p2 + 1]
            tmp2 = mather[p1:p2 + 1]
            ft = np.concatenate((father[:p1], tmp2, father[p2 + 1:]))
            mt = np.concatenate((mather[:p1], tmp1, mather[p2 + 1:]))
        res.append(ft)
        res.append(mt)
    return np.array(res)


def mutation(popus):
    for i in range(NP):
        if random.random() < Pm:
            p = random.randint(0, L - 1)
            popus[i][p] = 0 if popus[i][p] == 1 else 1
    return popus


def GA():
    popus = population_init()
    for _ in range(NG):
        popus = mutation(crossover(selection(popus)))
    # 找fitness value max的
    tmp = []
    for x in popus:
        x1, x2 = decode(x)
        tmp.append(JDS(x1, x2))
    tmp = np.array(tmp)
    res = tmp.argmax()
    print(tmp[res], popus[res])
    x1, x2 = decode(popus[res])
    print(x1, x2)


if __name__ == '__main__':
    GA()
    """
    res: 4.9902189861827875 [0 1 1 1 1 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1] 
    解码后x1,x2: -1.221299462628238 2.8822667318026447
    """
