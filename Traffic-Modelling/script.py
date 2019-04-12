import numpy as np
from matplotlib import pyplot as plt

traffic_dat=np.genfromtxt('traffic_time.dat', delimiter='      ')
traffic_dat_time=traffic_dat[...,1]
traffic_dat_west=traffic_dat[...,2]
traffic_dat_east=traffic_dat[...,0]

int_const_A=44.0
mu=8.53
lamda=0.19
beta=-0.09
e_val=2.71828

traffic_exp_west=int_const_A*(mu+(traffic_dat_time**2))*(e_val**(-1*((lamda*traffic_dat_time-beta)**2)))

plt.plot(traffic_dat_time, traffic_dat_west, 'b')
plt.savefig('exp_traffic_west.png')
plt.plot(traffic_dat_time,traffic_exp_west,'r')
plt.savefig('west_model.png')

plt.clf()

int_const_A=44.1
mu=10.5
lamda=0.22
beta=0.24

traffic_exp_east=int_const_A*(mu+(traffic_dat_time**2))*(e_val**(-1*((lamda*traffic_dat_time-beta)**2)))

plt.plot(traffic_dat_time, traffic_dat_east, 'b')
plt.savefig('exp_traffic_east.png')
plt.plot(traffic_dat_time,traffic_exp_east,'r')
plt.savefig('east_model.png')