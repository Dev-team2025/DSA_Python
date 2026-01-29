class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        return self.stack.pop()

    def isempty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)

    def display(self):
        print("Stack is ->", self.stack)
myStack = Stack()
myStack.push("Iron Man")
myStack.push("RDJ")
myStack.push("Yash")
myStack.display()

myStack.pop()

print(myStack.isempty())
print(myStack.length())



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


