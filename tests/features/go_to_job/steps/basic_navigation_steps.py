"""Step definitions for basic navigation BDD tests using screaming architecture."""

from pytest_bdd import given, when, then, scenarios, parsers
import pytest

# Import fixture
from .step_functions.fixture_go_to_job_context import go_to_job_context

# Import step function modules - each file name tells you exactly what it does
from .step_functions import (
    given_i_have_some_projects_in_work_folder,
    given_i_have_multiple_projects_in_work_directory,
    given_i_have_project_in_work_directory,
    given_my_project_has_virtual_environment,
    given_my_project_has_no_virtual_environment,
    when_i_execute_go_to_job_command,
    when_i_select_project,
    then_i_should_see_available_projects_list,
    then_i_should_switch_to_project_directory,
    then_virtual_environment_should_be_activated,
    then_should_not_try_to_activate_virtual_environment
)

# Load all scenarios from the basic navigation feature
scenarios('../basic_navigation.feature')

# Mark first scenario for selective testing
pytestmark = pytest.mark.bdd


@given('我有一些專案在工作資料夾')
def step_given_i_have_some_projects_in_work_folder(go_to_job_context):
    """Given 我有一些專案在工作資料夾."""
    given_i_have_some_projects_in_work_folder.execute(go_to_job_context)


@given('我在工作目錄有多個專案')
def step_given_i_have_multiple_projects_in_work_directory(go_to_job_context):
    """Given 我在工作目錄有多個專案."""
    given_i_have_multiple_projects_in_work_directory.execute(go_to_job_context)


@when('我執行 go-to-job 指令')
def step_when_i_execute_go_to_job_command(go_to_job_context):
    """When 我執行 go-to-job 指令."""
    when_i_execute_go_to_job_command.execute(go_to_job_context)


@given(parsers.parse('我在工作目錄有專案 "{project_name}"'))
def step_given_i_have_project_in_work_directory(go_to_job_context, project_name):
    """Given 我在工作目錄有專案 {project_name}."""
    given_i_have_project_in_work_directory.execute(go_to_job_context, project_name)


@when(parsers.parse('我選擇 "{project_name}" 專案'))
def step_when_i_select_project(go_to_job_context, project_name):
    """When 我選擇 {project_name} 專案."""
    when_i_select_project.execute(go_to_job_context, project_name)


@then('我應該看到可用專案的清單')
def step_then_i_should_see_available_projects_list(go_to_job_context):
    """Then 我應該看到可用專案的清單."""
    then_i_should_see_available_projects_list.execute(go_to_job_context)


@given(parsers.parse('我的專案 "{project_name}" 有虛擬環境'))
def step_given_my_project_has_virtual_environment(go_to_job_context, project_name):
    """Given 我的專案 {project_name} 有虛擬環境."""
    given_my_project_has_virtual_environment.execute(go_to_job_context, project_name)


@given(parsers.parse('我的專案 "{project_name}" 沒有虛擬環境'))
def step_given_my_project_has_no_virtual_environment(go_to_job_context, project_name):
    """Given 我的專案 {project_name} 沒有虛擬環境."""
    given_my_project_has_no_virtual_environment.execute(go_to_job_context, project_name)


@then(parsers.parse('我應該切換到 "{project_name}" 目錄'))
def step_then_i_should_switch_to_project_directory(go_to_job_context, project_name):
    """Then 我應該切換到 {project_name} 目錄."""
    then_i_should_switch_to_project_directory.execute(go_to_job_context, project_name)


@then('我應該切換到專案目錄')
def step_then_i_should_switch_to_project_directory_general(go_to_job_context):
    """Then 我應該切換到專案目錄."""
    then_i_should_switch_to_project_directory.execute(go_to_job_context)


@then('虛擬環境應該被自動啟用')
def step_then_virtual_environment_should_be_activated(go_to_job_context):
    """Then 虛擬環境應該被自動啟用."""
    then_virtual_environment_should_be_activated.execute(go_to_job_context)


@then('不應該嘗試啟用虛擬環境')
def step_then_should_not_try_to_activate_virtual_environment(go_to_job_context):
    """Then 不應該嘗試啟用虛擬環境."""
    then_should_not_try_to_activate_virtual_environment.execute(go_to_job_context)