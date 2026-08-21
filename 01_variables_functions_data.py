"""
Lesson 1: variables, functions, lists, dicts, tuples.

How to use this file:
  - Read each section's comment.
  - Look at the worked EXAMPLE (already done for you, just run it mentally).
  - Fill in the TODO function right below it.
  - Run this file: `python3 01_variables_functions_data.py`
  - It will tell you exactly which exercise is still wrong. Fix, rerun, repeat.

Nothing here is abstract busywork — every exercise mirrors something that
appears in the real uber-geo-system codebase, referenced in [brackets].
"""


# ============================================================
# SECTION 1 — variables, types, f-strings
# ============================================================
# A variable is just a name pointing at a value. Python figures out the type
# (int, float, str, bool) from the value itself — you don't declare it.
#
# f-strings (the f"..." syntax) let you drop variables straight into text.

# EXAMPLE (already correct — just read it):
city = "San Francisco"
num_drivers = 40
print(f"{city} has {num_drivers} drivers online.")


def describe_trip(rider_city: str, eta_min: float) -> str:
    """TODO: return a string like 'Your ride to San Francisco arrives in 4.5 min'
    Same idea as the EXAMPLE above: an f-string with rider_city and eta_min
    dropped into the text.
    """
    raise NotImplementedError


# ============================================================
# SECTION 2 — functions with type hints
# ============================================================
# `def name(arg: type) -> return_type:` is a function. The `: type` and
# `-> type` parts are *type hints* — they don't change how the code runs,
# they're documentation the reader (and tools) can check.
# This is exactly the style used throughout geo.py, e.g.:
#   def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:

# EXAMPLE:
def add_km(a_km: float, b_km: float) -> float:
    return a_km + b_km


def eta_minutes(distance_km: float, speed_kmh: float) -> float:
    """TODO: return how many minutes it takes to travel distance_km at speed_kmh.
    Formula: (distance / speed) hours, converted to minutes (x 60).
    Round to 1 decimal place with round(x, 1).
    """
    raise NotImplementedError


# ============================================================
# SECTION 3 — lists
# ============================================================
# A list is an ordered, changeable collection: [1, 2, 3].
# You'll see list comprehensions a LOT in the real code, e.g. simulation.py's
# snapshot() does: [{"id": d.id, ...} for d in self.drivers.values()]
# That's "build a new list by transforming every item in another list/dict."

# EXAMPLE:
speeds_kmh = [20, 35, 28, 41, 19]
fast_speeds = [s for s in speeds_kmh if s > 25]  # comprehension: filter
print(fast_speeds)  # [35, 28, 41]


def speeds_in_mph(speeds_kmh: list[float]) -> list[float]:
    """TODO: convert every speed in km/h to mph using a list comprehension.
    1 km/h = 0.621371 mph. Round each result to 1 decimal place.
    Same shape as the fast_speeds EXAMPLE above, but transforming
    (s * 0.621371) instead of filtering (s > 25).
    """
    raise NotImplementedError


# ============================================================
# SECTION 4 — dicts
# ============================================================
# A dict maps keys to values: {"a": 1, "b": 2}. The real system stores every
# driver in one: `self.drivers: dict[str, Driver]` — driver ID -> Driver object.
# That's why you'll see `self.drivers[driver_id]` and `self.drivers.values()`
# everywhere in simulation.py.

# EXAMPLE:
driver_speeds = {"d1": 25.0, "d2": 31.5, "d3": 18.0}
print(driver_speeds["d2"])  # 31.5
print(list(driver_speeds.keys()))  # ['d1', 'd2', 'd3']
print(list(driver_speeds.values()))  # [25.0, 31.5, 18.0]


def average_speed(driver_speeds: dict[str, float]) -> float:
    """TODO: return the average of all values in the dict, rounded to 1 decimal.
    Hint: sum(driver_speeds.values()) / len(driver_speeds)
    """
    raise NotImplementedError


def fastest_driver_id(driver_speeds: dict[str, float]) -> str:
    """TODO: return the KEY (driver id) whose value (speed) is highest.
    Hint: max(driver_speeds, key=driver_speeds.get)
    """
    raise NotImplementedError


# ============================================================
# SECTION 5 — tuples & unpacking
# ============================================================
# A tuple is like a list but fixed-size and usually mixed-meaning: (lat, lon).
# geo.py's destination_point() returns a tuple: `return lat, lon` and callers
# unpack it: `new_lat, new_lon = destination_point(...)`.

# EXAMPLE:
point = (37.78, -122.43)  # (lat, lon)
lat, lon = point  # unpacking: two variables from one tuple
print(f"lat={lat}, lon={lon}")


def midpoint(point_a: tuple[float, float], point_b: tuple[float, float]) -> tuple[float, float]:
    """TODO: return the midpoint (average lat, average lon) of two (lat, lon) points,
    as a tuple. Round each value to 4 decimal places.
    Hint: unpack each point first, same as the EXAMPLE above:
    lat_a, lon_a = point_a
    """
    raise NotImplementedError


# ============================================================
# Self-check — do not edit below this line.
# Run this file to see which exercises still need work.
# ============================================================

def _check(label: str, condition: bool, hint: str) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}" + ("" if condition else f"  <-- {hint}"))
    if not condition:
        raise AssertionError(f"{label} is not correct yet. {hint}")


if __name__ == "__main__":
    _check(
        "describe_trip",
        describe_trip("San Francisco", 4.5) == "Your ride to San Francisco arrives in 4.5 min",
        "Use an f-string: f'Your ride to {rider_city} arrives in {eta_min} min'",
    )
    _check(
        "eta_minutes",
        eta_minutes(2.0, 40.0) == 3.0,
        "eta_minutes should compute (distance_km / speed_kmh) * 60, rounded to 1 decimal.",
    )
    _check(
        "speeds_in_mph",
        speeds_in_mph([20, 40]) == [12.4, 24.9],
        "Use a list comprehension: [round(s * 0.621371, 1) for s in speeds_kmh]",
    )
    _check(
        "average_speed",
        average_speed({"d1": 20.0, "d2": 30.0}) == 25.0,
        "sum(driver_speeds.values()) / len(driver_speeds), rounded to 1 decimal.",
    )
    _check(
        "fastest_driver_id",
        fastest_driver_id({"d1": 20.0, "d2": 30.0, "d3": 15.0}) == "d2",
        "max(driver_speeds, key=driver_speeds.get) returns the key with the highest value.",
    )
    _check(
        "midpoint",
        midpoint((37.0, -122.0), (38.0, -121.0)) == (37.5, -121.5),
        "Average the two lats, average the two lons, round each to 4 decimals.",
    )
    print("\nAll checks passed.")
