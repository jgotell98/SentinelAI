# demo/simulate_attack.py
import random

def simulate_bruteforce():
    logs = []
    for _ in range(50):
        logs.append({
            "failed": random.choice([True, False]),
            "attempts": random.randint(1, 20)
        })
    return logs

if __name__ == "__main__":
    print(simulate_bruteforce())
