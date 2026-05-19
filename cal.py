# Improved Calendar Module with useful utilities

import calendar as cal

print("=== Calendar Examples ===")

# Current month
print("March 2025 Calendar:")
print(cal.month(2025, 3))
print()

# Full year
print("2026 Full Calendar (truncated):")
print(cal.calendar(2026)[:500] + "...")
print()

# Weekday check
print("Weekday of 18 Dec 2026:", cal.weekday(2026, 12, 18), "(0=Mon)")
print()

print("Is 2026 leap year?", cal.isleap(2026))
print("Leap days 2000-2026:", cal.leapdays(2000, 2026))

# Text calendar example
print("\n=== Text Calendar ===")
tc = cal.TextCalendar()
print(tc.formatmonth(2025, 5))