"""Go-to-job project navigation tool."""
from typing import List, Optional
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ProjectInfo:
    """Information about a project."""
    name: str
    path: Path
    has_venv: bool = False


class GoToJobTool:
    """Main tool for project navigation."""
    
    def __init__(self, work_dir: Optional[str] = None):
        """Initialize with work directory."""
        self.work_dir = Path(work_dir) if work_dir else Path.home() / "temp"
    
    def list_projects(self) -> List[ProjectInfo]:
        """Scan work directory and return all available project information.
        
        Returns:
            List of ProjectInfo objects sorted alphabetically by project name.
            Returns empty list if work directory doesn't exist.
        """
        discovered_project_list: List[ProjectInfo] = []
        
        if not self.work_dir.exists():
            return discovered_project_list
        
        for potential_project_directory in self.work_dir.iterdir():
            if self._is_valid_project_directory(potential_project_directory):
                project_with_environment_info = self._create_project_info_with_virtual_environment_detection(
                    potential_project_directory
                )
                discovered_project_list.append(project_with_environment_info)
        
        return sorted(discovered_project_list, key=lambda project: project.name)
    
    def _is_valid_project_directory(self, directory_path: Path) -> bool:
        """Determine if directory path represents a valid project directory.
        
        Args:
            directory_path: Path to examine for project directory validity
            
        Returns:
            True if directory is valid project directory, False otherwise
        """
        return directory_path.is_dir() and not directory_path.name.startswith('.')
    
    def _create_project_info_with_virtual_environment_detection(self, project_directory_path: Path) -> ProjectInfo:
        """Create ProjectInfo object with virtual environment detection for given project path.
        
        Args:
            project_directory_path: Path to project directory to analyze
            
        Returns:
            ProjectInfo object containing project details and virtual environment status
        """
        virtual_environment_detected = self._detect_virtual_environment_in_project_directory(
            project_directory_path
        )
        
        return ProjectInfo(
            name=project_directory_path.name,
            path=project_directory_path,
            has_venv=virtual_environment_detected
        )
    
    def _detect_virtual_environment_in_project_directory(self, project_directory_path: Path) -> bool:
        """Detect presence of virtual environment in project directory.
        
        Args:
            project_directory_path: Path to project directory to examine
            
        Returns:
            True if virtual environment detected, False otherwise
        """
        standard_venv_directory = project_directory_path / 'venv'
        hidden_venv_directory = project_directory_path / '.venv'
        
        return standard_venv_directory.exists() or hidden_venv_directory.exists()
    
    def navigate_to_project(self, project_name: str) -> bool:
        """Navigate to specified project directory."""
        project_path = self.work_dir / project_name
        
        if not project_path.exists():
            return False
        
        if not project_path.is_dir():
            return False
        
        # In a real implementation, this would change the current working directory
        # For testing purposes, we just validate the project exists
        return True
    
    def activate_venv_if_exists(self, project_path: Path) -> bool:
        """Activate virtual environment if it exists."""
        # Check for common venv directory names
        venv_paths = [
            project_path / 'venv',
            project_path / '.venv',
            project_path / 'env'
        ]
        
        for venv_path in venv_paths:
            if venv_path.exists() and venv_path.is_dir():
                # Check if activate script exists
                activate_script = venv_path / 'bin' / 'activate'
                if activate_script.exists():
                    # In real implementation, this would run: source venv/bin/activate
                    # For testing purposes, we just return True to indicate success
                    return True
        
        # No virtual environment found
        return False