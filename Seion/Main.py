from queue import Queue
from multiprocessing import Process
from Seion.Manager import Manager

url_q = Queue()
result_q = Queue()
store_q = Queue()
conn_q = Queue()
#创建分布式管理器
node = Manager()
manager = node.start_manager(url_q,result_q)
#创建URL管理进程，数据提取进程和数据存储进程
url_manager_proc = Process(target=node.url_manager_proc,args=(url_q,conn_q,
                                                              'http://baike.baidu.com/view/284853.htm',))
result_solve_proc = Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q,))
store_proc = Process(target=node.store_proc,args=(store_q))
 #启动3个进程和分布式管理器
url_manager_proc.start()
result_solve_proc.start()
store_proc.start()
manager.get_server().serve_forever()
