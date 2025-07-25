"""Step function: Given 我有一些專案在工作資料夾."""
from pathlib import Path


def execute(go_to_job_context):
    """設置工作資料夾的基本環境."""
    # Context already has work_dir from fixture
    # This step just validates the setup
    work_dir = Path(go_to_job_context['work_dir'])
    assert work_dir.exists(), f"Work directory {work_dir} should exist"