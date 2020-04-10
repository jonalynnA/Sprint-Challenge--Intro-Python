# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# NOTE: Base Class is Vehicle

# Base Class


class Vehicle:
    pass

# Inherit from Vehicle


class GroundVehicle(Vehicle):
    pass


class FlightVehicle(Vehicle):
    pass

# Inherit from Ground Vehicle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# Inherit from Flight Vehicle


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass
