from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# from crewai_tools import FirecrawlSearchTool
# import json

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PersonalAcademy():
	"""PersonalAcademy crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools

	# @agent
	# def advisor(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['advisor'],
	# 		verbose=True
	# 	)

	@agent
	def professor(self) -> Agent:
		return Agent(
			config=self.agents_config['professor'],
			verbose=True
		)

	@agent
	def researcher(self) -> Agent:
		# tool = FirecrawlSearchTool(query='what is firecrawl?', search_options={'limit': 3})

		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			# tools=[tool]
		)

	@agent
	def course_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['course_writer'],
			verbose=True
		)
	
	@agent
	def course_lecturer(self) -> Agent:
		return Agent(
			config=self.agents_config['course_lecturer'],
			verbose=True
		)
	
	@agent
	def homework_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['homework_creator'],
			verbose=True
		)
	
	@agent
	def quiz_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['quiz_creator'],
			verbose=True
		)

	@agent
	def teaching_assistant(self) -> Agent:
		return Agent(
			config=self.agents_config['teaching_assistant'],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task

	@task
	def outline_task(self) -> Task:
		return Task(
			config=self.tasks_config['outline_task'],
			output_file='outputs/outline.md'
		)
	
	@task
	def outline_json_task(self) -> Task:
		return Task(
			config=self.tasks_config['outline_json_task'],
			output_file='outputs/outline.json'
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='outputs/research.md'
		)
	
	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='outputs/report.md'
		)
	
	@task
	def write_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_task'],
			output_file='outputs/course_content.md'
		)
	
	@task
	def lecture_task(self) -> Task:
		return Task(
			config=self.tasks_config['lecture_task'],
			output_file='outputs/course_transcript.md'
		)

	# @task
	# def review_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['review_task'],
	# 		output_file='outputs/review.md'
	# 	)
	
	@task
	def homework_task(self) -> Task:
		return Task(
			config=self.tasks_config['homework_task'],
			output_file='outputs/homework.md'
		)
	
	@task
	def quiz_task(self) -> Task:
		return Task(
			config=self.tasks_config['quiz_task'],
			output_file='outputs/quiz.md'
		)
	
	# @task
	# def feedback_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['feedback_task'],
	# 		output_file='outputs/feedback.md'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the PersonalAcademy crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
