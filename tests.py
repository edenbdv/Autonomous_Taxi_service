
from constants import TaxiState , DEFAULT_TIME
from taxi import Taxi
from order import Order
from taxiRepository import TaxiRepository
from constants import TaxiState
from orderingSystem import OrderingSystem

def test_move_toward1():
    taxi = Taxi( x=0, y=0)
    order = Order(100, 100, 10, 10)  
    taxi.assign_order(order)

    print(f"Initial taxi location: {taxi.x}, {taxi.y}")

    print(f"start order location: ", order.get_start())
    print(f"end order location: ", order.get_end())

    is_arrived = taxi.move_toward(order, time=DEFAULT_TIME)
    new_location = (taxi.x, taxi.y)  

    print(f"New location of Taxi: {new_location}")
    print(f"Has the taxi arrived at the target? {is_arrived}")
    print(f"Taxi state: {taxi.state}")
    print("----------------------------")

    # Test condition: The taxi should have arrived and be available
    if is_arrived and taxi.state == TaxiState.AVAILABLE:
        print("Test  move_toward-1 Passed!")
    else:
        print("Test move_toward-1 Failed!")
    print("----------------------------")


def test_move_toward2():
    taxi = Taxi( x=0, y=0)
    order = Order(300, 300, 10, 10)  
    taxi.assign_order(order)

    print(f"Initial taxi location: {taxi.x}, {taxi.y}")

    print(f"start order location: ", order.get_start())
    print(f"end order location: ", order.get_end())

    is_arrived = taxi.move_toward(order, time=DEFAULT_TIME)
    new_location = (taxi.x, taxi.y)  

    print(f"New location of Taxi: {new_location}")
    print(f"Has the taxi arrived at the target? {is_arrived}")
    print(f"Taxi state: {taxi.state}")
    print("----------------------------")

    # Test condition: The taxi should have arrived and be available
    if  not is_arrived and taxi.state == TaxiState.DRIVING_TO_START:
        print("Test move_toward-2 Passed!")
    else:
        print("Test move_toward-2 Failed!")
    print("----------------------------")


def test_move_toward3():
    taxi = Taxi( x=0, y=0)
    order = Order(100, 100, 300, 300)  
    taxi.assign_order(order)

    print(f"Initial taxi location: {taxi.x}, {taxi.y}")

    print(f"start order location: ", order.get_start())
    print(f"end order location: ", order.get_end())

    is_arrived = taxi.move_toward(order, time=DEFAULT_TIME)
    new_location = (taxi.x, taxi.y)  

    print(f"New location of Taxi: {new_location}")
    print(f"Has the taxi arrived at the target? {is_arrived}")
    print(f"Taxi state: {taxi.state}")
    print("----------------------------")

    # Test condition: The taxi should have arrived and be available
    if  not is_arrived and taxi.state == TaxiState.DRIVING_TO_END:
        print("Test move_toward-3 Passed!")
    else:
        print("Test move_toward-3 Failed!")
    print("----------------------------")


def test_find_nearest_taxi1():
    taxi1 = Taxi( x=1274, y=6379)
    taxi2 = Taxi( x=5931, y=18042)
    taxi3 = Taxi( x=554, y=1490)
    taxi3.state = TaxiState.DRIVING_TO_END

    taxi_repo = TaxiRepository()
    taxi_repo.add_taxi(taxi1)
    taxi_repo.add_taxi(taxi2)
    taxi_repo.add_taxi(taxi3)

    order = Order(556, 1492, 0, 2505)  
    orderingSystem = OrderingSystem(taxi_repository= taxi_repo)
    orderingSystem.add_order(order)
    nearest_taxi = orderingSystem.find_nearest_taxi(order)


    print(f"nearest_taxi: ", nearest_taxi.id)

 
    print("----------------------------")
    # Test condition: The taxi should have arrived and be available
    if  nearest_taxi.id == taxi1.id:
        print("Test test_find_nearest_taxi Passed!")
    else:
        print("Test test_find_nearest_taxi Failed!")
    print("----------------------------")



def test_find_nearest_taxi2():
    taxi1 = Taxi( x=1274, y=6379)
    taxi2 = Taxi( x=5931, y=18042)
    taxi3 = Taxi( x=554, y=1490)

    taxi_repo = TaxiRepository()
    taxi_repo.add_taxi(taxi1)
    taxi_repo.add_taxi(taxi2)
    taxi_repo.add_taxi(taxi3)

    order = Order(556, 1492, 0, 2505)  
    orderingSystem = OrderingSystem(taxi_repository= taxi_repo)
    orderingSystem.add_order(order)
    nearest_taxi = orderingSystem.find_nearest_taxi(order)


    print(f"nearest_taxi: ", nearest_taxi.id)
 
    print("----------------------------")

    # Test condition: The taxi should have arrived and be available
    if  nearest_taxi.id == taxi3.id:
        print("Test test_find_nearest_taxi Passed!")
    else:
        print("Test test_find_nearest_taxi Failed!")
    print("----------------------------")

# Run the test function
test_move_toward1()
test_move_toward2()
test_move_toward3()
test_find_nearest_taxi1()
test_find_nearest_taxi2()