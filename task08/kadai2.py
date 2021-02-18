import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(thread):
    logging.debug(f'start thread: {thread}')
    time.sleep(15)
    logging.debug(f'end thread: {thread}')

if __name__ == '__main__':
    threads = []
    counter = 0

    for _ in range(5):
        counter += 1
        t = threading.Thread(target=worker1, args=(str(counter),))
        t.setDaemon(True)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    print("all ended")