import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0
    
    #insert a new item into the priority queue
    def put(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1

    #remove and return the item with the lowest priority from the queue
    def get(self):
        if len(self.queue) < 1:
            return None
        return heapq.heappop(self.queue)[-1]
    
    #check if the queue is empty
    def empty(self):
        return len(self.queue) < 1
    
if __name__ == "__main__":
    queue = PriorityQueue()
    queue.put((1, 2), 1)
    queue.put((3, 4), 3)
    queue.put((2, 3), 2)
    print(queue.get())
    print(queue.get())
    print(queue.empty())
    print(queue.get())
    print(queue.empty())