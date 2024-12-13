# enums.py
from enum import Enum

class TaxiState(Enum):
    AVAILABLE = 1
    DRIVING_TO_START = 2
    DRIVING_TO_END = 3

DEFAULT_TIME = 20  
SPEED = 20 
GRID_LEN = 20000
MAX_DISTANCE = 2000
NUM_TAXIS = 10
