"""
    模拟倒计时程序
"""
import datetime
now = datetime.datetime.today()
print(" \033[0;31m                         Today  " )
print(" \033[1;31m                {} 年 {} 月 {} 日".format(now.year,now.month,now.day) )
print(" \033[1;31m 距离： " )
Countdown= datetime.datetime.strptime('2020-6-7','%Y-%m-%d')
detla=Countdown-now
day=detla.days
print(" \033[0;32m 2020年高考还有：  "+  str(day) +" 天")
Countdown= datetime.datetime.strptime('2020-7-24','%Y-%m-%d')
detla=Countdown-now
day=detla.days
print(" \033[0;34m 东京奥运会还有：  "+  str(day) +" 天")
Countdown= datetime.datetime.strptime('2022-2-4','%Y-%m-%d')
detla=Countdown-now
day=detla.days
print(" \033[0;31m 北京冬奥会还有：  "+  str(day) +" 天")
Countdown= datetime.datetime.strptime('2022-11-21','%Y-%m-%d')
detla=Countdown-now
day=detla.days
print(" \033[0;33m 卡塔尔世界杯还有：  "+  str(day) +" 天")

Countdown= datetime.datetime.strptime('2020-6-5','%Y-%m-%d')
detla=Countdown-now
day=detla.days
print(" \033[0;33m 亲爱的小宝贝生日：  "+  str(day) +" 天")

Countdown= datetime.datetime.strptime('2019-11-11','%Y-%m-%d')
detla=Countdown-now
day=abs(detla.days)
print(" \033[0;33m 和亲爱的在一起：  "+  str(day) +" 天")

print(datetime.datetime.today())

print("\033[0;34m")
print("*" * 10)
print("武汉加油")
print("*" * 10)
print("\033[0m")


print(" \033[0;32m 今天我们学习参数问题，加油哦！")
print(" \033[0;33m 今天我们学习参数问题，加油哦！")
print(" \033[0;34m 今天我们学习参数问题，加油哦！")
print(" \033[0;35m 今天我们学习参数问题，加油哦！")

print(datetime.datetime.strftime())