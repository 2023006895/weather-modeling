# maintenance_update_model.py
def predict_temperature(x, a=1, b=-4, c=5):
    return a * x**2 + b * x + c

# Example: update coefficients based on new data
new_coeffs = {'a': 0.9, 'b': -3.8, 'c': 4.7}
x = float(input("Enter time step (x): "))
temp = predict_temperature(x, **new_coeffs)
print(f"Updated Prediction at x={x:.1f} is {temp:.2f}°C")