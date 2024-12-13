from taxiSimulation import TaxiSimulation

def main():
    simulation = TaxiSimulation(num_taxis=10, cycle_time=20)
    simulation.run_simulation()

if __name__ == "__main__":
    main()