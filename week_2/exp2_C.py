import heapq
from math import gcd

def fuel_blending_a_star(tank_a_capacity, tank_b_capacity, target_octane):
    # Feasibility check
    if target_octane > max(tank_a_capacity, tank_b_capacity) or \
       target_octane % gcd(tank_a_capacity, tank_b_capacity) != 0:
        return None

    start_state = (0, 0)  # (Fuel in Tank A, Fuel in Tank B)

    def heuristic(a, b):
        return min(abs(a - target_octane), abs(b - target_octane))

    def next_states(a, b):
        return {
            (tank_a_capacity, b),    # Fill Tank A
            (a, tank_b_capacity),    # Fill Tank B
            (0, b),                  # Empty Tank A
            (a, 0),                  # Empty Tank B
            (a - min(a, tank_b_capacity - b),
             b + min(a, tank_b_capacity - b)),  # Transfer A → B
            (a + min(b, tank_a_capacity - a),
             b - min(b, tank_a_capacity - a))   # Transfer B → A
        }

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(0, 0), 0, start_state))

    visited = set()
    parent = {}

    while priority_queue:
        _, cost, state = heapq.heappop(priority_queue)

        if state in visited:
            continue
        visited.add(state)

        a, b = state
        if a == target_octane or b == target_octane:
            path = []
            while state in parent:
                path.append(state)
                state = parent[state]
            path.append(start_state)
            return path[::-1]

        for nxt in next_states(a, b):
            if nxt not in visited:
                parent[nxt] = state
                heapq.heappush(
                    priority_queue,
                    (cost + 1 + heuristic(*nxt), cost + 1, nxt)
                )

    return None

# ----------------------------
# User Input Section
# ----------------------------
print("=== Automated Fuel Blending Optimisation System ===")
try:
    tank_a_capacity = int(input("Enter Tank A capacity (units): "))
    tank_b_capacity = int(input("Enter Tank B capacity (units): "))
    target_octane = int(input("Enter required target octane level (units): "))
except ValueError:
    print("nvalid input. Please enter integer values only.")
    exit()

solution = fuel_blending_a_star(tank_a_capacity, tank_b_capacity, target_octane)

print("\n=== Optimisation Result ===")
if solution:
    for step, (a, b) in enumerate(solution):
        print(f"Step {step}: Tank A = {a} units, Tank B = {b} units")
    print(f"\n Target octane level {target_octane} units achieved successfully!")
else:
    print(f" Target octane level {target_octane} units cannot be achieved with given tanks.")
