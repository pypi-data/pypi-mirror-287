import math
import numpy as np

def prd(x):
    return ((31*x**2)+(49*x)+7.8)*(10**-3)

def rld(x):
    return 1400*math.exp(-0.54*x)

def prr(x):
    return ((2.6*x**2)-(4.2*x)+4.8)*(10**-3)

def pratioze(prd_l,ze,rld_l,prr_l):
    return (prd_l * math.exp(-ze/rld_l) + prr_l)

prd_f = np.vectorize(prd)
rld_f = np.vectorize(rld)
prr_f = np.vectorize(prr)
pratioze_f = np.vectorize(pratioze)