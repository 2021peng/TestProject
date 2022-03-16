# 开发人：彭协宇
# 开发时间 ：2022/3/5 18:37

# file = open('a.txt','r')
# print(file.readlines())
# file.close()

# file = open('b.txt','w')
# file.write('hello')
# file.close()

#复制文件操作
# src_file = open('李沐.png','rb') #也可以.jpg
# target_file = open('copy.png','wb')
# target_file.write(src_file.read()) #读出什么就写入进target文件中去
# src_file.close()
# target_file.close()

# file = open('a.txt','r')
# file.seek(2)    #指跳过了两个字节，一个中文两个字节，如果是1会报错
#                 #file.seek(1)
# print(file.read())
# file.close()

