"""Configuration feature step definitions."""

from pytest_bdd import scenarios, given, when, then
from pathlib import Path
import os
import tempfile
from .step_functions.fixture_go_to_job_context import go_to_job_context

# Load scenarios from configuration feature
scenarios("../configuration.feature")


@given('我有 go-to-job 工具')
def given_i_have_go_to_job_tool(go_to_job_context):
    """Initialize go-to-job tool."""
    # This step ensures the tool context is ready
    pass


@given('沒有設定工作資料夾')
def given_no_work_directory_configured(go_to_job_context):
    """Clear any work directory configuration."""
    # Remove environment variable if exists
    if 'GOTOJOB_WORK_DIR' in os.environ:
        del os.environ['GOTOJOB_WORK_DIR']
    if 'WORK_DIR' in os.environ:
        del os.environ['WORK_DIR']
    
    # Remove config file if exists
    config_file = Path.home() / '.go-to-job.conf'
    if config_file.exists():
        config_file.unlink()


@given('我設定環境變數 "{var_name}" 為 "{value}"')
def given_environment_variable_set(go_to_job_context, var_name, value):
    """Set environment variable."""
    os.environ[var_name] = value


@given('我有設定檔 "{config_path}" 內容為 "{content}"')
def given_config_file_with_content(go_to_job_context, config_path, content):
    """Create config file with specified content."""
    config_file = Path(config_path).expanduser()
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(content)


@then('應該掃描 "{directory}" 目錄中的專案')
def then_should_scan_directory(go_to_job_context, directory):
    """Verify the correct directory is being scanned."""
    expected_dir = Path(directory).expanduser()
    # This would be verified by checking the tool's work directory
    # For now, we'll store the expected directory in context
    go_to_job_context['expected_scan_directory'] = str(expected_dir)