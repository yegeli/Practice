"""
    使用队列在线程间进行通信
        生产者消费者模式：
            生产者：产生数据的模块           进
            消费者：处理数据的模块           出
            仓库：生产者与消费者之间的缓冲区  存
"""
from queue import Queue
import threading,random,time

# 通过子类创建线程
class Producer(threading.Thread):
    def __init__(self,name,queue):
        super().__init__(name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("生产者%s将产品%d加入队列！" %(self.getName(),i))
            self.data.put(i)
            time.sleep(random.random())
        print("生产者%s完成！" % self.getName())


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        super().__init__(name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            self.data.get()
            print("消费者%s将产品%d从对列取出！" % (self.getName(), i))
            time.sleep(random.random())
        print("消费者%s完成！" % self.getName())


if __name__ == "__main__":
    print("--------主线程开始--------")
    queue = Queue()
    producer = Producer("Producer",queue)
    consumer = Consumer("Consumer",queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("--------主线程结束--------")
