#Define a heuristic function to estimate the distance between two points
def heuristic(x1,y1,x2,y2):
    return (((x2-x1)**2)+((y2-y1)**2))**0.5 # Calculate and return the Euclidian distance between two points

#Define the function that finds the grid with the lowest f-score
def find_grid(open_set, f_scores):
    lowest = float('inf') #Initializes a variable lowest, setting it to positive infinity
    lowest_grid = None #This variable will be used to store the lowest f_score. Initially set to None because no grid has been found yet
    for grid in open_set: #Start traversing each grid in the open_set collection
        if f_scores[grid] < lowest: #Check if the f_score of the current grid is less than the lowest score currently recorded
            lowest = f_scores[grid] #Update lowest to this smaller value.
            lowest_grid = grid #Update lowest_grid to this smaller value.
    return lowest_grid #After traversing all the grids in open_set, the function returns the grid with the lowest f_score value

def do_a_star(grid, start, end, display_message):
    g_function = {start: 0} #Initialize g_function, which records the actual cost of movement from the starting point to each node
    f_function = {start: heuristic(start[0], start[1], end[0], end[1])} # Initialize f_function with the f-score for the starting node, based on Euclidian distance to the end node.
    open_set = {start} #Initialize the open_set collection and add the starting point to it
    came_from = {} #Initialize ‘came_from’, which is used to track the optimal path
    closed_set=set() #Initialize an empty closed_set collection. Once a node has been evaluated, 
                    #it will be added to this set, indicating that there is no need to evaluate again and avoid double calculations.
    display_message(f"Start: {start}, End: {end}") # Display the coordinate of the start and end points


    while open_set: #Continue to loop until open_set is empty, indicating that there are no more nodes to examine.
        current = find_grid(open_set, f_function) # Find the node with the lowest f score from open_set

        if current == end: # If the current node is the end point, start building the shortest path
            path = [current] # Initialize the path list, including the end point first
            while current in came_from: # Trace the path in reverse direction until the starting point
                current = came_from[current] # Update the current node to its precursor node
                path.append(current) # Add the current node to the path list
            path.reverse() # Reverse the list of paths so that it starts at the beginning and ends at the end
            path_coordinates = " -> ".join([f"({x},{y})" for x, y in path]) #Convert the coordinates in the path into string form and connect them with "->" for display
            display_message("Path found: " + path_coordinates) # Display the coordinates of the found path.
            display_message("The path is found") # If the path is found, gui will display the "The path is found"
            return path # Return the found path

        open_set.remove(current) # Remove the current node from the set to be examined
        closed_set.add(current) #Add the current node to the examined set

        for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]: # Traverse adjacent grids (up, down, left, right)
            coordinates = (current[0] + direction[0], current[1] + direction[1]) # Calculate the coordinates(col,row) after the move


            #display_message(f"Next Grid: {coordinates}")# print(f"Next Grid: {coordinates}")
            if 0 <= coordinates[0] < len(grid) and 0 <= coordinates[1] < len(grid[0]) and grid[coordinates[0]][coordinates[1]] == 1:# Check whether the coordinates are within the grid range and can be passed
                if coordinates in closed_set: # If the coordinate(col,row) is already in 'closed_set', ignore this coordinate
                    continue

                tentative_g_score=g_function[current]+1# Calculate the g-score (actual cost) from the starting point to the current coordinates
                
                if coordinates not in open_set: # If the coordinates are not in open_set, add them
                    open_set.add(coordinates)

                elif tentative_g_score >= g_function.get(coordinates, float('inf')):# If the new g-score is not lower than the current g-score of the coordinate, ignore this coordinate
                    continue
                
                # Update the best path information and score to reach this coordinate
                came_from[coordinates]=current
                g_function[coordinates]=tentative_g_score
                f_function[coordinates]=tentative_g_score+heuristic(coordinates[0], coordinates[1], end[0], end[1])

    display_message("The path is not found") #If the path is not found, the gui will display "The path is not found"
    return [] #FUNCTION MUST ALWAYS RETURN A LIST OF (col,row) COORDINATES
#end of file
