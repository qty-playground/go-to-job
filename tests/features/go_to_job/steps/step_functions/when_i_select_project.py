"""Step function: When 我選擇 {project_name} 專案."""
from go_to_job import GoToJobTool
from pathlib import Path


def execute(go_to_job_context, project_name):
    """選擇指定的專案進行導航."""
    work_dir = go_to_job_context['work_dir']
    tool = GoToJobTool(work_dir)
    
    try:
        # Navigate to project
        result = tool.navigate_to_project(project_name)
        go_to_job_context['selected_project'] = project_name
        go_to_job_context['navigation_result'] = result
        
        # Check and activate virtual environment if exists
        if result:
            project_path = Path(work_dir) / project_name
            venv_activated = tool.activate_venv_if_exists(project_path)
            go_to_job_context['venv_activated'] = venv_activated
        
    except NotImplementedError:
        # Expected in Red Phase - let it propagate
        raise