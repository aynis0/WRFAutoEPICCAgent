from agents.planner_agent import PlannerAgent
from agents.runtime_agent import RuntimeAgent
from agents.physics_agent import PhysicsAgent
from agents.validation_agent import ValidationAgent
from agents.emission_agent import EmissionAgent


def main():
    print("[SYSTEM] OpenCode Agent Runtime Initialized")
    print("[SYSTEM] Running in FULL AUTONOMOUS MODE")

    planner = PlannerAgent()
    runtime = RuntimeAgent()
    physics = PhysicsAgent()
    validation = ValidationAgent()
    emission = EmissionAgent()

    planner.plan_task()
    runtime.load_wrf_metadata()
    emission.process_inventory()
    physics.run_diagnostics()
    validation.check_mass_conservation()
    runtime.generate_report()

    print("[SYSTEM] Workflow completed successfully")


if __name__ == "__main__":
    main()
