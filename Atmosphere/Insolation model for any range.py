#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
albedoM =-0.01
albedoB =2.8
icelatM=1.5
icelatB=-322.5
epsilon = 1
sigma = 5.67E-8  


# In[ ]:


L1,L2,albedo, nIters, = input("Lrange L1 , L2 , albedo nIters ").split()
L1,L2,albedo, nIters = [ float(L1), float(L2), float(albedo), int(nIters) ]
Temp=lambda albedo:(L*(1-albedo)/(4*sigma))**0.25
albe=lambda T:max(0.15, min(0.65, (albedoB +(albedoM * T))))
alti=lambda T:max(0.0, min(90, (icelatB + (icelatM * T))))


# In[8]:


LRange = [L1,L2]
L=LRange[1]
while L>LRange[0]-1 :
    x_list = []              # an empty list
    y_list = []
    for i in range(nIters):
        T=Temp(albedo)
        Altitude=alti(T)
        albedo=albe(T)
        x_list.append(T)
        y_list.append(albedo)
    plt.plot(range(nIters),x_list,c='r')
    L=L-5   
plt.xlabel('Iteration')
plt.ylabel('T')


# In[ ]:




