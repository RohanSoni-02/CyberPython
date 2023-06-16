# CyberPython

Cyber Python is a new take on the classic Snake game, enhanced with the use of AI techniques, specifically A*, BFS and DFS search. The game simulates a cybernetic snake's journey through a grid-based world, attempting to eat as many apples as possible on the map.

# CyberPython: A star search
It finds the shortest path and grows as it eats the apple. Since it is 15 x 13 grid therefore the maximum score can be 193 (195 – snake’s initial position – apple’s position).

<img width="228" alt="image" src="https://github.com/RohanSoni-02/CyberPython/assets/110955425/d36e60d1-891a-4ff5-b821-1ed7859fac41">
<img width="224" alt="image" src="https://github.com/RohanSoni-02/CyberPython/assets/110955425/cd1f5f4f-132b-498f-8d03-de71f07ea076">
<img width="229" alt="image" src="https://github.com/RohanSoni-02/CyberPython/assets/110955425/eff09856-f83e-443b-9f86-7213420330fb">
<img width="225" alt="image" src="https://github.com/RohanSoni-02/CyberPython/assets/110955425/a8ea5e14-9aa8-43f2-8acc-a2f071acb393">

# CyberPython: Optimised
In the Optimised Cyber Python, the decision to use the A* algorithm (a_path_search.cal) or the Depth-First Search (DFS) algorithm (dfs_path_search.cal) is based on the length of the snake compared to half of the total number of cells.
A* is more computationally expensive than DFS, so by using DFS when the snake is longer, the algorithm can potentially save computation time while still providing a reasonable path for the snake to follow.

# Performance comparison
<img width="435" alt="image" src="https://github.com/RohanSoni-02/CyberPython/assets/110955425/8cc89393-a2db-419c-84c5-7884c206e3cb">
