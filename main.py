import time

for i in range(10):
    print(f"Прогресс: {i}/10", end="\r")
    time.sleep(1)