
# Tree Based Data Structure
# complete binary tree
# parent should be less or equal than it's children (Min Heap)

class MinHeap:
    def __init__(self):
      self.heap = []
    
    # return parent index
    def __parent(self, child_index):
      return child_index // 2
    
    def __swap(self, first_index, second_index):
      self.heap[first_index], self.heap[second_index] = self.heap[second_index], self.heap[first_index]
      
    def min_heapify(self):
      current = len(self.heap) -1
      
    def insert(self, item):
      self.heap.append(item)
      current = len(self.heap) -1
      
      while self.heap[current] < self.heap[self.__parent(current)]:
        self.__swap(current, self.__parent(current))
        current = self.__parent(current)
        
    def remove(self):
      min = self.heap.pop(0)
      self.minHeapify()
      return min
      
    def peek(self):
      return self.heap.pop()

    def size(self):
      return len(self.heap)

    def print(self):
      for i in range(0, (len(self.heap) // 2)):
        print ("PARENT :"+  str(self.heap[i]) + "   LEFT CHILD   ", str(self.heap[2*i +1]), "  RIGHT CHILD "+ str(self.heap[2*i + 2]))
    
    def heap_height(self):
      return
    
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(17)
min_heap.insert(1)
min_heap.insert(84)

min_heap.print()