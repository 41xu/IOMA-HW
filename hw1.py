"""
说明：
randu(seed,M) -> 生成U(0,1), seed为初始值S0
randn(u,sigma,seed) -> 生成N(u,sigma)
calpi() -> 计算π, res=3.14160
"""

M = 65536 
A = 13
C = 5
seed = 1


def f(pre):
    yield (pre * A + C) % M


def randu(seed=1, M=65536):
    cnt = 1
    last = seed
    res = [last, ]
    while cnt < M:
        last = next(f(last))
        res.append(last)
        cnt += 1
    x = [i / M for i in res]
    return x


def randn(u, sigma, seed=1):
    x = randu(seed)
    res = [sum(x[i * 6:(i + 1) * 6]) for i in range(M // 6)]
    res = [u + sigma * z for z in res]
    return res


def calpi():  # 计算和原点距离=sqrt(x^2+y^2), r=2
    # pi=4*Nc/Ns
    Nc, Ns = 0, 0
    x = iter(randu(3))
    y = iter(randu(6))
    while 1:
        try:
            # if (next(x)*4-2)**2+(next(y)*4-2)**2<=4:
            if next(x) ** 2 + next(y) ** 2 <= 1:
                Nc += 1
            Ns += 1
        except StopIteration:
            break
    return format(4 * Nc / Ns, '.5f')


randn(u=2, sigma=3)
pi = calpi()
print(pi)
