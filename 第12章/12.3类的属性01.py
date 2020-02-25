"""
     @property将一个方法转换为属性，调用方法不需要添加（）
      函数体一般以return语句结束
"""


class Rect:
    """
    计算矩形面积
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rect(40, 50)
print("矩形面积为：", rect.area)

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# rect = Rect(40, 50)
# print("矩形面积为：", rect.area())
