import importlib
import time
import matplotlib.pyplot as plt


def run_algorithm(day_number):
    module_name = f'day{day_number:02d}'

    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)

        # Check if the 'solve' function exists in the module
        if hasattr(module, 'solve') and callable(module.solve):
            start_time = time.time()
            module.solve(1)  # Run the solve function
            end_time = time.time()
            t1 = end_time - start_time

            start_time = time.time()
            module.solve(2)  # Run the solve function
            end_time = time.time()
            t2 = end_time - start_time

            return t1, t2
        else:
            return 0, 0

    except ImportError:
        print(f"Day {day_number}: Module not found.")


x = list(range(1, 26))
t1s, t2s = [], []
for day_number in x:
    t1, t2 = run_algorithm(day_number)
    t1s.append(t1)
    t2s.append(t2)


plt.figure(figsize=(10, 5))
plt.bar(x, t2s, label='Part 2')
plt.bar(x, t1s, label='Part 1')
plt.xlabel('Day')
plt.ylabel('Time (s)')
plt.ylim(0, 1)
plt.legend()
plt.show()