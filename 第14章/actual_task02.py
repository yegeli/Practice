"""
模拟淘宝客服自动回复：

"""


def get_answer(question):
    with open("reply.txt",'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            key = line.split('|')[0]
            reply = line.split('|')[1]
            if key in question:
                return reply
        return False

if __name__ == '__main__':
    question = input("亲，您想要咨询什么问题：")
    while True:
        if question == 'bye':
            break
        reply = get_answer(question)
        if not reply:
            message="亲，您咨询的问题已超过我的能力范围，请输入关键词咨询，如订单、物流、账户、支付（退出请输入bye）："
            question = input(message)
        else:
            print(reply)
            message = "亲，您可以输入关键词咨询，如订单、物流、账户、支付（退出请输入bye）："
            question = input(message)
    print("亲，再见呐，么么哒！")

