# In a MaxHeap

# Parent floor((idx-1)/2)
# left (idx*2)+1
#right (idx*2)+2

import math
class priority_queue:
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def is_empty(self):
        return len(self.heap)==0
    
    def parent(self,idx):
        if idx ==0:
            return 0
        return math.floor((idx-1)/2)

    def left_child(self,idx):
        return idx*2+1

    def right_child(self,idx):
        return idx*2+2

    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    
    def compare(self,i,j):
        print(i,j)
        if self.heap[i] > self.heap[j]:
            return True
        else:
            return False
    def shift_down(self):
        index =0
        while (self.left_child(index)<self.size() and self.compare(self.left_child(index),index)) or(self.right_child(index)<self.size() and self.compare(self.right_child(index),index)):
            if self.left_child(index) < self.size() and self.compare(self.left_child(index), self.right_child(index)):
                greaterChild =  self.left_child(index)
            else:
                greaterChild = self.right_child(index)
            self.swap(greaterChild,index)
            index = greaterChild        
    def pop(self):
        if self.size()>1:
            self.swap(0,len(self.heap)-1)
        popped_value = self.heap.pop()
        self.shift_down()
        print(self.heap)
        return popped_value    
    def shift_up(self):
        node_idx = len(self.heap) -1
        parent_idx  =self.parent(node_idx)
        while 0<node_idx and self.compare(node_idx,parent_idx):
            self.swap(node_idx,self.parent(node_idx))
            node_idx = self.parent(node_idx)    

    def push(self,element):
        self.heap.append(element)
        self.shift_up()
        return self.size()

pq  = priority_queue()
pq.push(15);
pq.push(12);
pq.push(50);
pq.push(7);
pq.push(40);
pq.push(22);
pq.pop()
pq.pop()