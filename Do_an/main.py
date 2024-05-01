from maze import maze
from algrithms import dfs
from queue import PriorityQueue

if __name__ == '__main__':
    pq = PriorityQueue()

    pq.put((2, 1, "World"))
    pq.put((1, 2, "Hello"))
    pq.put((1, 3, "Foo"))

    print(pq.get())