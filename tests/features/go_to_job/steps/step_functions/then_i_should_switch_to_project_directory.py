"""Step function: Then 我應該切換到專案目錄."""


def execute(go_to_job_context, project_name=None):
    """驗證是否成功切換到專案目錄."""
    # Check navigation result
    result = go_to_job_context.get('navigation_result')
    assert result is True, "應該成功導航到專案目錄"
    
    # Verify selected project exists
    selected = go_to_job_context.get('selected_project')
    assert selected is not None, "應該有選擇的專案"
    
    # If project_name is provided, verify it matches
    if project_name:
        assert selected == project_name, f"選擇的專案應該是 {project_name}, 實際是 {selected}"