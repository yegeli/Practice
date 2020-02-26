"""
    模块之间的调用
    每个模块中都包括一个记录模块名称的变量__name__,一般模块执行时都在解释器的顶级模块中，顶级模块的__name__变量值为：__main__
"""
pinetree = '我是一棵松树'


def fun_christmastree():
    """
    功能：一个梦
    :return: 无
    """
    pinetree = '挂上彩灯，礼物.....我变成一颗圣诞树 o(*￣▽￣*)ブ\n'
    print(pinetree)


if __name__ == '__main__':
    print("\n下雪了....\n")
    print('=========================开始做梦了====================\n')
    fun_christmastree()
    print('==========================梦醒了=======================\n')
    pinetree ="我身上落满雪花，" + pinetree
    print(pinetree)
