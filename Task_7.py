class Queue:
    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.front = 0
        self.back = 0
        self.capacity = capacity

    def add(self, item):
        if self.internalArray[self.back] is not None:
            print("Queue is full")
        else:
            self.internalArray[self.back] = item
            self.back = self.back + 1
            if self.back == self.capacity:
                self.back = 0
            print(f"Added {item} to queue")
        pass

    def remove(self):
        if self.internalArray[self.front] is not None:
            removed = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front = self.front + 1
            if self.front == self.capacity:
                self.front = 0
            return print(f"{removed} has been removed from the queue")
        else:
            return print("Queue is empty")
        pass

    def __str__(self):
        return self.internalArray.__str__()


def run_task7a(queries):
    print("What is your query?")
    new_query = str(input()).capitalize()
    queries.add(new_query)


def run_task7b(queries):
    queries.remove()
