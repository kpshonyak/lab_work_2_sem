class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority  

    def __repr__(self):
        return f"({self.value}, p={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        print(f"\nВставка: значення={value}, пріоритет={priority}")
        node = Node(value, priority)
        self.heap.append(node)
        self._up(len(self.heap) - 1)
        print(f"Купа після вставки: {self.heap}")

    def remove(self):
        if not self.heap:
            print("Черга порожня")
            return None
        if len(self.heap) == 1:
            print(f"\nВидалено останній елемент: {self.heap[0]}")
            return self.heap.pop()
                                                                                                                                                                                                                                                
        print(f"\nВидалення вершини: {self.heap[0]}")
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        print(f"Переміщення останнього елемента на вершину: {self.heap[0]}")
        self._down(0)
        print(f"Купа після видалення: {self.heap}")
        return top

    def view(self):
        return [(node.value, node.priority) for node in self.heap]

    def _up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            print(f"Підйом: {self.heap[index]}  {self.heap[parent_index]}")
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._up(parent_index)

    def _down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[largest]:
            print(f"Заміна з лівою дитиною: {self.heap[largest]}  {self.heap[left_child]}")
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[largest]:
            print(f"Заміна з правою дитиною: {self.heap[largest]}  {self.heap[right_child]}")
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._down(largest)

    def __repr__(self):
        return str(self.heap)

q = PriorityQueue()

q.insert("A", 5)
q.insert("B", 9)
q.insert("C", 3)
q.insert("D", 10)
q.insert("E", 7)

q.remove()
q.remove()