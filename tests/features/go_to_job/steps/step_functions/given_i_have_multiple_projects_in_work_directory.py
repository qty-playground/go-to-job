"""Step function: Given 我在工作目錄有多個專案."""
from pathlib import Path


def execute(go_to_job_context):
    """在工作目錄中創建多個測試專案."""
    work_dir = Path(go_to_job_context['work_dir'])
    project_names = ["web-app", "api-server", "data-tool"]
    
    for project_name in project_names:
        project_path = work_dir / project_name
        project_path.mkdir(exist_ok=True)
        go_to_job_context['projects'].append(project_name)
    
    # Verify projects were created
    assert len(go_to_job_context['projects']) == 3