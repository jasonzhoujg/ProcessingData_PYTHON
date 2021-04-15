import numpy as np
import matplotlib.pyplot as plt
import math as m

def extract_para(file):
    with open(file, "r") as f: #可以在程序正常或者非正常结束的时候都可以正常关闭文档
        fre = []
        s = []
        for line in f.readlines()[3:]:
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            line = line.split()  #以空行为分隔符
            try:
                fre.append(float(line[0]))
                s.append(float(line[1]))
            except:
                break

    fre = np.array(fre)
    s = np.array(s)
    return fre,s


fre,s11_r = extract_para("data - post/s11_r.txt")
fre,s11_i = extract_para("data - post/s11_i.txt")
fre,s21_r = extract_para("data - post/s21_r.txt")
fre,s21_i = extract_para("data - post/s21_i.txt")

# fre,s11_r = extract_para("data2/s11_r.txt")
# fre,s11_i = extract_para("data2/s11_i.txt")
# fre,s21_r = extract_para("data2/s21_r.txt")
# fre,s21_i = extract_para("data2/s21_i.txt")

fre,s21 = extract_para("data - post/s21.txt")
fre,s11 = extract_para("data - post/s11.txt")

fre,s21_p = extract_para("data - post/s21_p.txt")
fre,s11_p = extract_para("data - post/s11_p.txt")


c = 3e8
d = 0.812e-3
N = len(fre)
S11 = s11_r+s11_i*1j
S21 = s21_r+s21_i*1j
kd = np.zeros(N)
n1 = np.zeros(N,dtype = complex)
z1 = np.zeros(N,dtype= complex)
kd = d*2*np.pi*fre*1e9/c

for i in range(0,N):
    z1[i] = np.sqrt(((1 + S11[i]) ** 2 - S21[i] ** 2)/((1 - S11[i]) **2 - S21[i] ** 2))
    if z1[i].real > 0:
        z1[i] = z1[i]
    else:
        z1[i] = -z1[i]

    s = (1 - S11[i] ** 2 + S21[i] ** 2) / 2 / S21[i]
    n1[i] = np.arccos(s)
    n1[i] = n1[i]/kd[i]

    if n1[i].imag > 0:
        n1[i] = n1[i]
    else:
        n1[i] = -n1[i]

mu = n1*z1
epsilon = n1/z1
plt.figure()
#画S11和S21的图形
# plt.style.use('ggplot')

# plt.plot(fre,s11_r,color = 'red',label="s11_real")
# plt.plot(fre,s11_i,color = 'blue',label="s11_imag",linestyle = "--")
# plt.plot(fre,s21_r,color = 'yellow',label="s21_real")
# plt.plot(fre,s21_i,color = 'green',label="s21_imag",linestyle = "--")
# plt.title("S11 and S21")

# plt.plot(fre,s11,color = 'blue',label="s11",linestyle = "--")
# plt.plot(fre,s21,color = 'red',label="s21")
# plt.title("Magnitude of S11 and S21")

# plt.plot(fre,s11_p,color = 'blue',label="s11",linestyle = "--")
# plt.plot(fre,s21_p,color = 'red',label="s21")
# plt.title("Phase of S11 and S21")
#
# plt.plot(fre,n1.imag,color = 'blue',label="n_imag",linestyle = "--")
# plt.plot(fre,n1.real,color = 'yellow',label="n_real")
# plt.plot(fre,n1,color = 'red',label="n")
# plt.title("Refraction Index")

# plt.plot(fre,mu.real,color = 'red',label="mu_real")
# plt.plot(fre,mu.imag,color = 'blue',label="mu_imag",linestyle = "--")
# plt.plot(fre,epsilon.real,color = 'yellow',label="epsilon_real")
# plt.plot(fre,epsilon.imag,color = 'purple',label="epsilon_imag",linestyle = "--")
# plt.title("Effective Permittivity and Permeability ")


plt.xlabel("frequency/GHz")# 设置横轴标签
#plt.ylabel("n")# 设置纵轴标签
plt.legend(loc="upper right")
plt.show()






