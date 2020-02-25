"""
    @property不仅可以将属性修改为只读属性，
    还可以对属性设置拦截器，允许对属性进行修改，但修改时需要遵守一定约束
"""


class TVshow:
    '''
    显示电视节目,属性设置为私有的，限制在函数体外修改，只读模式
    '''

    def __init__(self, show):
        self.__show1 = show

    @property
    def show2(self):
        return self.__show1


tvshow = TVshow("正在播放 《战狼2》")
print("默认：", tvshow.show2)

tvshow.show2 = "正在播放 《红海行动》"
print("修改后 " ,tvshow.show2)