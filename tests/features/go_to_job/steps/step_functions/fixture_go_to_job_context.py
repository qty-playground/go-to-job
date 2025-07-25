"""Go-to-job context fixture for BDD testing."""
import pytest
import tempfile
import os
from pathlib import Path


@pytest.fixture
def go_to_job_context():
    """Context fixture for go-to-job BDD scenarios."""
    # Create temporary work directory for testing
    temp_work_dir = tempfile.mkdtemp()
    
    context = {
        'work_dir': temp_work_dir,
        'projects': [],
        'command_output': None,
        'selected_project': None,
        'current_directory': None,
        'venv_activated': False,
        'error_message': None
    }
    
    yield context
    
    # Cleanup - remove temporary directory
    import shutil
    shutil.rmtree(temp_work_dir, ignore_errors=True)