class Planes:
    def __init__(self, name, country):
        self.type = "AirPlane"
        self.area = "Air"
        self.name = name
        self.country = country


class Airbus(Planes):
    def __init__(self):
        self.name = "Airbus"
        self.country = "France"
        self.engine = 4
        self.seat = 350
        self.tail = 1



airbus = Airbus()

print(airbus.name)  # Airbus
print(airbus.engine)  # 4
print(airbus.seat)  # 350
