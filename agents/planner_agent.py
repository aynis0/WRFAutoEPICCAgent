import time


class PlannerAgent:

    def __init__(self):
        self.total_tokens = 0

    def plan_task(self):
        print("[PLANNER] Parsing atmospheric workflow...")
        time.sleep(1)

        subtasks = [
            "Load WRF metadata",
            "Analyze nested domains",
            "Build EPICC species mapping",
            "Run mass conservation diagnostics",
            "Generate runtime correction strategy",
            "Execute validation workflow"
        ]

        for idx, task in enumerate(subtasks):
            print(f"[PLANNER] Subtask {idx+1}: {task}")
            self.total_tokens += 180000
            time.sleep(0.5)

        print(f"[TOKEN] Planner Agent consumed: {self.total_tokens:,}")
