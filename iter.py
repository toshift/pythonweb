# coding: utf-8
class Iterator(object):
    def __init__(self):
        self.counter = 3
    
    def __iter__(self):
        return self

    def next(self):
        self.counter -= 1
        if self.counter < 0:
            raise StopIteration
        return u"わーい!"

class RunTimeIterator(Iterator):
    def __init__(self):
        super(RunTimeIterator, self).__init__()

        for i in self:
            print i
            break
        self.next = self.alter_next

    def alter_next(self):
        self.counter -= 1
        if self.counter < 0:
            raise StopIteration
        return u"たーのしー!"
