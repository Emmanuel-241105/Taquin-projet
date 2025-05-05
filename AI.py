import heapq

# 🧮 Test de solubilité (pour grille 4x4)
def is_solvable(grid):
    flat = [num for row in grid for num in row]

    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] != 0 and flat[j] != 0 and flat[i] > flat[j]:
                inversions += 1

    zero_index = flat.index(0)
    zero_row_from_bottom = 4 - (zero_index // 4)

    # Règle pour 4x4 : (inversions + ligne du bas) doit être pair
    return (inversions + zero_row_from_bottom) % 2 == 0, flat

# 🧠 Heuristique : Distance de Manhattan
def manhattan(state, goal, size):
    distance = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        goal_idx = goal.index(val)
        x1, y1 = i % size, i // size
        x2, y2 = goal_idx % size, goal_idx // size
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# 🔁 Génération des voisins
def get_neighbors(state, size):
    neighbors = []
    zero_index = state.index(0)
    x, y = zero_index % size, zero_index // size

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # gauche, droite, haut, bas

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            new_index = ny * size + nx
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors

# ⭐ Algorithme A*
def a_star(start, goal, size):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal, size), 0, start, []))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current, size):
            if neighbor not in visited:
                heapq.heappush(open_set, (
                    g + 1 + manhattan(neighbor, goal, size),
                    g + 1,
                    neighbor,
                    path + [current]
                ))
    return None

# 🎯 Exemple d'utilisation
if __name__ == "__main__":
    grid = [
    [15, 2, 7, 4],
    [3, 14, 9, 11],
    [8, 1, 13, 12],
    [10, 5, 6, 0]
]

    solvable, flat = is_solvable(grid)
    start = tuple(flat)
    goal = tuple(range(1, 16)) + (0,)

    print("Configuration initiale :", flat)
    print("Soluble :", solvable)

    if not solvable:
        print("Ce taquin est insoluble.")
    else:
        solution = a_star(start, goal, 4)
        if solution:
            print(f"Résolu en {len(solution)-1} coups.")
            for step in solution:
                for i in range(0, 16, 4):
                    print(step[i:i+4])
                print("------")
        else:
            print("Aucune solution trouvée (erreur algo A*).")

