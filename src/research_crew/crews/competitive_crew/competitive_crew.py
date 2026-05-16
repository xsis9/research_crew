from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from typing import List

from research_crew.tools.source_tracker import SourceTracker


@CrewBase
class CompetitiveCrew():
    """竞品分析 Crew - 多 Agent 协作系统"""

    agents: List  # type: ignore
    tasks: List  # type: ignore

    @agent
    def collector(self) -> Agent:
        return Agent(
            config=self.agents_config['collector'],
            verbose=True,
            tools=[SerperDevTool()],
            llm="anthropic/MiniMax-M2.7"
        )

    @agent
    def analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['analyzer'],
            verbose=True,
            llm="anthropic/MiniMax-M2.7"
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True,
            llm="anthropic/MiniMax-M2.7"
        )

    @agent
    def qa(self) -> Agent:
        return Agent(
            config=self.agents_config['qa'],
            verbose=True,
            llm="anthropic/MiniMax-M2.7"
        )

    @task
    def collect_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_task']
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task']
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task']
        )

    @task
    def qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_task']
        )

    @task
    def revise_task(self) -> Task:
        return Task(
            config=self.tasks_config['revise_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )