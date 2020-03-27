
"""
    游戏2048
"""

list_merge = [0,0,0,0]

list_map = [
    [2,0,0,2],
    [0,2,0,2],
    [4,0,2,2],
    [2,0,4,4],
]

def zero_to_end():
    """
        将0元素移动到末尾
    """
    for i in range(len(list_merge) - 1):
        for r in range(i+1,len(list_merge)):
            if list_merge[i] ==0:
                list_merge[i],list_merge[r] = list_merge[r],list_merge[i]


def merge():
    """
        合并数据
    """
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] != 0 and list_merge[i] == list_merge[i+1]:
            del list_merge[i+1]
            list_merge.append(0)

def move_left():
    """
        将list_map元素向左移动,0元素向后移动
    """
    global list_merge
    for line in list_map:
        list_merge = line
        merge()

def move_right():
    """
        将list_map元素向右移动，0元素向左移动
    """
    global list_merge
    for line in list_map:
        list_merge = line[::-1]
        merge()
        line[::-1] =list_merge


def matrix_transposition():
    """
        矩阵转换
    """
    for c in range(1,len(list_map)):
        for r in range(c,len(list_map)):
            list_map[r][c-1],list_map[c-1][r] = list_map[r][c-1],list_map[c-1][r]

def move_up():
    matrix_transposition()
    move_left()
    matrix_transposition()

def move_down():
    matrix_transposition()
    move_right()
    matrix_transposition()

move_down()
print(list_map)





