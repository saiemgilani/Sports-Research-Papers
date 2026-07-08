from scipy.stats import norm
import sys
import os
import pandas as pd
import numpy as np
from scipy import optimize

# this is the regularization parameter
l = 2

df = pd.read_csv("data.csv")

cols = [c for c in df.columns if c.startswith('P')]

players = list(set(set(df.P1.unique()) | set(df.P2.unique())| set(df.P3.unique())| set(df.P4.unique()) | set(df.P5.unique()) | set(df.P6.unique()) | set(df.P7.unique()) | set(df.P8.unique()) | set(df.P9.unique()) | set(df.P10.unique())))

print players, len(players)

df.P1 = df.P1.apply(lambda x: players.index(x)+1)
df.P2 = df.P2.apply(lambda x: players.index(x)+1)
df.P3 = df.P3.apply(lambda x: players.index(x)+1)
df.P4 = df.P4.apply(lambda x: players.index(x)+1)
df.P5 = df.P5.apply(lambda x: players.index(x)+1)
df.P6 = df.P6.apply(lambda x: players.index(x)+1)
df.P7 = df.P7.apply(lambda x: players.index(x)+1)
df.P8 = df.P8.apply(lambda x: players.index(x)+1)
df.P9 = df.P9.apply(lambda x: players.index(x)+1)
df.P10 = df.P10.apply(lambda x: players.index(x)+1)

def apm_constr(x):
    return np.mean(x)


def obj(x):
    val_cols = [c for c in df.columns if c.startswith('P')]
    home_pred = df[val_cols[0:5]].apply(lambda i: x[i-1]).sum(axis=1)
    away_pred = df[val_cols[5:10]].apply(lambda i: x[i-1]).sum(axis=1)
    pred_diff = home_pred - away_pred
    regularizer = l*(x**2).sum()
    err = ((df.Result - pred_diff)**2).sum() + regularizer 
    return err


x0 = np.zeros(shape=len(players))

res = optimize.minimize(obj,x0,constraints=[{'type':'eq', 'fun':apm_constr}], method="SLSQP",
                        options={'maxiter':10000,'disp':True})

print("                Player   APM")
for i in range(len(x0)):
    print("{:>20s}    {:.4f}".format("P"+str(players[i]), res.x[i]))
