import time
import random


class ValidationAgent:

    def __init__(self):
        self.tokens = 0

    def check_mass_conservation(self):

        print("[VALIDATION] Checking mass conservation...")
        time.sleep(1)

        domains = ["d01", "d02", "d03", "d04"]

        for domain in domains:
            before = random.uniform(1000, 5000)
            after = before * random.uniform(0.995, 1.005)

            print(
                f"[VALIDATION] {domain} | before={before:.2f} | after={after:.2f}"
            )

            self.tokens += random.randint(80000, 300000)
            time.sleep(0.5)

        print(f"[TOKEN] Validation Agent consumed: {self.tokens:,}")
