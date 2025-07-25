"""Step function: Given 我在工作目錄有專案 {project_name}."""
from pathlib import Path


def execute(go_to_job_context, project_name):
    """在工作目錄中創建指定的專案."""
    work_dir = Path(go_to_job_context['work_dir'])
    project_path = work_dir / project_name
    project_path.mkdir(exist_ok=True)
    go_to_job_context['projects'].append(project_name)
    
    # Store the specific project for later steps
    go_to_job_context['target_project'] = project_name