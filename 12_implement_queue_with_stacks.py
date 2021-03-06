class MyQueue:
	def __init__(self):
		self.inStack = []
		self.outStack = []

	def enqueue(self,x):
		self.inStack.append(x)

	def dequeue(self):
		if len(self.outStack) != 0:
			while len(self.inStack) >0 :
				self.outStack.append(self.inStack.pop())
		return self.outStack.pop();

	def peek():
		if len(self.outStack) != 0:
			while len(self.inStack) >0 :
				self.outStack.append(self.inStack.pop())
		return self.outStack[-1]	
	def empty():
		return len(self.inStack) == 0 and len(self.outStack) ==0		