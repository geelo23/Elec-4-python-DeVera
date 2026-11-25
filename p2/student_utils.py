# Full Name: De Vera, John Angelo
# Section: IV-BSIT C
# Activity: P2 module
# Date: 2026-11-15

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def determine_status(grades, passing_mark=75):
    return "PASSED" if grades and calculate_average(grades) >= passing_mark else "FAILED"

def get_highest(grades):
    return max(grades) if grades else None

def get_lowest(grades):
    return min(grades) if grades else None
