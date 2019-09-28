import math

# mansion class
class Mansion:
    # constructor: creates grid of rooms
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.rooms = []
        for i in range(self.x_size):
            self.rooms.append([])
            for j in range(self.y_size):
                r = Room(i, j, True)
                self.rooms[i].append(r)
    
    # accesses individual rooms
    def get(self, i, j):
        return self.rooms[i][j]
    
    # close rooms in mansion
    def closeRooms(self, close_rooms):
        for i in range(self.x_size):
            for j in range(self.y_size):
                self.rooms[i][j].room_open = True
        for room in close_rooms:
            self.rooms[room.x][room.y].room_open = False

# room class
class Room:
    # constructor: creates room with x,y location in a mansion and boolean indicating if room is open
    def __init__(self, x, y, room_open):
        self.x = x
        self.y = y
        self.room_open = room_open

# mansion search graph class
class MansionSearchGraph:
    # constructor: creates grid of nodes
    def __init__(self, mansion):
        self.x_size = mansion.x_size
        self.y_size = mansion.y_size
        self.nodes = []
        for i in range(self.x_size):
            self.nodes.append([])
            for j in range(self.y_size):
                n = Node(mansion.get(i, j), -1, math.inf, math.inf, False, False)
                self.nodes[i].append(n)
    
    # accesses individual nodes
    def get(self, i, j):
        return self.nodes[i][j]
    
    # neighbors added in left, down, right, up order
    def getNeighbors(self, n):
        neighbors = []
        i = n.state.x
        j = n.state.y
        # get left neighbor
        if i != 0:
            neighbors.append(self.nodes[i-1][j])
        # get down neighbor
        if j != 0:
            neighbors.append(self.nodes[i][j-1])
        # get right neighbor
        if i != self.x_size-1:
            neighbors.append(self.nodes[i+1][j])
        # get up neighbor
        if j != self.y_size-1:
            neighbors.append(self.nodes[i][j+1])
        # return list of neighbor nodes
        return neighbors

# node class
class Node:
    # constructor: creates node with room state (x, y, room_open), parent node,
    # boolean indicating if room is open, cost to reach room,
    # booleans indicating if node is explored or queued
    def __init__(self, state, parent, cost, priority, queued, explored):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.priority = priority
        self.queued = queued
        self.explored = explored

# queue class
class Queue:
    # constructor
    def __init__(self):
        self.queue = []
    
    # isEmpty predicate
    def isEmpty(self):
        return len(self.queue) == 0
    
    # adds node to queue
    def enqueue(self, n):
        self.queue.append(n)
    
    # removes and returns node from queue
    def dequeue(self):
        n = self.queue[0]
        self.queue.pop(0)
        return n
      
# stack class
class Stack:
    # constructor
    def __init__(self):
        self.stack = []
    
    # isEmpty predicate
    def isEmpty(self):
        return len(self.stack) == 0
    
    # adds node to stack
    def push(self, n):
        self.stack.append(n)
    
    # removes and returns node from stack
    def pop(self):
        n = self.stack.pop()
        return n
    
# priority queue class
class PriorityQueue:
    # constructor
    def __init__(self):
        self.pqueue = MinHeap()
    
    # isEmpty predicate
    def isEmpty(self):
        return self.pqueue.isEmpty()
    
    # adds node to priority queue
    def insert(self, n):
        self.pqueue.insert(n)
    
    # removes and returns node from priority queue
    def extract(self):
        return self.pqueue.extract()

# minheap class
# used to implement priority queue
class MinHeap:
    # constructor
    def __init__(self):
        self.heap = []
        self.num_els = 0
        
    # isEmpty predicate
    def isEmpty(self):
        return len(self.heap) == 0
    
    # adds node to minheap
    def insert(self, n):
        self.num_els += 1
        n.num_in_pq = self.num_els
        self.heap.append(n)
        curr_idx = len(self.heap)-1
        par_idx = self.parentIdx(curr_idx)
        heaped = False
        # bubble node up
        while not heaped:
            if (self.heap[curr_idx].priority < self.heap[par_idx].priority):
                temp = self.heap[par_idx]
                self.heap[par_idx] = self.heap[curr_idx]
                self.heap[curr_idx] = temp
                curr_idx = par_idx;
                par_idx = self.parentIdx(curr_idx)
            else:
                heaped = True
    
    # removes and returns node from minheap
    def extract(self):
        n = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            # move last node to top
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()
            curr_idx = 0
            lc = self.leftChildIdx(curr_idx)
            rc = self.rightChildIdx(curr_idx)
            heaped = False
            # bubble node down
            while not heaped:
                if (self.heap[curr_idx].priority > self.heap[lc].priority) or (self.heap[curr_idx].priority > self.heap[rc].priority):
                    if self.heap[lc].priority == self.heap[rc].priority:
                        if self.heap[lc].num_in_pq <= self.heap[rc].num_in_pq:
                            swap_idx = lc
                        else:
                            swap_idx = rc
                    elif self.heap[lc].priority < self.heap[rc].priority:
                        swap_idx = lc
                    else:
                        swap_idx = rc
                    temp = self.heap[swap_idx]
                    self.heap[swap_idx] = self.heap[curr_idx]
                    self.heap[curr_idx] = temp
                    curr_idx = swap_idx
                    lc = self.leftChildIdx(curr_idx)
                    rc = self.rightChildIdx(curr_idx)
                elif (self.heap[curr_idx].priority == self.heap[lc].priority) or (self.heap[curr_idx].priority > self.heap[rc].priority):
                    if (self.heap[curr_idx].num_in_pq > self.heap[lc].num_in_pq) or (self.heap[curr_idx].num_in_pq > self.heap[rc].num_in_pq):
                        if self.heap[lc].num_in_pq <= self.heap[rc].num_in_pq:
                            swap_idx = lc
                        else:
                            swap_idx = rc
                        temp = self.heap[swap_idx]
                        self.heap[swap_idx] = self.heap[curr_idx]
                        self.heap[curr_idx] = temp
                        curr_idx = swap_idx
                        lc = self.leftChildIdx(curr_idx)
                        rc = self.rightChildIdx(curr_idx)
                    else:
                        heaped = True
                else:
                    heaped = True
        return n
        
    # helper function: computes the parent index of a node in the minheap
    def parentIdx(self, i):
        if i == 0:
            return 0
        else:
            return math.floor((i-1)/2)
        
    # helper function: computes the left child index of a node in the minheap
    def leftChildIdx(self, i):
        lc = (2*i)+1
        if lc >= len(self.heap):
            return i
        else:
            return lc
    
    # helper function: computes the right child index of a node in the minheap
    def rightChildIdx(self, i):
        rc = (2*i)+2
        if rc >= len(self.heap):
            return i
        else:
            return rc
