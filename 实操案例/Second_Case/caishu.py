# 开发人：彭协宇
# 开发时间 ：2022/3/7 18:59
import random

rand = random.randint(1,100)
print('在我心中有个数，在1-100之间，请你猜一猜。')
for i in range(1,11):
    num = int(input('你猜测的结果为：'))
    if num<rand:
        print('小了')
    elif num>rand:
        print('大了')
    else:
        print('恭喜你，成功走进我心里！')
        break
print(f'您一共猜了{i}次')

end = input('按任意键结束！')


