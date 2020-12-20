import numpy as np


def JDS(X):
    """test function J.D. Schaffer, X:[n,2] n points"""
    x1=X[:,0]
    x2=X[:,2]
    fx=4.5-(pow(np.sin(np.sqrt(pow(x1,2)+pow(x2,2))),2)-.5)/pow((1+0.001*(pow(x1,2)+pow(x2,2))),2)
    return fx


if __name__ == '__main__':
    pass