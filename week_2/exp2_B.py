import heapq
from math import gcd

def water_jug_a_star(cap_x, cap_y, goal):
    if goal > max(cap_x, cap_y) or goal % gcd(cap_x, cap_y) != 0:
        return None

    start = (0, 0)

    def heuristic(x, y):
        return min(abs(x - goal), abs(y - goal))

    def neighbors(x, y):
        return {
            (cap_x, y),          # Fill X
            (x, cap_y),          # Fill Y
            (0, y),              # Empty X
            (x, 0),              # Empty Y
            (x - min(x, cap_y - y), y + min(x, cap_y - y)),  # Pour X → Y
            (x + min(y, cap_x - x), y - min(y, cap_x - x))   # Pour Y → X
        }

    pq = []
    heapq.heappush(pq, (heuristic(0, 0), 0, start))
    visited = set()
    parent = {}

    while pq:
        _, cost, state = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        x, y = state
        if x == goal or y == goal:
            path = []
            while state in parent:
                path.append(state)
                state = parent[state]
            path.append(start)
            return path[::-1]

        for nxt in neighbors(x, y):
            if nxt not in visited:
                parent[nxt] = state
                heapq.heappush(
                    pq, (cost + 1 + heuristic(*nxt), cost + 1, nxt)
                )

    return None


# Space Station Water Measurement Problem
cap_x = 7   # 7 litre container
cap_y = 4   # 4 litre container
goal = 6    # Required water

solution = water_jug_a_star(cap_x, cap_y, goal)

if solution:
    print("Steps to measure exactly 6 litres of water:\n")
    for i, (x, y) in enumerate(solution):
        print(f"Step {i}: Container X = {x} L, Container Y = {y} L")

    print("\n Exactly 6 litres obtained successfully.")
else:
    print(" It is not possible to measure exactly 6 litres.")
