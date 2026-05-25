import time
import random


class EmissionAgent:

    def __init__(self):
        self.tokens = 0

    def process_inventory(self):

        print("[EMISSION] Loading MEIC inventory...")
        time.sleep(1)

        species = [
            "SO2", "NOX", "NH3", "CO",
            "VOC", "PM2.5", "PM10", "BC", "OC"
        ]

        for sp in species:
            print(f"[EMISSION] Converting species: {sp}")
            self.tokens += random.randint(50000, 200000)
            time.sleep(0.5)

        print("[EMISSION] Running conservative interpolation...")
        time.sleep(1)

        print("[EMISSION] Generating EPICC input fields...")
        time.sleep(1)

        print(f"[TOKEN] Emission Agent consumed: {self.tokens:,}")
