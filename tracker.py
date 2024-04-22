class Tracker:
    def __init__(self,skier_name, mountain_name):
        # basic data associated with the skier and the mountain
        self.skier_name = skier_name
        self.mountain_name = mountain_name

        # metrics the tracker will update throughout the ski day
        self.runs = 0
        self.distance_skied = 0
        self.distance_on_lifts = 0
        self.max_speed = 0
        self.max_dist = 0
        self.avg_speed = 0
        self.avg_dist = 0
    
    """ track_lift
    Description:
        - adds the information from a lift to distance_on_lifts
    Inputs:
        - base_elev : float
        - peak_elev : float
    """
    def track_lift(self,base_elev,peak_elev):
        ### TODO
        pass

    """ track_run
    Description:
        - tracks the information from this run
    Inputs:
        - peak_elev : float
        - base_elev : float
        - time : float: the time this run took, in hours
        - max_speed : float: the top speed acheived on this run, in mph
    Effects:
        - updates the relevant statistics stored by Tracker
    """
    def track_run(self,peak_elev,base_elev,time,max_speed):
        ### TODO
        pass

    """ compute_metrics
    Description:
        - computes the available metrics for the skier in question, at 
            the end of the day
    Effects:
        - updates all the relevant metrics stored by Tracker
    """
    def compute_metrics(self):
        ### TODO
        pass

    """ display_metrics
    Description:
        - nicely displays the day's skiing metrics
    Effects:
        - prints a well-formatted output to the console
    """
    def display_metrics(self):
        ### TODO (use f-strings)
        pass