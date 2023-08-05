class Planes:
    model = None
    country = "USA"
    def __init__(self,name,country, quantity):
        self.name = name
        self.origin = country
        self.quantity= quantity

first_plane = Planes("MiG","UA",1)
targ_name = first_plane.name
targ_country = first_plane.origin
print(targ_name) # MiG
print(targ_country) # UA

second_plane = Planes("F35","USA",1)
france_plane = Planes("Airbus","French",1)

our_planes = [first_plane.name, second_plane.name, france_plane.name]

print(our_planes) # ['MiG', 'F35', 'Airbus']

airbuses = Planes("Airbus", "France",10)
print(airbuses.quantity) # 10
boeing = Planes("Boeing","USA",30)
print(boeing.quantity) # 30

sum_plane = airbuses.quantity + boeing.quantity
print(sum_plane) # 40
