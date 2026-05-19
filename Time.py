# Improved Time Module Examples with better comments and structure

import datetime as dt

# 1. Creating time objects
print("=== Time Objects ===")
time1 = dt.time(11, 20, 30, 2000)
print("Time:", time1)
print("Hour:", time1.hour)
print("Minute:", time1.minute)
print("Second:", time1.second)
print("Microsecond:", time1.microsecond)
print()

# 2. Current datetime and operations
print("=== Current DateTime ===")
current = dt.datetime.now()
print("Current:", current)
print("Date:", current.date())
print("Time:", current.time())
print()

# 3. Timedelta calculations
print("=== Timedelta Examples ===")
one_week = dt.timedelta(days=7)
next_week = current + one_week
past_week = current - one_week
print("Next week:", next_week)
print("Past week:", past_week)
print()

# 4. Formatting dates
print("=== Formatted Dates ===")
print("Formatted:", current.strftime("%Y-%m-%d %H:%M:%S"))
print("ISO Format:", current.isoformat())