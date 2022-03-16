# 开发人：彭协宇
# 开发时间 ：2022/3/3 9:54

#ctrl + / 整体注释
# fp = open('E:/test.txt','a+')
# print('first_input','second_input',file=fp)
# fp.close()
# #不换行就用，隔开
# print('hello','world')

# def calc(a,b):
#     c=a+b
#     return c
# result = calc(10,20)
# print(result)

def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)

n1 = 11
n2 = [22,33,44]
print(n1)
print(n2)
print('-------------------')
fun(n1,n2)
print(n1)
print(n2)
# 在函数调用过程中，进行参数的传递
# 如果是不可变对象，
# 在函数体的修改不会影响实参的值argl的修改为100，不会影响n1的值
# 如果是可变对象，在函数体的的修改会影响到实参的值arg2的修改， append(10)， 会影响到n2的值
print('-------------------')
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2 ==0:
            odd.append(i)
        else:
            even.append(i)

    return odd,even

lst = [10,29,34,23,44,53,56]
print(fun(lst))
# 函数的返回值
# (1)如果函数没有返回值[函数执行完毕之后，不需要给调用处提供数据] return可以省略 不写
# (2)函数的返回值，如果是1个，直接返回类型
# (3)函数的返回值，如果是多个，返回的结果为元组
# 函数是否需要return视情况而定
