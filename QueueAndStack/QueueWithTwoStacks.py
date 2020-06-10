class QueueWithTwoStacks(object):
    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def appendTile(self, x):
        self._queue1.append(x)

    def deleteHead(self):
        if self._queue2:
            return self._queue2.pop()
        else:
            if self._queue1:
                while self._queue1:
                    self._queue2.append(self._queue1.pop())
                return self._queue2.pop()
            else:
                return None
    
    def getQueue(self):
        print('_queue2:', self._queue2)