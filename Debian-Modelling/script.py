import numpy as np
from matplotlib import pyplot as plt


in_data = np.genfromtxt('in_squeeze.dat', delimiter='                    ')
in_data_x = in_data[..., 0]
in_data_y_exp = in_data[..., 1]
lamda = 2.2
int_const = 265.0
eeta = -28.0

in_data_y_theoretical = eeta + ((int_const**2)*((in_data_x + lamda)**(-2)))
plt.loglog(in_data_x, in_data_y_exp, 'ob')
plt.savefig('in_exp.png')
plt.loglog(in_data_x, in_data_y_theoretical, 'r')
plt.savefig('in_data.png')

plt.clf()
out_data = np.genfromtxt('out_squeeze.dat', delimiter='                    ')
out_data_x = out_data[..., 0]
out_data_y_exp = out_data[..., 1]
lamda = 0.45
int_const = 110.0
eeta = -28.0

out_data_y_theoretical = eeta + ((int_const**2)*((out_data_x + lamda)**(-2)))
plt.loglog(out_data_x, out_data_y_exp, 'ob')
plt.savefig('out_exp.png')
plt.loglog(out_data_x, out_data_y_theoretical, 'r')
plt.savefig('out_data.png')
