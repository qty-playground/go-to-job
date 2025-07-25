"""Step function: Given 我的專案 {project_name} 沒有虛擬環境."""
from pathlib import Path


def execute(go_to_job_context, project_name):
    """創建沒有虛擬環境的專案."""
    work_dir = Path(go_to_job_context['work_dir'])
    project_path = work_dir / project_name
    project_path.mkdir(exist_ok=True)
    
    # Create some dummy files to make it look like a real project
    readme_file = project_path / 'README.md'
    readme_file.write_text(f'# {project_name}\n\nA simple project without virtual environment.\n')
    
    go_to_job_context['projects'].append(project_name)
    go_to_job_context['target_project'] = project_name