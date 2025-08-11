import math
# Hardcoded coefficients
a = 1
b = -5
c = 6
# Calculate discriminant
D = b**2 - 4*a*c
# Compute roots
if D > 0:
x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)
print(f"Two real roots: {x1}, {x2}")
elif D == 0:
x = -b / (2*a)
print(f"One real root: {x}")
else:
print("No real roots")
PHASE 2: Keyboard Input
Save the code given below with this as file name weather_model_input.py
CODE:
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = b**2 - 4*a*c
if D > 0:
x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)
print(f"Two real roots: {x1}, {x2}")
elif D == 0:
x = -b / (2*a)
print(f"One real root: {x}")
else:
print("No real roots")