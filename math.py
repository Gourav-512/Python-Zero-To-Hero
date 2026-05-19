# Enhanced Math Module Examples with more functions

import math as mt

print("=== Math Module Examples ===")
print("sqrt(144)  =", mt.sqrt(144))
print("ceil(2.3)  =", mt.ceil(2.3))
print("floor(2.7) =", mt.floor(2.7))
print("pow(2, 8)  =", mt.pow(2, 8))
print("pi         =", mt.pi)
print("e          =", mt.e)
print()

print("=== Trigonometry ===")
print("sin(90°)   =", mt.sin(mt.radians(90)))
print("cos(0°)    =", mt.cos(0))
print("tan(45°)   =", mt.tan(mt.radians(45)))
print()

print("=== Other Functions ===")
print("fabs(-22.5)=", mt.fabs(-22.5))
print("factorial(5)=", mt.factorial(5))
print("gcd(48,18)=", mt.gcd(48, 18))
print("lcm(12,18)=", mt.lcm(12, 18) if hasattr(mt, 'lcm') else 'lcm not in this Python version')