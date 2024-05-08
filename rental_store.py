import random

class RentalStore:
    def __init__(self,name,location,is_weekend,is_season) -> None:

        # set the class parameters based off the provided inputs
        self.name = name
        self.location = location
        self.is_weekend = is_weekend
        self.is_season = is_season

        # the available gear, at this store
        self.gear_types = ['skis','poles','boots','helmet','goggles','coat','pants']

        self.money_earned = 0
        self.skiers_served = {}
        self.price_points = {}
    

    """ generate_prices
    Description:
    - uses Python's `random` module to generate 3 price ranges for each item this store sells
    - make your own prices, so that they don't overlap
    - make the prices higher if it's the weekend (is_weekend) or if it's skiing season (is_season),
        and the highest if it's both the weekend and ski season
        - specifically, if it's either the weekend or ski season (but not both), the lowest price should be at least $50 for each item
        - if its both the weekend and ski season, the lowest price should be at least $80 for each item
        - if its neither, the lowest price should be at least $30 for each item
    Effects:
        - populates the `price_points` dictionary, mapping each `gear_type` to a length-3 list of tuples of price ranges
    """
    def generate_prices(self):
        # you can use Python's random module like so:
        # random.randrange(x,y):
        # > a random integer between x and y

        ### TODO
        pass

    """ generate_price
    Description:
        - given the item_name, and the index into price_points[item_name], generates a random price
            using Python's random module, which represents the price of this item that is in the chosen range
    Inputs:
        - item_name : str
        - range_idx : int: either 0, 1, or 2: the index into the corresponding tuple of price ranges
            in the price_points dictionary
    Returns:
        - the randomly generated price for the given item, in the specified range
    """
    def generate_price(self,item_name,range_idx):
        ### TODO
        pass

    """ serve_skier
    Description:
        - sells the skier the gear they need, and stores that information within the class
        - uses generate_price to generate the price for each item, in the range upper bounded by prices_max[i]
    Inputs:
        - skier_name : str
        - gear_list : list[str]: a list of the gear items the skier needs to buy
        - prices_max : list[int]: a list of the skier's price range for each item, such that
            prices_max[i] is the skier's max price range (by index) for the item referenced by gear_list[i] denoted 
            by the index into the price_points list
    Effects:
        - adds a new k:v pair to the `skiers_served` dictionary, where the key is the skier's name,
            and the value is a list of tuples, for example, `[('pants',100),('coat',250)` means you 
            sold the skier pants which cost $100 and a coat that costs $250
    """
    def serve_skier(self,skier_name:str,gear_list:list[str],prices_max:list[int]):
        ### TODO
        pass

    """ serve_group
    Description:
        - uses RentalStore.serve_skier to sell each skier in the `skier_info` dictionary the gear they need
    Inputs: 
        - skier_info : dict: a dictionary mapping skier names to a tuple of lists:
            the first list is that skier's gear_list, and the second is that skier's prices_max for each item
    Effects:
        - populates the skiers_served dictionary, through the use of the serve_skier function
    """
    def serve_group(self,skier_info:dict):
        ### TODO
        pass

    """ check_out_skier
    Description:
        - after selling the gear for the skier given by skier_name, and populating their information into
            skiers_served, tracks how much money we earned from that skier
    Effects:
        - adds the cumulative cost of goods sold to the given skier to RentalStore.money_earned
    """
    def check_out_skier(self,skier_name:str):
        ### TODO
        pass

    """ print_sales
    Description: nicely prints a summary of the day's sales
    """
    def print_sales(self):
        print(f'Store Name: {self.name}, Location: {self.location}')
        #TODO: also print the names of each skier served, what they bought, and how much each item cost
        # then, also print the total money earned that day
        pass


    """ close_store
    Description:
        - for each skier served, add the money earned from them to money_earned, and nicely displays 
            the day's spoils. To display, calls RentalStore.print_sales after calling check_out_skier
            for each skier we served today
    Returns: the total amount of money earned today
    Effects:
        - fills in the day's information to the money_earned parameter of our RentalStore
    """
    def close_store(self):
        ### TODO
        pass