from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class TaskManagementCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def task_intake_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['task_intake_specialist'],
            verbose=True
        )
    
    @agent
    def task_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['task_planner'],
            verbose=True
        )
    
    @task
    def intake_task(self) -> Task:
        return Task(
            config=self.tasks_config['intake_task']
        )
    
    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
            output_file='daily_schedule.md'
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbos=True
        )