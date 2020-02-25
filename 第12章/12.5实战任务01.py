"""
     模拟银行账户资金交易管理
"""
import time
import prettytable as pt

balance = 1000
log = []


class Bank:
    '''
        银行类
    '''

    def __init__(self):
        """
            初始化函数
        """
        global balance
        self.balance = balance
        self.log = log

    def depost(self):
        """
            存款
        :return: 无
        """

        money = float(input("输入存款金额："))
        self.balance += money
        self.write_log("转入", money)

    def withdring_money(self):
        """
            取款
        :return:无
        """
        money = float(input("输入取款金额："))
        if money > self.balance:
            print("余额不足")
        else:
            self.balance -= money
            self.write_log("消费", money)

    def write_log(self, summary_info, money):
        """
            写入日志
        :return:无
        """
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取创建时间
        data = [create_time, summary_info, money, self.balance]
        self.log.append(data)

    def print_record(self):
        """
            打印交易凭单
        :return:无
        """
        tb = pt.PrettyTable()
        tb.field_names = ["交易日期", "摘要", "金额", "币种", "余额"]
        for info in self.log:
            if info[1] == '转入':
                money = '+{}'.format(info[2])
            else:
                money = '-{}'.format(info[2])
            tb.add_row([info[0], info[1], money, '人民币', info[3]])
        print(tb)


def show_menu():
    """
        显示菜单
    :return: 无
    """
    menu = """菜单：
    0：退出
    1：存款
    2: 取款
    3：打印交易凭单
    """
    print(menu)


if __name__ == "__main__":
    print("银行交易流水模拟:" + '\n')
    show_menu()
    print("初始余额为：" + str(balance)+'\n')
    bank = Bank()
    num = float(input("请根据菜单输入操作编号："))
    while num != 0:
        if num == 1:
            bank.depost()
        elif num == 2:
            bank.withdring_money()
        elif num == 3:
            bank.print_record()
        else:
            print("您输入有误")
        num = float(input("请根据菜单输入操作编号："))

    print("您已退出系统")

