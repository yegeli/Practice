"""
    迭代器：---> yield
"""


class InformationController:
    def __init__(self):
        self.__list_infos = []
        self.index = 0

    def add_info(self, info):
        self.__list_infos.append(info)

    def __iter__(self):
        while self.index < len(self.__list_infos):
            yield self.__list_infos[self.index]
            self.index += 1


controller = InformationController()
controller.add_info("野哥")
controller.add_info("打法")
controller.add_info("撒打发而奋斗")
controller.add_info("啊师傅打耳光")
controller.add_info("色法国")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        time = iterator.__next__()
        print(time)
    except StopIteration:
        break
