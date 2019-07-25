class Queue:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def put(self, num):
        self.list1.append(num)

    def get(self):
        self.arrange()
        try:
            return self.list2.pop()
        except:
            raise Exception("Queue Empty!")

    def arrange(self):
        if not self.list2:
            while self.list1:
                self.list2.append(self.list1.pop())


if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    print(q.get(), q.get(), q.get())

