graph = {
    'H': ['E', 'A'],
    'E': ['F'],
    'A': ['E','B','C'],
    'F': ['A'],
    'C': ['B'],
    'B': ['D'],
    'D': ['G','C'],
    'G': ['B']
}

# Print the the list all veertexs connectiing
def bfs(grap, vertex):
    # Initial empty visited as a list
    vist = []
    # Initial queue with the first value being vertex
    queue = [vertex]
    # Loop until queue empty:
    while len(queue) > 0:
        # Popping out the first vertex
        hold = queue.pop(0)
        vist.append(hold)
        # Check vertex in visited or not,
    #  while len(graph[hold])>0:
     #       v = graph[hold].pop(0)
      #      if not v in vist:
       #         queue.append(v)
           # print (graph[hold].pop(0))
        # If not inside visited  --> append them into queue

        # Traversall all neighbor vertex
        for neighbor in graph[hold]:
            if not neighbor in vist:
                queue.append(neighbor)

    return vist






print(bfs(graph, 'E'))
# A B C ... G  ( except H)
print(bfs (graph, 'H'))
# All vertexs


company = {
    1:  [2, 3, 4],
    2: [ 3],
    3: [5, 6, 7],
    4: [],
    5: [8],
    6:  [4],
    7: [],
    8: []
}



def bfs1(company, id):
    queue = [id]
    visited = set()
    visited.add(id)

    while len(queue) > 0:
        eID = queue.pop(0)
        visited.add(eID)
        for child in company[eID]:
            if child not in visited:
                queue.append(child)


    print(visited)

bfs1(company, 3)