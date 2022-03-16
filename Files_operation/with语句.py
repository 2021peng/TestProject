# 开发人：彭协宇
# 开发时间 ：2022/3/5 19:29

# with open('a.txt','r') as file:
#     print(file.read()) #打开文件后可以不需要close，离开with回自动关闭

"""with语句的执行逻辑：自动调用enter打开文件，自动调用exit关闭文件"""
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')
    def show(self):
        print('show方法被调用了')

with MyContentMgr() as file:
    file.show()

#复制文件操作
with open('李沐.png','rb') as src_file:
    with open('copy2.png','wb') as target_file:
        target_file.write(src_file.read())
