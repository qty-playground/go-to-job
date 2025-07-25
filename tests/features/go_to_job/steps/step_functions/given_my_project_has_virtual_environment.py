"""Step function: Given 我的專案 {project_name} 有虛擬環境."""
from pathlib import Path


def execute(go_to_job_context, project_name):
    """創建有虛擬環境的專案."""
    work_dir = Path(go_to_job_context['work_dir'])
    project_path = work_dir / project_name
    project_path.mkdir(exist_ok=True)
    
    # Create venv directory to simulate virtual environment
    venv_path = project_path / 'venv'
    venv_path.mkdir(exist_ok=True)
    
    # Create activate script to simulate real venv
    bin_path = venv_path / 'bin'
    bin_path.mkdir(exist_ok=True)
    activate_script = bin_path / 'activate'
    activate_script.write_text('# Virtual environment activation script\n')
    
    go_to_job_context['projects'].append(project_name)
    go_to_job_context['target_project'] = project_name