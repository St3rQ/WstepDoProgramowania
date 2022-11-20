import random

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(f"Min: {min(punkty)}")
print(f"Max: {max(punkty)}")
avg = sum(punkty) / len(punkty)
print(f"Average: {round(avg, 2)}")
