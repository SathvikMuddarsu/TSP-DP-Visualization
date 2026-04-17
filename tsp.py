import math
import time
import matplotlib.pyplot as plt

def calculate_distance(p1, p2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp(cities):
    n = len(cities)
    # distance_matrix[i][j] stores distance between city i and city j
    dist_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

    # Memoization table: memo[(mask, last_city)] = min_distance
    # mask: bitmask representing the set of visited cities
    memo = {}

    # parent table to reconstruct the path
    parent = {}

    def tsp(mask, pos):
        # Base case: if all cities are visited, return to the start (city 0)
        if mask == (1 << n) - 1:
            return dist_matrix[pos][0]

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        res = float('inf')
        best_next_city = -1

        # Try visiting every city that hasn't been visited yet
        for next_city in range(n):
            if (mask >> next_city) & 1 == 0:  # If city not visited
                new_dist = dist_matrix[pos][next_city] + tsp(mask | (1 << next_city), next_city)
                if new_dist < res:
                    res = new_dist
                    best_next_city = next_city

        memo[(mask, pos)] = res
        parent[(mask, pos)] = best_next_city
        return res

    # Start the recursion from city 0
    min_cost = tsp(1, 0)

    # Reconstruct the optimal path
    path = []
    curr_mask = 1
    curr_pos = 0
    while True:
        path.append(curr_pos)
        next_city = parent.get((curr_mask, curr_pos))
        if next_city is None:
            break
        curr_mask |= (1 << next_city)
        curr_pos = next_city
    
    path.append(0)  # Return to start
    return min_cost, path

def visualize_tsp(cities, path, min_dist):
    """Visualizes the cities and the optimal tour using matplotlib."""
    x = [c[0] for c in cities]
    y = [c[1] for c in cities]

    plt.figure(figsize=(10, 7))
    
    # Plot cities
    plt.scatter(x, y, color='blue', zorder=2)
    
    # Label cities
    for i, (xi, yi) in enumerate(cities):
        plt.text(xi + 0.1, yi + 0.1, f"City {i}", fontsize=12)

    # Highlight starting city
    plt.scatter(cities[0][0], cities[0][1], color='green', s=150, label='Start (City 0)', zorder=3)

    # Draw the path with arrows
    for i in range(len(path) - 1):
        start_node = cities[path[i]]
        end_node = cities[path[i+1]]
        
        plt.annotate("", 
                     xy=(end_node[0], end_node[1]), 
                     xytext=(start_node[0], start_node[1]),
                     arrowprops=dict(arrowstyle="->", color="red", lw=2, mutation_scale=20))

    plt.title(f"TSP Solution using Dynamic Programming\nTotal Distance: {min_dist:.2f}", fontsize=14)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def main():
    print("--- Traveling Salesman Problem Solver (Held-Karp) ---")
    
    try:
        n = int(input("Enter the number of cities: "))
        if n < 2:
            print("You need at least 2 cities.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    cities = []
    for i in range(n):
        while True:
            try:
                coords = input(f"Enter coordinates for city {i} (x y): ").split()
                x, y = float(coords[0]), float(coords[1])
                cities.append((x, y))
                break
            except (ValueError, IndexError):
                print("Invalid format. Please enter two numbers separated by a space.")

    print("\nCalculating optimal path...")
    
    start_time = time.time()
    min_dist, path = solve_tsp(cities)
    end_time = time.time()

    print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
    print(f"Minimum Distance: {min_dist:.4f}")
    print(f"Optimal Path: {' -> '.join(map(str, path))}")

    visualize_tsp(cities, path, min_dist)

if __name__ == "__main__":
    main()