from datetime import datetime
from latest_ai_development.crew import TaskManagementCrew

def run():
    user_task_input = """
        Finish the ML model training script by Monday.
        Submit the internship report by Friday.
        Call mom this weekend.
        Do laundry on Sunday.
        Review team PRs.
        Read a research paper on LLM Safety.
        Prepare slides for team sync.
        Go for a run in the evening.
    """

    inputs = {
        'user_tasks': user_task_input,
        'current_year': str(datetime.now().year)
    }

    try:
        TaskManagementCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")