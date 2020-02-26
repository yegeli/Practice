"""
推算几天后的日期
"""
import datetime


def inputdate():
    """
    输入日期
    :return:date
    """
    indate = input("请输入日期后按<enter>键结束(如20200224，输入为空则默认为当天日期)：")
    indate = indate.strip()
    if len(indate) == 0:
        return datetime.date.today()
    else:
        if len(indate) == 8:
            datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:8]
            return datetime.datetime.strptime(datestr, "%Y-%m-%d")
        else:
            print("输入错误，按当前日期推算")
            return datetime.date.today()





def calculate_date():
    """
    推算日期
    :return:无
    """
    sdate = inputdate()
    interval_time = input("输入间隔天数后按<enter>键结束（输入负数，往前推算）：")
    if int(interval_time) != 0:
        fdate = sdate + datetime.timedelta(days=int(interval_time))
        fdate = datetime.datetime.strftime(fdate, "%Y-%m-%d")
        print("您推算的日期为：%s" % fdate)
    else:
        print("输入有误，程序退出！")

print("******************推算几天后的日期**********************")
while True:

    calculate_date()
    s = input("是否要继续推算y/n:")
    if s == 'n':
        break

