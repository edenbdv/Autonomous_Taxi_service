from constants import TaxiState, DEFAULT_TIME  , SPEED

class Taxi:
    _id_counter = 1  # Class-level counter for unique order IDs

    def __init__(self, x, y):
        self.id = Taxi._id_counter  
        Taxi._id_counter += 1 
        self.x = x
        self.y = y
        self.state = TaxiState.AVAILABLE  
        self.speed = SPEED
        self.order = None

    
    def getLocation(self):
        return self.x , self.y


    def assign_order(self, order):
        if  (order.assigned_taxi is None) and (self.state == TaxiState.AVAILABLE):
            self.order = order
            self.state = TaxiState.DRIVING_TO_START
       

    def move_toward(self, order, time=DEFAULT_TIME):
        """Move the taxi based on its state (either towards the start or the destination)."""
        start_x, start_y = order.get_start()
        end_x, end_y = order.get_end()


        if self.state == TaxiState.DRIVING_TO_START :
            remaining_time = self.move_toward_start(start_x, start_y, time)
            if remaining_time > 0:
                self.move_toward_end(order.end_x, order.end_y, remaining_time) # use the remaining_time to move to the end 

        elif self.state == TaxiState.DRIVING_TO_END:
            # Move toward the end if already at the start
            self.move_toward_end(end_x, end_y, time)


        return self.state == TaxiState.AVAILABLE


    def move_toward_start(self, target_x, target_y, time=DEFAULT_TIME):
        """Move the taxi toward the start location."""
        distance_to_travel = self.speed * time # how much can travel in one cycle
        distance = self.calculate_distance(target_x, target_y) # how much need to travel

        if distance <= distance_to_travel:
            # Reached the start location
            self.x = target_x
            self.y = target_y
            remaining_time = time - (distance / self.speed) 
            self.state = TaxiState.DRIVING_TO_END
            return remaining_time
        
        else: # not enogugh to reach to start, Move closer to the start
            self.move_closer(target_x, target_y, distance_to_travel)
            return 0  

    
    def move_toward_end(self, target_x, target_y, time=DEFAULT_TIME):
        """
        Move the taxi toward the target location based on the time and speed.
        Returns True if the taxi reaches the target, otherwise False.
        """
        distance_to_travel = self.speed * time
        distance = self.calculate_distance(target_x, target_y)

        if distance <= distance_to_travel: # Taxi reaches the target location
            self.x = target_x
            self.y = target_y
            self.state = TaxiState.AVAILABLE  
            self.order = None
            return True  

        else:
            # Move closer to the destination
            self.move_closer(target_x, target_y, distance_to_travel)
            return False 
        

    def move_closer(self, target_x, target_y, distance_to_travel):
        """Move the taxi closer to the target location when it cant reach to target."""
        dx = target_x - self.x
        dy = target_y - self.y

        if abs(dx) > 0:
            move_x = min(abs(dx), distance_to_travel) * (1 if dx > 0 else -1)
            self.x += move_x
            distance_to_travel -= abs(move_x)

        if abs(dy) > 0:
            move_y = min(abs(dy), distance_to_travel) * (1 if dy > 0 else -1)
            self.y += move_y


    def calculate_distance(self, x, y):
        """ Calculate Manhattan distance to a given point (x, y). """

        return abs(self.x - x) + abs(self.y - y)
    

    
    def __str__(self):
        """ Provide a string representation for the Taxi object. """

        state = "standing" if self.state==TaxiState.AVAILABLE else "driving"
        id = self.order.id if self.order is not None else None
        return f"Taxi-{self.id}: {self.x}, {self.y} ({state}) , order: {id} "

