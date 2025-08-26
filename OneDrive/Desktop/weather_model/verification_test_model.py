def predict_temperature(x):
    return 1 * x**2 - 4 * x + 5

# Simulate historical data comparison
historical = {0: 5, 1: 2, 2: 1, 3: 2, 4: 5}
for x, actual in historical.items():
    predicted = predict_temperature(x)
    print(f"x={x}, Predicted={predicted:.2f}, Actual={actual:.2f}, Error={abs(predicted - actual):.2f}")


