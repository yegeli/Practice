"""
输出福彩3D号码

"""

import random


def ball3d():
    """
    产生三个随机数号码
    :return: str
    """
    ball_random = ""
    numbers = '0123456789'
    for i in range(3):
        ball_random += str(random.choice(numbers))

    return ball_random


def input_new():
    """
    输入三个固定的投注号码
    :return: str 三位数
    """
    new_number = input("输入3个投注号码(只能为三位数字)：")
    new_number = new_number.strip()
    return new_number


def check_input():
    """
    检查输入是否正确
    :return: str 三位数
    """
    instr = input_new()
    if len(instr) == 3 and instr.isdigit():
        return instr
    else:
        print("输入投注号码错误，请重新输入：")


if __name__ == '__main__':
    note = '''输出福彩3D号码：
   输入3个固定投注号码
   随机生产3个投注号码
    '''
    print(note)
    inball = []
    while len(inball) < 3:
        inball.append(check_input())
        if None in inball:
            inball.remove(None)
    #print(inball)
    inball.append(ball3d())
    inball.append(ball3d())
    inball.append(ball3d())
    print("您的福彩号码如下：")
    print(('\n').join(inball))