class Hamster:
    def __init__(self, consumption, avidity):
        self.consumption = consumption
        self.avidity = avidity

    def get_hamster_total_consumption(self, number_of_hamsters):
        return self.consumption + self.avidity * (number_of_hamsters - 1)
