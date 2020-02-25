"""
    设计药品类
"""

from datetime import datetime

class Medicine():
    def __init__(self, name, price, PD, Exp):
        """
        初始化函数
        :param name:药名
        :param price: 价格
        :param PD: 生产日期
        :param Exp: 失效日期
        """
        self.name = name
        self.price = price
        self.PD = PD
        self.Exp = Exp

    def get_name(self):
        """
        获取药品名称
        :return: str
        """
        return self.name

    def get_GP(self):
        """
        计算保质期（失效日期和生产日期的时间间隔）
        :return: str
        """
        start = datetime.strptime(self.PD,'%Y-%m-%d')
        end  = datetime.strptime(self.Exp,'%Y-%m-%d')
        return (end-start).days


medicine = Medicine('格列宁',1860,'2018-5-1','2018-12-1')
name = medicine.get_name()
GP = medicine.get_GP()

print('药品名称：{}'.format(name))
print('药品保质期：{}天'.format(GP))