class Order:
    _id_counter = 1  # Class-level counter for unique order IDs

    def __init__(self, start_x, start_y, end_x, end_y):
        self.id = Order._id_counter  
        Order._id_counter += 1      
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.assigned_taxi = None


    def assign_to_taxi(self, taxi):
        self.assigned_taxi = taxi


    def get_start(self):
        return self.start_x, self.start_y

    def get_end(self):
        return self.end_x, self.end_y

        
    def __str__(self):
        """ Provide a string representation for the Order object. """
        return f"Order-{self.id}: from ({self.start_x}, {self.start_y}) to ({self.end_x}, {self.end_y})"

