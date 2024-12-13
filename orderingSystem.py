from taxiRepository import TaxiRepository
from order import Order
from collections import deque
from constants import TaxiState , DEFAULT_TIME


class OrderingSystem:
    def __init__(self, taxi_repository: TaxiRepository):
        self.taxi_repository = taxi_repository  
        self.order_queue = deque()  
        self.cycle_count = 1
    
    def add_order(self, order):
        """ Adds a new order to the waiting queue """
        self.order_queue.append(order)

    
    def assign_orders(self):
        """ Assign taxis to orders in the queue if available """

        while self.order_queue:
            order = self.order_queue[0]
            nearest_taxi = self.find_nearest_taxi(order)
            if nearest_taxi:
                nearest_taxi.assign_order(order) 
                order.assign_to_taxi(nearest_taxi) 
                self.order_queue.popleft()
            else:
                break # No available taxis
           

    def get_taxis(self):
        """ Returns all taxis in the repository """
        return self.taxi_repository.get_taxis()
    
    
    def find_nearest_taxi(self, order: Order):
        """ Finds the nearest available taxi to the given order's start location """

        available_taxis = self.taxi_repository.get_available_taxis()
        if not available_taxis:
            return None  

        nearest_taxi = available_taxis[0]
        nearest_distance = nearest_taxi.calculate_distance(order.get_start()[0], order.get_start()[1])

        for taxi in available_taxis[1:]:
            distance = taxi.calculate_distance(order.get_start()[0], order.get_start()[1])
            if distance < nearest_distance:
                nearest_taxi = taxi
                nearest_distance = distance
    
        return nearest_taxi


    def update_taxis(self):
        """ This function will be called to update the location of all taxis. """
        for taxi in self.taxi_repository.get_taxis():
            if taxi.order is not None: 
                order = taxi.order
                taxi.move_toward(order) 
        


    def print_status(self):
        """ Prints the current state of the system """

        elapsed_time = self.cycle_count * DEFAULT_TIME
        print(f"\nAfter {elapsed_time} seconds:")
        

        print("Order Queue:")
        if self.order_queue:
            for order in self.order_queue:
                print(order)
        else:
            print("Empty")

        print("\nTaxi locations:")
        for taxi in self.taxi_repository.get_taxis():
            print(taxi)


