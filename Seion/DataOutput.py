import codecs
import time
class DataOutput(object):
    def __init__(self):
        self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) )
