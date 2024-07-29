import numpy as np

def funcion_clase(x):
    r = x**2 + 3
    return np.sum(r)

def lata(x):
    r = 2*np.pi*x**2+500/x
    return np.sum(r)

def caja(L):
    r = (-1)*((200*L)-(60*(L**2))+(4*(L**3)))
    return np.sum(r)

def caso1(x):
    r = (x**2)+(54/x)
    return np.sum(r)

def caso2(x):
    r = (x**3) + (2*x) -3
    return np.sum(r)

def caso3(x):
    r = (x**4) + (x**2) - 33
    return np.sum(r)

def caso4(x):
    r = (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)
    return np.sum(r) 