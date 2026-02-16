class Queue:
    def __init__(self):
        self.queue=[]
    def addqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        return self.queue.pop(0)
    def isempty(self):
        return len(self.queue)==0                    
    def length(self):
        return len(self.queue)
    def display(self):
        print("Queue is ->",self.queue) 

myQueue=Queue()
myQueue.addqueue("A")
myQueue.addqueue("B")
myQueue.addqueue("C")
myQueue.display()
myQueue.dequeue()

print(myQueue.isempty())
print(myQueue.length())

