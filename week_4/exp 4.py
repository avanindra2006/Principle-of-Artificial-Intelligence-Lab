# Function to check if it is safe to assign color
def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
# Backtracking function
def map_coloring(graph, colors, assignment, nodes):
    if len(assignment) == len(nodes):
        return assignment
    node = nodes[len(assignment)]
    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = map_coloring(graph, colors, assignment, nodes)
            if result:
                return result
            del assignment[node]  # backtrack
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'yellow']
nodes = list(graph.keys())

solution = map_coloring(graph, colors, {}, nodes)

if solution:
    print("graph Color Assignment:")
    for region in solution:
        print(region, "->", solution[region])
else:
    print("No solution found")