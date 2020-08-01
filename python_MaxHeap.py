#Python maxHeap
#public functions: push(insert), peek(max value in heap), pop(remove max value)
#private functions: __swap, __floatUp, __boubleDown
#__boubleDown = maxhipyfy

class MaxHeap:
    def __init__(self, items= []):
        super().__init__
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            #cim ubacimo nov element u listu self.heap penjemo ga gore na pravu poziciju
            self.__floatUp(len(self.heap)-1)
    
    def push(self, number):
        self.heap.append(number)
        self.__floatUp(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def popMax(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max_value = self.heap.pop()
            self.__boubleDown(1)
            return max_value
        elif len(self.heap) == 2:
            max_value = self.heap.pop()
            return max_value
        else:
            return False
    
    def __swap(self, num1, num2):
        self.heap[num1], self.heap[num2] = self.heap[num2], self.heap[num1]
    
    def __floatUp(self, num):
        child = num
        parent = num//2
        if num < 2:
            return
        elif self.heap[child] > self.heap[parent]:
            self.__swap(child, parent)
            child = parent
            self.__floatUp(child)
    
    def __boubleDown(self, index):
        left_child = index*2
        right_child = index*2 + 1
        largest = index
        if len(self.heap) > left_child and self.heap[largest] < self.heap[left_child]:
            largest = left_child
        elif len(self.heap) > right_child and self.heap[largest] < self.heap[right_child]:
            largest = right_child
        if largest != index:
            self.__swap(index, largest)
            self.__boubleDown(largest)

#test
m = MaxHeap([95,3,21,100,3540])
print(m.heap)
print(m.popMax())
print(m.heap)