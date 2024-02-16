import pandas as pd

a = pd.read_csv("data.csv")

b = a["c1"]
c = a["c2"]


def d(e, f):
    return e + f


g = d(b, c)

print(g)
