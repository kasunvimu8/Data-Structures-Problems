import math
# Tree Based Data Structure
# complete binary tree
# parent should be greater or equal than it's children (Min Heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    # swap the two elements
    def __swap(self, first_index, second_index):
        self.heap[first_index], self.heap[second_index] = self.heap[second_index], self.heap[first_index]

    # return the height of the heap
    def heap_height(self):
        return math.ceil(math.log2(len(self.heap)))

    # return parent index
    def parent_index(self, child_index):
        return child_index // 2

    # return left child index
    def left_child_index(self, p):
        return 2*p + 1

    # return right child index
    def right_child_index(self, p):
        return 2*p + 2

    def is_leaf(self, i):
        return self.left_child_index(i) + 1 > len(self.heap)

    def heapify(self, i):
        left_child_index = self.left_child_index(i)
        right_child_index = self.right_child_index(i)
        parent = self.heap[i]

        if not self.is_leaf(i):
            if parent < self.heap[left_child_index] or (right_child_index + 1 < len(self.heap) and parent < self.heap[right_child_index]):
                if parent < self.heap[left_child_index]:
                    self.__swap(i, left_child_index)
                    self.heapify(left_child_index)
                else:
                    self.__swap(i, right_child_index)
                    self.heapify(right_child_index)

    def max_heapify(self):
        h = self.heap_height()

        for i in range(h-1, -1, -1):
            self.heapify(i)

    def insert(self, item):
        self.heap.append(item)
        current = len(self.heap) - 1

        while self.heap[current] > self.heap[self.parent_index(current)]:
            self.__swap(current, self.parent_index(current))
            current = self.parent_index(current)

    def remove(self):
        self.__swap(0, len(self.heap)-1)
        min = self.heap.pop()
        self.max_heapify()
        return min

    def peek(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)

    # Print the Heap Left and Right Elements
    def print(self):
        for i in range(0, (len(self.heap) // 2)):
            right_child = 'NO CHILD'
            if self.right_child_index(i) < len(self.heap):
                right_child = str(self.heap[2*i + 2])

            print("PARENT :" + str(self.heap[i]) + "   LEFT CHILD   ",
                  str(self.heap[2*i + 1]), "  RIGHT CHILD " + right_child)
