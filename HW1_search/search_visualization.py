import matplotlib.pyplot as plt

# plot mansion, including rooms, closed rooms, and path travelled
def plotMansionGraph(mansion_graph, goal_node):
    [roomXs, roomYs] = getRooms(mansion_graph)
    [closedXs, closedYs] = getClosedRooms(mansion_graph)
    [pathXs, pathYs] = getTravelledPath(goal_node)
    plt.plot(roomXs, roomYs, 'k.', closedXs, closedYs, 'rs', pathXs, pathYs, 'b.')
    plt.show()

# get the xy locations of all rooms in the mansion
def getRooms(mansion_graph):
    xs = []
    ys = []
    for i in range(mansion_graph.x_size):
        for j in range(mansion_graph.y_size):
            xs.append(mansion_graph.get(i, j).state.x)
            ys.append(mansion_graph.get(i, j).state.y)
    return xs, ys

# get the xy locations of all closed rooms in the mansion
def getClosedRooms(mansion_graph):
    xs = []
    ys = []
    for i in range(mansion_graph.x_size):
        for j in range(mansion_graph.y_size):
            if not mansion_graph.get(i, j).state.room_open:
                xs.append(mansion_graph.get(i, j).state.x)
                ys.append(mansion_graph.get(i, j).state.y)
    return xs, ys

# get the xy locations of all rooms travelled through
def getTravelledPath(goal_node):
    xs = []
    ys = []
    curr_node = goal_node
    while curr_node != -1:
        xs.append(curr_node.state.x)
        ys.append(curr_node.state.y)
        curr_node = curr_node.parent
    return xs, ys
