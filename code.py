# 开发人：彭协宇
# 开发时间 ：2022/3/5 17:22
import matplotlib.pyplot as plt

n=30
k=30
m=[]
r=[]
r2=[]
for i in range(0,31):#0-30遍历
    m.append(i)
    s1=k*(1-i/n)*(1/(1+k*i/n))
    s2=k*(1-i/n)
    print('缓存大小为：',i)
    print('编码缓存方案：',s1)
    print('为编码方案：',s2)
    r.append(s1)
    r2.append(s2)
# print(type(m))
# print(type(r))
#r=k*(1-m/n)*(1/(1+k*m/n))

plt.plot(m,r)

plt.plot(m,r2)
plt.show()

