"""Step function: When 我執行 go-to-job 指令."""
from go_to_job import GoToJobTool


def execute(go_to_job_context):
    """執行 go-to-job 指令."""
    work_dir = go_to_job_context['work_dir']
    tool = GoToJobTool(work_dir)
    
    try:
        projects = tool.list_projects()
        go_to_job_context['command_output'] = projects
    except NotImplementedError:
        # Expected in Red Phase - let it propagate
        raise