# 开发人：彭协宇
# 开发时间 ：2022/3/7 18:42

#两种文件读写操作
file = open('C:/Users/admin/PycharmProjects/TestProject/实操案例/First_Case/test1.txt','w')
print('好好学习，天天向上！',file=file)
file.close()

with open('C:/Users/admin/PycharmProjects/TestProject/实操案例/First_Case/test2.txt','w') as file:
    file.write('好好学习，天天向上！')

