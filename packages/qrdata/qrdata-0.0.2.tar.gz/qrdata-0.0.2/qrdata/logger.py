#给定一个qtextedit控件，提供一个log函数，该函数接收字符串输入可以输出到qtextedit控件中
class Logger:
    def __init__(self, qtextedit):
        self.qtextedit = qtextedit
    def log(self, msg):
        self.qtextedit.append(msg)
