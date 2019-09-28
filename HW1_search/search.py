from search_data_structures import Mansion, Room, MansionSearchGraph, Queue, Stack, PriorityQueue
from search_visualization import plotMansionGraph
import math

# initialize mansion, start room, goal room
mansion = Mansion(100, 100)
start = Room(0, 0, True)
goal = Room(99, 99, True)

# two closed room scenarios
closed_rooms1 = []
for i in range(50,76):
    closed_rooms1.append(Room(75, i, False))
    closed_rooms1.append(Room(i, 75, False))
    
closed_rooms2 = []
for i in range(0,99):
    closed_rooms2.append(Room(i, 30, False))
for i in range(1,100):
    closed_rooms2.append(Room(i, 60, False))

# straight-line distance heuristic function
def heuristic(n, goal):
    return math.sqrt( (goal.x - n.state.x)**2 + (goal.y - n.state.y)**2 )

# goal test
def isGoal(n, goal):
    return (n.state.x == goal.x) and (n.state.y == goal.y)

# compute one iteration of given search algorithms
# input: alg, a string representing the algorithm to run
#        search_structure, the data structure used to search (Queue, Stack, PriorityQueue)
#        mansion_graph, a MansionSearchGraph data structure
#        goal, a Room data structure representing the goal
#        nodes_expanded, a count of the number of nodes expanded
# output: result of search iteration
#         updated search_structure
#         updated mansion_graph
#         number of rooms searched after iteration
def iterateSearch(alg, search_structure, mansion_graph, goal, nodes_expanded):
    if alg == 'breadth-first':
        ############################################
        ### TODO: IMPLEMENT BREADTH-FIRST SEARCH ###
        ############################################
        
        # check for failure
        # get node out of search_structure
        # check for goal
        # explore node
        # look at neighbors
        # update search_structure

        if search_structure.isEmpty == True:
            return "FAILURE!", search_structure, mansion_graph, nodes_expanded
        else:
            expand_node = search_structure.dequeue()
            nodes_expanded = nodes_expanded + 1

            if isGoal(expand_node, goal):
                return 'SUCCESS!', search_structure, mansion_graph, nodes_expanded

            expand_node.explored = True

            neighbors = mansion_graph.getNeighbors(expand_node)

            for neighbor in neighbors:
                if neighbor.explored == False and neighbor.queued == False:
                    neighbor.parent = expand_node
                    neighbor.cost = expand_node.cost + 1
                    neighbor.queued = True

                    search_structure.enqueue(neighbor)

        return 'iterating', search_structure, mansion_graph, nodes_expanded
    
    elif alg == 'depth-first':
        ##########################################
        ### TODO: IMPLEMENT DEPTH-FIRST SEARCH ###
        ##########################################
        
        # check for failure
        # get node out of search_structure
        # check for goal
        # explore node
        # look at neighbors
        # update search_structure

        if search_structure.isEmpty == True:
            return "FAILURE!", search_structure, mansion_graph, nodes_expanded
        else:
            expand_node = search_structure.pop()
            nodes_expanded = nodes_expanded + 1

            if isGoal(expand_node, goal):
                return 'SUCCESS!', search_structure, mansion_graph, nodes_expanded

            expand_node.explored = True

            neighbors = mansion_graph.getNeighbors(expand_node)

            for neighbor in neighbors:

                if neighbor.explored == False and neighbor.queued == False:
                    neighbor.parent = expand_node
                    neighbor.cost = expand_node.cost + 1
                    neighbor.queued = True

                    search_structure.push(neighbor)
        
        return 'iterating', search_structure, mansion_graph, nodes_expanded
    
    elif alg == 'uniform-cost':
        ###########################################
        ### TODO: IMPLEMENT UNIFORM-COST SEARCH ###
        ###########################################
        
        # check for failure
        # get node out of search_structure
        # check for goal
        # explore node
        # look at neighbors
        # update search_structure

        if search_structure.isEmpty == True:
            return "FAILURE!", search_structure, mansion_graph, nodes_expanded
        else:
            expand_node = search_structure.extract()
            nodes_expanded = nodes_expanded + 1

            if isGoal(expand_node, goal):
                return 'SUCCESS!', search_structure, mansion_graph, nodes_expanded

            expand_node.explored = True

            neighbors = mansion_graph.getNeighbors(expand_node)

            for neighbor in neighbors:
                cost_through_expand_node = expand_node.cost + 1

                if neighbor.explored == False and neighbor.queued == False:
                    neighbor.parent = expand_node
                    neighbor.cost = cost_through_expand_node
                    neighbor.priority = neighbor.cost
                    neighbor.queued = True

                    search_structure.insert(neighbor)

                elif neighbor.explored == False and neighbor.queued == True:
                    if neighbor.cost > cost_through_expand_node:
                        neighbor.parent = expand_node
                        neighbor.cost = cost_through_expand_node
                        neighbor.priority = neighbor.cost

                        search_structure.insert(neighbor)

        return 'iterating', search_structure, mansion_graph, nodes_expanded
    
    elif alg == 'greedy':
        ################################################
        ### TODO: IMPLEMENT GREEDY BEST-FIRST SEARCH ###
        ################################################
        
        # check for failure
        # get node out of search_structure
        # check for goal
        # explore node
        # look at neighbors
        # update search_structure
        
        if search_structure.isEmpty == True:
            return "FAILURE!", search_structure, mansion_graph, nodes_expanded
        else:
            expand_node = search_structure.extract()
            nodes_expanded = nodes_expanded + 1

            if isGoal(expand_node, goal):
                return 'SUCCESS!', search_structure, mansion_graph, nodes_expanded

            expand_node.explored = True

            neighbors = mansion_graph.getNeighbors(expand_node)

            for neighbor in neighbors:
                cost_through_expand_node = expand_node.cost + 1

                if neighbor.explored == False and neighbor.queued == False:
                    neighbor.parent = expand_node
                    neighbor.cost = cost_through_expand_node
                    neighbor.priority = heuristic(neighbor, goal)
                    neighbor.queued = True

                    search_structure.insert(neighbor)

                elif neighbor.explored == False and neighbor.queued == True:
                    if neighbor.cost > cost_through_expand_node:
                        neighbor.parent = expand_node
                        neighbor.cost = cost_through_expand_node
                        neighbor.priority = heuristic(neighbor, goal)

                        search_structure.insert(neighbor)

        return 'iterating', search_structure, mansion_graph, nodes_expanded
    
    elif alg == 'A*':
        #################################
        ### TODO: IMPLEMENT A* SEARCH ###
        #################################
        
        # check for failure
        # get node out of search_structure
        # check for goal
        # explore node
        # look at neighbors
        # update search_structure
        
        if search_structure.isEmpty == True:
            return "FAILURE!", search_structure, mansion_graph, nodes_expanded
        else:
            expand_node = search_structure.extract()
            nodes_expanded = nodes_expanded + 1

            if isGoal(expand_node, goal):
                return 'SUCCESS!', search_structure, mansion_graph, nodes_expanded

            expand_node.explored = True

            neighbors = mansion_graph.getNeighbors(expand_node)

            for neighbor in neighbors:
                cost_through_expand_node = expand_node.cost + 1

                if neighbor.explored == False and neighbor.queued == False:
                    neighbor.parent = expand_node
                    neighbor.cost = cost_through_expand_node
                    neighbor.priority = neighbor.cost + heuristic(neighbor, goal)
                    neighbor.queued = True

                    search_structure.insert(neighbor)

                elif neighbor.explored == False and neighbor.queued == True:
                    if neighbor.cost > cost_through_expand_node:
                        neighbor.parent = expand_node
                        neighbor.cost = cost_through_expand_node
                        neighbor.priority = neighbor.cost + heuristic(neighbor, goal)

                        search_structure.insert(neighbor)

        return 'iterating', search_structure, mansion_graph, nodes_expanded
    
    else:
        return 'invalid algorithm', search_structure, mansion_graph, nodes_expanded

# main function for searching
# input: alg, a string representing the algorithm to run
#        mansion, a Mansion data structure
#        goal, a Room data structure representing the goal
#        close_rooms, a list of rooms to close
#           for assignment, will either be [], room_close1, room_close2
# output: result of search
#         plot of path returned by solution
#         number of rooms searched
#         distance travelled by solution
def search(alg, mansion, goal, close_rooms):
    # initialize variables for rooms searched
    nodes_expanded = 0
    
    # initialize result
    res = "iterating"
    
    # close rooms
    mansion.closeRooms(close_rooms)
    
    # initialize search graph
    mansion_graph = MansionSearchGraph(mansion)
    
    # initialize data structure
    search_structure = []
    if alg == 'breadth-first':
        #'WHOOPS!'
        ##############################################
        ### TODO: INITIALIZE PROPER DATA STRUCTURE ###
        ##############################################

        search_structure = Queue()

        mansion_graph.nodes[start.x][start.y].cost = 0
        mansion_graph.nodes[start.x][start.y].queued = True

        search_structure.enqueue(mansion_graph.nodes[start.x][start.y])

    elif alg == 'depth-first':
        #'WHOOPS!'
        ##############################################
        ### TODO: INITIALIZE PROPER DATA STRUCTURE ###
        ##############################################

        search_structure = Stack()

        mansion_graph.nodes[start.x][start.y].cost = 0
        mansion_graph.nodes[start.x][start.y].queued = True

        search_structure.push(mansion_graph.nodes[start.x][start.y])

    elif alg == 'uniform-cost':
        #'WHOOPS!'
        ##############################################
        ### TODO: INITIALIZE PROPER DATA STRUCTURE ###
        ##############################################

        search_structure = PriorityQueue()

        mansion_graph.nodes[start.x][start.y].cost = 0.0
        mansion_graph.nodes[start.x][start.y].priority = mansion_graph.nodes[start.x][start.y].cost
        mansion_graph.nodes[start.x][start.y].queued = True

        search_structure.insert(mansion_graph.nodes[start.x][start.y])

    elif alg == 'greedy':
        #'WHOOPS!'
        ##############################################
        ### TODO: INITIALIZE PROPER DATA STRUCTURE ###
        ##############################################

        search_structure = PriorityQueue()

        mansion_graph.nodes[start.x][start.y].cost = 0.0
        mansion_graph.nodes[start.x][start.y].priority = heuristic(mansion_graph.nodes[start.x][start.y], goal)
        mansion_graph.nodes[start.x][start.y].queued = True

        search_structure.insert(mansion_graph.nodes[start.x][start.y])

    elif alg == 'A*':
        #'WHOOPS!'
        ##############################################
        ### TODO: INITIALIZE PROPER DATA STRUCTURE ###
        ##############################################

        search_structure = PriorityQueue()

        mansion_graph.nodes[start.x][start.y].cost = 0.0
        mansion_graph.nodes[start.x][start.y].priority = mansion_graph.nodes[start.x][start.y].cost + heuristic(mansion_graph.nodes[start.x][start.y], goal)
        mansion_graph.nodes[start.x][start.y].queued = True

        search_structure.insert(mansion_graph.nodes[start.x][start.y])

    else:
        return 'invalid algorithm'
    
    # iterate through algorithm
    while res == "iterating":
        [res, search_structure, mansion_graph, nodes_expanded] = iterateSearch(alg, search_structure, mansion_graph, goal, nodes_expanded)
      
    # handle result
    if res == "SUCCESS!":
        # compute distance travelled
        dist = mansion_graph.get(goal.x, goal.y).cost
        
        # plot
        plotMansionGraph(mansion_graph, mansion_graph.get(goal.x, goal.y))
        print(alg + " search algorithm expanded " + str(nodes_expanded) + " nodes and found a path of distance " + str(dist))
        return res, nodes_expanded, dist
    else:
        for x in range(5):
            for y in range(5):
                print(mansion_graph.nodes[x][y].queued)

        print(alg + "search algorithm failed")
        return res

test_algo = 'A*'
test_mansion = Mansion(5, 5)
test_goal = Room(4, 4, True)
test_closed_room = []

search(test_algo, test_mansion, test_goal, test_closed_room)