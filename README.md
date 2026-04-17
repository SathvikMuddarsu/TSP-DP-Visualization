#  Traveling Salesman Problem (TSP) – Dynamic Programming

##  About the Project

This project solves the **Traveling Salesman Problem (TSP)** using a **Dynamic Programming approach (Held-Karp Algorithm)**.

Given a set of cities and their coordinates, the program finds the **shortest possible route** that:

* Visits every city exactly once
* Returns to the starting city

It also **visualizes the path** using matplotlib.

---

##  Features

*  Uses Dynamic Programming (Held-Karp)
*  Takes user input for city coordinates
*  Calculates distance using Euclidean formula
*  Displays the shortest path clearly using graphs
*  Shows execution time

---

##  Requirements

* Python 3.x
* matplotlib

Install dependency:

```bash
pip install matplotlib
```

---

##  How to Run

```bash
python tsp_dp_visualization.py
```

Then:

1. Enter number of cities
2. Enter coordinates for each city

---

##  Output

* Prints the **minimum distance**
* Displays the **optimal path**
* Shows a **graph with cities and shortest route**

---

##  Algorithm Used

* Dynamic Programming (Held-Karp)
* Time Complexity: **O(n² × 2ⁿ)**
* Guarantees the **optimal solution**

---

##  Project Structure

```
TSP-DP-Visualization/
│── tsp_dp_visualization.py
│── README.md
│── requirements.txt
```

---

##  Author

Sathvik Muddarsu
