# Entry point: launches all agents and Streamlit UI

from agents.coordinator_agent import CoordinatorAgent
from ui.streamlit_app import run_app

if __name__ == '__main__':
    coordinator = CoordinatorAgent()
    coordinator.launch()
    run_app(coordinator)
