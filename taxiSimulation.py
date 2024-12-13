import random
import time
from taxiRepository import TaxiRepository, Taxi
from orderingSystem import OrderingSystem
from order import Order
from constants import  DEFAULT_TIME , GRID_LEN , MAX_DISTANCE , NUM_TAXIS


class TaxiSimulation:
    def __init__(self, num_taxis=NUM_TAXIS, cycle_time=DEFAULT_TIME):
        self.taxi_repo = TaxiRepository()
        self.ordering_system = OrderingSystem(taxi_repository=self.taxi_repo)
        self.num_taxis = num_taxis
        self.cycle_time = cycle_time


    def generate_valid_coordinates(self,start_x, start_y):
        """ Ensures that the endpoint stays within bounds (0 to 20000) and within a 2km radius """
        # Generate a random distance offset in both directions (positive or negative)
        offset_x = random.randint(-MAX_DISTANCE, MAX_DISTANCE)
        offset_y = random.randint(-MAX_DISTANCE, MAX_DISTANCE)
        
        # Calculate the potential end coordinates
        end_x = start_x + offset_x
        end_y = start_y + offset_y
        
        # Ensure end coordinates stay within bounds (0 to 20000)
        end_x = max(0, min(GRID_LEN, end_x))
        end_y = max(0, min(GRID_LEN, end_y))
        
        return end_x, end_y


    def initialize_taxis(self):
        """ Initialize taxis with random locations and add them to the repository """
        print("Initial taxi locations: ")
        for i in range(self.num_taxis):
            x = random.randint(0, GRID_LEN)
            y = random.randint(0, GRID_LEN)
            taxi = Taxi(x=x, y=y)
            self.taxi_repo.add_taxi(taxi)
            print(taxi)



    def simulate_one_cycle(self):
        """ Perform one cycle of the simulation: add a new order and process the system """
        # Generate a random starting point for the order
        start_x = random.randint(0, GRID_LEN)
        start_y = random.randint(0, GRID_LEN)
        
        # Generate a valid endpoint for the order
        end_x, end_y = self.generate_valid_coordinates(start_x, start_y)
        
        # Create and add the order to the ordering system
        order = Order(start_x, start_y, end_x, end_y)
        self.ordering_system.add_order(order)

        # Process the ordering system
        self.ordering_system.update_taxis()
        self.ordering_system.assign_orders()
        self.ordering_system.print_status()
        self.ordering_system.cycle_count+=1


    def run_simulation(self):
        self.initialize_taxis()

        # Simulate the system
        while True:
            time.sleep(self.cycle_time)  
            self.simulate_one_cycle()


