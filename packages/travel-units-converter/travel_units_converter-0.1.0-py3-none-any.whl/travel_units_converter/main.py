# travel_units_converter/converter.py

def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def gallon_to_liters(gallons):
    return gallons * 3.78541


def liters_to_gallon(liters):
    return liters / 3.78541


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def pounds_to_kgs(pounds):
    return pounds * 0.453592


def kgs_to_pounds(kgs):
    return kgs / 0.453592


def yards_to_meters(yards):
    return yards * 0.9144


def meters_to_yards(meters):
    return meters / 0.9144
