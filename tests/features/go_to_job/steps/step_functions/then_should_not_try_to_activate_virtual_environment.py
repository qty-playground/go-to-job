"""Step function: Then 不應該嘗試啟用虛擬環境."""


def execute(go_to_job_context):
    """驗證沒有嘗試啟用虛擬環境."""
    venv_activated = go_to_job_context.get('venv_activated', False)
    assert venv_activated is False, "不應該嘗試啟用虛擬環境"
    
    # Verify the project was still navigated to
    selected_project = go_to_job_context.get('selected_project')
    assert selected_project is not None, "應該仍然導航到專案"