import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start thread1')
    for i in range(100):
        print(f'こっちのカウントは{i}')
        time.sleep(2)


def worker2():
    logging.debug('start thread2')
    for n in range(500):
        print(f"countは{n}です")
        time.sleep(5)

if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)

    t1.start()
    t2.start()

    print('started')