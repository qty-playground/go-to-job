"""Step function: Then 我應該看到可用專案的清單."""


def execute(go_to_job_context):
    """驗證是否顯示了專案清單."""
    projects = go_to_job_context['command_output']
    
    # Verify we have projects list
    assert projects is not None, "應該有專案清單輸出"
    assert len(projects) > 0, "應該至少有一個專案"
    
    # Verify expected projects are in the list
    expected_projects = go_to_job_context['projects']  # ['web-app', 'api-server', 'data-tool']
    project_names = [p.name for p in projects]
    
    for expected in expected_projects:
        assert expected in project_names, f"應該包含專案 {expected}"