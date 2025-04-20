from crewai import Crew, Process
from agents import coordinator_agent, travel_info_agent, local_recommendation_agent
from tasks import initial_travel_plan_task, local_recommendation_task, final_coordinator_task

class TravelCoordinatorCrew():
    # 팀구성
    def crew(self) -> Crew:
        return Crew(
            agents=[travel_info_agent, local_recommendation_agent,coordinator_agent], # 이건 순서 중요치 않다.
            tasks=[initial_travel_plan_task, local_recommendation_task, final_coordinator_task],
            process=Process.sequential,  # Task에 등록된 순서대로 작업하는 process
            verbose=True
        )


