from taxi import Taxi
from constants import TaxiState

class TaxiRepository:
    def __init__(self):
        self.taxis = [] 

    def add_taxi(self, taxi: Taxi):
        self.taxis.append(taxi)

    def remove_taxi(self, taxi: Taxi):
        if taxi in self.taxis:
            self.taxis.remove(taxi)

    def get_available_taxis(self):
        """ Returns taxis that are not assigned to an order """
        return [taxi for taxi in self.taxis if taxi.state == TaxiState.AVAILABLE]

    def get_taxis(self):
        return self.taxis
