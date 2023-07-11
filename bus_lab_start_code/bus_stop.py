class BusStop:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self,):
        return len(self.queue)
    
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        bus_stop.clear()
    
    # def pick_up_from_stop_recap(self, bus_stop):
    #     for passenger in bus_stop.queue:
    #         self.passenger.append(passenger)
    #     bus_stop.clear()

        

    def drop_off(self, passenger_to_drop_off):
        self.passengers.remove(passenger_to_drop_off)

    def empty_bus(self):
        self.passengers.clear()
    




