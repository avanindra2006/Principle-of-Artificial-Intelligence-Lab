import heapq
from math import gcd

def water_jug_a_star(cap_a, cap_b, goal):
    # Feasibility check
    if goal > max(cap_a, cap_b) or goal % gcd(cap_a, cap_b) != 0:
        return None

    start = (0, 0)

    def heuristic(x, y):
        return min(
            abs(x - goal),
            abs(y - goal),
            abs((cap_a - x) - goal),
            abs((cap_b - y) - goal)
        )

    def neighbors(x, y):
        states = []

        # Fill
        states.append((cap_a, y))
        states.append((x, cap_b))

        # Empty
        states.append((0, y))
        states.append((x, 0))

        # Pour A → B
        pour = min(x, cap_b - y)
        states.append((x - pour, y + pour))

        # Pour B → A
        pour = min(y, cap_a - x)
        states.append((x + pour, y - pour))

        return states

    pq = []
    heapq.heappush(pq, (heuristic(0, 0), 0, start))
    visited = set()
    parent = {}

    while pq:
        _, cost, (x, y) = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == goal or y == goal:
            path = []
            cur = (x, y)
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            path.append(start)
            return path[::-1]

        for nx, ny in neighbors(x, y):
            if (nx, ny) not in visited:
                parent[(nx, ny)] = (x, y)
                heapq.heappush(
                    pq,
                    (cost + 1 + heuristic(nx, ny), cost + 1, (nx, ny))
                )

    return None
solution = water_jug_a_star(cap_a=4, cap_b=3, goal=2)

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
