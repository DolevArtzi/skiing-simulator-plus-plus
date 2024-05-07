### TASK 1
class Navigator:
    def __init__(self,location_info):
        # breakfast: [breakfast store location list]
        # rental: [rental store location list]
        # mountain: [mountain location list]
        self.location_info = location_info
    
    """ distance
    Description:
        - computes the distance between the two points, p1 and p2
    Inputs:
        - p1 : tuple[float]: the first location's x and y coords
        - p2 : tuple[float]: the second location's x and y coords 
    """
    def distance(self,p1,p2):
        return ((p1[0] - p2[0]) ** 2 + (p2[1] - p2[1]) ** 2) ** 0.5

    """ find_route
    Description: 
        - finds the shortest route from your current location, passing through
            a breakfast store, a rental store, and then to the nearest mountain
        - brute force it: use a (very) nested for loop
            - NOTE: we'll see much smarter algorithms for this in the future
    Inputs:
        - curr_loc : tuple[float]: your current x,y coordinates
    Returns:
        - best_path: a list of names, like this: [breakfast store, rental store, mountain]
            corresponding to the stops on the shortest path
    """
    def find_route(self,curr_loc):
        min_dist = float('inf') #initialize the minimum distance so far as infinity
        best_path = []
        ### TODO: make a triple-nested for loop to iterate over each combination of 
            # breakfast store, rental store, mountain. Update min_dist and best_path
            # accordingly. By the end of the for loops, best_path should contain the 
            # name of the breakfast store, rental store, and mountain, that are on the 
            # shortest path from where you are

        ### TODO: nicely print out the best path, before returning it
        return best_path
