from copy import deepcopy


GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


MOVES = [
    (-1, 0, "Up"),
    (1, 0, "Down"),
    (0, -1, "Left"),
    (0, 1, "Right")
]


def print_puzzle(state):
    for row in state:
        print(row)
    print()


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []

    for dx, dy, move in MOVES:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)

          
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append((new_state, move))

    return neighbors


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)




def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        state_key = state_to_tuple(state)

        if state_key in visited:
            continue

        visited.add(state_key)

        if state == GOAL:
            return path

        for new_state, move in reversed(get_neighbors(state)):
            stack.append((new_state, path + [move]))

    return None




def depth_limited_search(state, depth, path, visited):

    if state == GOAL:
        return path

    if depth == 0:
        return None

    state_key = state_to_tuple(state)
    visited.add(state_key)

    for new_state, move in get_neighbors(state):

        new_key = state_to_tuple(new_state)

        if new_key not in visited:
            result = depth_limited_search(
                new_state,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

    visited.remove(state_key)

    return None


def ids(start, max_depth=30):

    for depth in range(max_depth + 1):

        visited = set()

        result = depth_limited_search(
            start,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

    return None




start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Initial State:")
print_puzzle(start)


dfs_solution = dfs(start)

print("DFS Solution:")
if dfs_solution:
    print(" -> ".join(dfs_solution))
    print("Number of moves:", len(dfs_solution))
else:
    print("No solution found")



ids_solution = ids(start)

print("\nIDS Solution:")
if ids_solution:
    print(" -> ".join(ids_solution))
    print("Number of moves:", len(ids_solution))
else:
    print("No solution found")
