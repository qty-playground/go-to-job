"""Step function: Then 虛擬環境應該被自動啟用."""


def execute(go_to_job_context):
    """驗證虛擬環境是否被啟用."""
    venv_activated = go_to_job_context.get('venv_activated', False)
    assert venv_activated is True, "虛擬環境應該被自動啟用"
    
    # Verify the project has venv
    selected_project = go_to_job_context.get('selected_project')
    assert selected_project is not None, "應該有選擇的專案"