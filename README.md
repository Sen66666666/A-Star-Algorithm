# A-Star Algorithm
## Introduction
The A-star (A*) algorithm is a widely used path-finding and graph traversal algorithm for finding the best path from an initial point to a goal point on the graph plane. It helps to find the shortest path from one point to another. The A-Star algorithm combines the high performance of best-first search with the utility of Dijkstra's algorithm. It is commonly used in a variety of applications, such as AI in games, map navigation, etc.
## Principles
1. Heuristic function
 - The A* algorithm uses heuristic functions to estimate the cost from any node to the target node. The most commonly used heuristic functions are Manhattan distance, Euclidean distance, etc.
2. Calculation of F, G and H
 - G (movement cost): the actual cost from the starting point to the current node.
 - H (predicted cost): predicted cost from the current node to the goal
 - F (total cost): F = G + H. F is a composite score of the nodes and is used to compare which node is more feasible.
3. Algorithm Steps
 - Add the start node to the open list.
 - Repeat the following steps until the Open list is empty:
   - Select a node with the smallest F value from the open list, called the current node
   - Remove the current node from the on list and add it to the off list
   - For each neighboring node, it is ignored if it is already in the closed list. If it is not in the open list then calculate its F, G and H values and add it to the open list. If it is already in the open list then update its G value to find a better path.
 - If the target node is added to the closure list, then the path has been found
 - If the open list is empty but the target node is not added to the close list, then the path does not exist.
## Starting Method
1. Make sure gui.py and pathPlanner.py are in the same folder.
2. Run
   ```
   python gui.py
   ```
3. How to use gui
 - Adding a satrting point
 - Adding an end point
 - Adding obstacles
 - Clicking run
4. Example:
   
   ```HTML
<video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
</video>
```


     
