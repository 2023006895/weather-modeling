# deployment_run_model.py
def predict_temperature(x):
    return 1 * x**2 - 4 * x + 5

def run():
    while True:
        try:
            x = float(input("Enter time step (x): "))
            print(f"Predicted Temperature: {predict_temperature(x):.2f} °C")
        except ValueError:
            print("Invalid input. Exiting.")
            break

run()