from collections import deque
def pour(x, y, cap_y):
    amount = min(x, cap_y - y)
    return x - amount, y + amount
def nib(x, y, z, a, b, c):
    states = [
        (a, y, z), (x, b, z), (x, y, c),
        (0, y, z), (x, 0, z), (x, y, 0)
    ]
    # A → B, A → C
    nx, ny = pour(x, y, b); states.append((nx, ny, z))
    nx, nz = pour(x, z, c); states.append((nx, y, nz))
    # B → A, B → C
    ny, nx = pour(y, x, a); states.append((nx, ny, z))
    ny, nz = pour(y, z, c); states.append((x, ny, nz))
    # C → A, C → B
    nz, nx = pour(z, x, a); states.append((nx, y, nz))
    nz, ny = pour(z, y, b); states.append((x, ny, nz))
    return states
def water_jug_3_bfs(a, b, c, d):
    queue = deque([(0, 0, 0, [(0,0,0)])])
    visited = set()
    while queue:
        x, y, z, path = queue.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if x == d or y == d or z == d:
            return path
        for state in nib(x, y, z, a, b, c):
            queue.append((*state, path + [state]))
    return None
def water_jug_3_dfs(a, b, c, d):
    stack = [(0, 0, 0, [(0,0,0)])]
    visited = set()
    while stack:
        x, y, z, path = stack.pop()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if x == d or y == d or z == d:
            return path
        for state in nib(x, y, z, a, b, c):
            stack.append((*state, path + [state]))
    return None
if __name__ == "__main__":
    a, b, c = 8, 5, 3
    d = 7
    bfs_result = water_jug_3_bfs(a, b, c, d)
    dfs_result = water_jug_3_dfs(a, b, c, d)
    print("=== 3 Water Jug Problem ===")
    print(f"Jug capacities: A={a}, B={b}, C={c}")
    print(f"Target amount: {d}\n")
    print("BFS Solution (Shortest Path):")
    if bfs_result:
        for i, state in enumerate(bfs_result):
            print(f"Step {i}: {state}")
        print(f"Total steps (BFS): {len(bfs_result)-1}")
    else:
        print("No solution found")
    print("\nDFS Solution:")
    if dfs_result:
        for i, state in enumerate(dfs_result):
            print(f"Step {i}: {state}")
        print(f"Total steps (DFS): {len(dfs_result)-1}")
    else:
        print("No solution found")