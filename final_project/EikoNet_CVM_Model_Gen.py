#!/usr/bin/env python
# coding: utf-8


## Normal Python Libraries

import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
from scipy import signal
import numpy as np
from scipy import interpolate
import pandas as pd
from pyproj import Proj
import copy
import os
from os import path
from base64 import b64encode

## Import EikoNet Libraries

from EikoNet import model as md
from EikoNet import database as db
from EikoNet import plot as pt 

## Import pytorch Libraries

import torch
from torch.nn import Linear
from torch import Tensor
from torch.nn import MSELoss
from torch.optim import SGD, Adam, RMSprop
from torch.autograd import Variable, grad
from torch.utils.data.sampler import SubsetRandomSampler,WeightedRandomSampler




# Read in the cvm. 
# df = pd.read_csv("/Users/banjo/uw/classes/bjohnson_repo/final_project/util/brem_cvm.csv")




xmin = [-122.77,47.46,0]
xmax = [-122.29,47.93,50]
projection = "+proj=utm +zone=10, +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
ipath = "/Users/banjo/uw/classes/bjohnson_repo/final_project/util"
opath = "/Users/banjo/uw/classes/bjohnson_repo/final_project/cvm_testing"
file = "brem_cvm_eikonet_.csv"
pnsn = db.PNSN_CVM(xmin=xmin,xmax=xmax,projection=projection,phase='VP',path=ipath,file=file)
cvm = db.Database(opath,pnsn,create=True,randomDist=True)




# cvm = db.Database(path,pnsn,create=True,randomDist=True)
#output = "/Users/banjo/uw/classes/bjohnson_repo/final_project/cvm_testing"
#model_VP = md.Model(output,pnsn,device='cpu')




# model_VP.Params['Training']['Number of sample points']   = 1e4
# model_VP.Params['Training']['Batch Size']                = 64
# # model_VP.Params['ModelPath'] = output

# model_VP.train()


# Xp is your grid points and Yp is the velocity at the grid points. 
# The way they have it set up is :
#     they define the grid points,
#     send the grid points to a program
#     then calculate the velocity at those grid points. 
#     
# What is the issue with us:
#     We have the grid points extablished:
#         --> We do not need to define grid points and calulate the velocity at those grid points.
#     Xp IS based on a Random Generation of points. 
#     --> Does this mean we need to rewrite the Database code to not require a random generation, Xp?
