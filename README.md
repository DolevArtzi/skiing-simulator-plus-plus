# Python Project: Skiing Simulator++
#### By: Dolev Artzi, April 2024
#### Student: [add your name here]
> # Setup
> [todo]

In this project, we will be building our first [Python `Classes`](https://docs.python.org/3/tutorial/classes.html).  In programming, a class is a collection of functions and data that all serve a cohesive purpose, bundled into one *object* (See `class_ex.ipynb` [todo] for basic usage of a toy example class). Accordingly, we will loosely follow the tenants of [object-oriented programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming), which is a style of programming centered around (usually real-world) objects, like a ski lift, or a ski rental store, or a car, or a todo list.

# Task 1: Getting to the Mountain

## Data Associated with `Navigator` [`navigator.py`]
> - `navigator : dict`: a dictionary mapping store types to a list of tuples, each containing the name and location of the given point of interest
    > - example k:v pair: 
        > `'breakfast': [('bshop 1', (10,50)), ('bshop 2', (35,75))]` means breakfast shop `bshop 1` is located at `(10,50)`, etc.
    > - keys: `breakfast`, `rental`, `mountain`

> ## Functions in `Navigator`, In Order
> `__init__`: initializes the navigator class. This is done for you
> `distance`
> ### Description
    > - computes the distance between the two points, `p1` and `p2`
> ### Inputs
    > - `p1 : tuple[float]`: the first location's x and y coords
    > - `p2 : tuple[float]`: the second location's x and y coords 
> `find_route`
> ### Description
    > - finds the shortest route from your current location, passing through a breakfast store, a rental store, and then to the nearest mountain
    > - brute force it: use a (very) nested for loop
        > - NOTE: we'll see much smarter algorithms for this in the future
> ### Inputs
    > - `curr_loc : tuple[float]`: your current x,y coordinates
> ### Returns
    > - `best_path`: a list of names, like this: `[breakfast store, rental store, mountain]` corresponding to the stops on the shortest path

# Task 2: Renting Gear For You and Your Friends
> ## Data Associated With the `RentalStore` Class   [`rental_store.py`]
> - `name : str`: the name of this particular store
> - `location : tuple[number]`: a tuple of an `x-coordinate` and `y-coordinate`, indicating the location of the store
> - `is_weekend : bool`: a `boolean` representing whether it's the weekend
> - `is_season : bool`: a `boolean` representing whether or not it's the ski season
> - `gear_types : list[str]`: the available gear at the rental store, each represented by a `str`
> - `money_earned : float`: the total money made from all the day's transactions. `float` means it can be a decimal, not just an integer (`int`)
> - `skiers_served : dict`: a dictionary, mapping `skier_name |-> gear_sold`, where `skier_name : str` and `gear_sold : list[tuple[str,float]]` is a list of tuples, where each element in the list is `(gear_name,price_sold)` 
> - `price_points : dict`: a dictionary, mapping `gear_type |-> price_ranges`, where `gear_type : str` is the name for the type of gear, and `price_ranges : list[tuple[float]]` is a list of available price ranges for each type of gear

> ## Functions in `RentalStore`, In Order
> `__init__`: Initializes the class and all its data. This is done for you

> `generate_prices`
> ### Description
    > - uses Python's `random` module to generate 3 price ranges for each item this store sells
    > - make your own price ranges, so that they don't overlap
    > - make the prices higher if it's the weekend (`is_weekend`) or if it's skiing season (`is_season`), and the highest if it's both the weekend and ski season
> ### Effects
    >   - populates the `price_points` dictionary, mapping each `gear_type` to a length-3 list of tuples of price ranges

> `generate_price`
> ### Description
    > - given the `item_name`, and the index into `price_points`, generates a random price for the given item using Python's `random` module
> ### Inputs
    > - `item_name : str`
    > - `range_idx : int`: either `0`, `1`, or `2`: the index into the corresponding tuple of price ranges in the `price_points` dictionary
> ### Returns
    > - the randomly generated price for the given item, which should be in the specified range

> `serve_skier`
> ### Description
    > - sells the skier the gear they need, and stores that information within the class
    > - uses `generate_price` to generate the price for each item, in the range upper bounded by `prices_max[i]`
> ### Inputs
    > - `skier_name : str`
    > - `gear_list : list[str]`: a list of the gear items the skier needs to buy
    > - `prices_max : list[int]`: a list of the skier's price range for each item, such that `prices_max[i]` is the skier's max price range for the item referenced by `gear_list[i]`
        > - this is represented by an index: `0`, `1`, or `2`: with 0 being the lowest price range, and 2 being the highest
> ### Effects
    > - adds a new k:v pair to the `skiers_served` dictionary, where the key is the skier's name, and the value is a list of tuples, for example, `[('pants',100),('coat',250)]` means you sold the skier pants which cost $100 and a coat that costs $250

>  `serve_group`
> ### Description
    > - uses `RentalStore.serve_skier` to sell each skier in the `skier_info` dictionary the gear they need
> ### Inputs
    > - `skier_info : dict`: a dictionary mapping skier names to a tuple of lists:
    >    - the first list is that skier's `gear_list`, and the second is that skier's `prices_max`, one for each item
> ### Effects:
    > - populates the `skiers_served` dictionary, through the use of the `serve_skier` function

> `check_out_skier`
> ### Description
    > - after selling the gear for the skier given by `skier_name`, and populating their information into `skiers_served`, tracks how much money we earned from that skier
> ### Effects
    > - adds the cumulative cost of goods sold to the given skier to `RentalStore.money_earned`

> `print_sales`
> ### Description
    > - nicely prints a summary of the day's sales

> `close_store`
> ### Description
    > - for each skier served, add the money earned from them to `money_earned`, and nicely displays the day's spoils. To display, calls `RentalStore.print_sales` after calling `check_out_skier` for each skier we served today
> ### Effects
    > - fills in the day's information to the `money_earned` parameter of our `RentalStore`

# Task 3: Tracking Metrics While You Ski
## Data Associated With `Tracker` [`tracker.py`]
> - `skier_name : str`
> - `mountain_name : str`
> - `runs : int`: the total number of runs for the day
> - `distance_skied : float`
> - `distance_on_lifts : float`
> - `max_speed : float`
> - `max_dist : float`
> - `avg_speed : float`
> - `avg_dist : float`

> ## Functions in `Tracker`, In Order
> `__init__`: initializes the class and all its data. This is done for you

> `track_lift`
> ### Description
    > - adds the information from a lift to `distance_on_lifts`
> ### Inputs
    > - `base_elev : float`
    > - `peak_elev : float`

> `track_run`
> ### Description
    > - tracks the information from this run
> ### Inputs
    > - `peak_elev : float`
    > - `base_elev : float`
    > - `time : float`: the time this run took, in hours
    > - `max_speed : float`: the top speed acheived on this run, in mph
> ### Effects
    > - updates the relevant statistics stored by `Tracker`

> `compute_metrics`
> ### Description
    > - computes the available metrics for the skier in question, at the end of the day
> ### Effects
    > - updates all the relevant metrics stored by `Tracker`