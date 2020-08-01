#Python maxHeap
#public functions: push(insert), peek(max value in heap), pop(remove max value)
#private functions: __swap, __floatUp, __boubleDown
#__boubleDown = minhipyfy

class MinHeap:
    def __init__(self, items= []):
        super().__init__ 
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            #cim ubacimo u self.heap penjemo ga gore u pravu poziciju
            self.__floatUp(len(self.heap)-1)
    
    def push(self, number):
        self.heap.append(number)
        self.__floatUp(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def popMin(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            min_value = self.heap.pop()
            self.__boubleDown(1)
            return min_value
        elif len(self.heap) == 2:
            min_value = self.heap.pop()
            return min_value
        else:
            return False
    
    def __swap(self, num1, num2):
        self.heap[num1], self.heap[num2] = self.heap[num2], self.heap[num1]
    
    def __floatUp(self, num):
        child = num
        parent = num//2
        if num < 2:
            return
        elif self.heap[child] < self.heap[parent]:
            self.__swap(child, parent)
            child = parent
            self.__floatUp(child)
    
    def __boubleDown(self, index):
        left_child = index*2
        right_child = index*2 + 1
        smallest = index
        if len(self.heap) > left_child and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        elif len(self.heap) > right_child and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if smallest != index:
            self.__swap(index, smallest)
            self.__boubleDown(smallest)

#testing
m = MinHeap([95,3,21,100,3540])
print(m.heap)
print(m.popMin())
print(m.heap)