"""
模拟高铁售票系统
"""

import prettytable as pt


def show_ticket(seat_line):
    """
     显示票最初始的状态:空座
    :param seat_line:初始行数
    :return: 无
    """
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]

    for i in range(seat_line):
        l = ["第%02d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(l)
    print(tb)


def buy_ticket(seat_line):
    """
    买完票的状态
    :param seat_line: 初始行数
    :return:无
    """
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]

    for i in range(seat_line):
        if row == i + 1:
            l = ["第%02d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
            l[line] = "无票"
            tb.add_row(l)
        else:
            l = ["第%02d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
            tb.add_row(l)
    print(tb)


if __name__ == '__main__':

    nodes = """模拟高铁售票系统：
    每节火车内部有13行
    每排有5个座位
    座位有票会显示：有票
    座位售出会显示：无票
    """
    print(nodes)
    seat_line = 13
    show_ticket(seat_line)
    seat = input("输入您选择座位的行和座位号，用逗号分隔：")

    try:
        row, line = seat.split(',')
        row = int(row)
        line = int(line)
    except:
        print('输入格式错误，如选择第13排5号座位请输入：13,5')
    buy_ticket(seat_line)
