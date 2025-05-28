class Node:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def __lt__(self, other):
        return self.amount > other.amount 

    def __repr__(self):
        return f"(ID={self.transaction_id}, сума={self.amount})"

class PaymentSystem:
    def __init__(self):
        self.heap = []
        self.transaction_ids = set()
        self.amounts = set()

    def add(self, transaction_id, amount):
        if transaction_id in self.transaction_ids:
            print("ID вже існує")
            return
        if amount in self.amounts:
            print("Сума вже існує")
            return

        node = Node(transaction_id, amount)
        self.heap.append(node)
        self.transaction_ids.add(transaction_id)
        self.amounts.add(amount)
        self._up(len(self.heap) - 1)
        print(f"Додано:{node}")
        print(f"Купа:{self.heap}")

    def remove(self):
        if not self.heap:
            print("Черга порожня")
            return

        if len(self.heap) == 1:
            removed = self.heap.pop()
        else:
            removed = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._down(0)

        self.transaction_ids.remove(removed.transaction_id)
        self.amounts.remove(removed.amount)
        print(f"Видалено: {removed}")
        return removed

    def find_by_amount(self, amount):
        for node in self.heap:
            if node.amount == amount:
                print(f"Знайдено: {node}")
                return node
        print("Переказ з такою сумою не знайдено")
        return None

    def view(self):
        print("Усі перекази:")
        for node in self.heap:
            print(node)

    def view_sorted(self):
        if not self.heap:
            print("Список переказів порожній")
            return

        max_amount = max(node.amount for node in self.heap)
        min_amount = min(node.amount for node in self.heap)

        size = max_amount - min_amount + 1
        count = [[] for _ in range(size)]

        for node in self.heap:
            count[node.amount - min_amount].append(node)

        print("Сортування від меншого до більшого:")
        for sublist in count:
            for node in sublist:
                print(node)

    def _up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._up(parent_index)

    def _down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._down(largest)


system = PaymentSystem()
print("add (ID sum)| remove | find (sum) | view | sorted | exit")
while True:
    command = input("").strip().split()
    if not command:
        continue
    if command[0] == "add" and len(command) == 3:
        system.add(command[1], int(command[2]))
    elif command[0] == "remove":
        system.remove()
    elif command[0] == "find" and len(command) == 2:
        system.find_by_amount(int(command[1]))
    elif command[0] == "view":
        system.view()
    elif command[0] == "sorted":
        system.view_sorted()
    elif command[0] == "exit":
        print("Завершення роботи")
        break
    else:
        print("Невідома команда")