# 开发人：彭协宇
# 开发时间 ：2022/3/5 16:13
import time
import schedule

def job():
    print('哈哈哈哈------')

print(time.time())
schedule.every(3).seconds.do(job)   #每隔3s执行一次job函数
while True:
    schedule.run_pending()
    time.sleep(1)   #每隔3s休眠一次