#coding:utf-8
#taskManager.py for windows

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#任务个数
from queue import Queue

task_number = 10
#定义收发队列
task_queue = Queue.queue(task_number)
result_queue = Queue.queue(task_number)
def get_task():
    return task_queue
def get_result():
    return result_queue

#创建类似的QueueManager:
class QueueManger(BaseManager):
    pass
def win_run():
    QueueManger.register('get_task_queue',callable=get_task)
    QueueManger.register('get_resutl_queue',callable=get_result)
    manager = QueueManger(address=('127.0.0.1',8001),authkey='qiye')
    #启动
    manager.start()
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        #添加任务
        for url in ['','','']:
            print()
    finally:
        manager.shutdown()