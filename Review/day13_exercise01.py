"""
    手雷爆炸，伤害玩家生命（血量减少，闪现红屏），伤害敌人得生命（血量减少，头顶爆字）
    要求：
        可能还增加其他事物，但是布恩那个修改手雷代码

    体会：
        封装：分
        继承：隔
        多态：做
"""

class Granade:
    """
        手雷
    """

    def explode(self,target):
        if isinstance(target,AttackTarget):
            target.damage()

class AttackTarget():
    """
        攻击目标
    """
    def damage(self):
        pass


class Player(AttackTarget):

    def damage(self):
        print("扣血")
        print("闪现红屏")


class Enemy(AttackTarget):

    def damage(self):
        print("扣血")
        print("头顶爆血")


g01 = Granade()
p01 = Player()
e01 = Enemy()
g01.explode(e01)