"""
    使用队列在线程间通信
        生产者类Producer，消费者类Consumer
        生产这生成5件产品，依次写入队列
        消费者依次从队列中提取产品
"""
from queue import Queue
import random, threading, time


class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("生产者%s将产品%d加入队列！" % (self.getName(),i))
            self.data.put(i)
            time.sleep((random.random()))
        print("生产者%s完成！" % self.getName())


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        super(Consumer, self).__init__(name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("消费者%s将产品从%d队列中取出！" % (self.getName(), val))
            time.sleep(random.random())
        print("消费者%s完成！" % self.getName())

if __name__ == '__main__':
    print('------主线程开始------')
    queue = Queue()
    producer = Producer('Producer',queue)
    consumer = Consumer('Consumer',queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("-----主线程结束------")
