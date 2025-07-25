#!/usr/bin/env python3
"""Go-to-job command line interface."""
import os
import sys
from pathlib import Path
from typing import List, Optional

from go_to_job import GoToJobTool, ProjectInfo


def get_work_directory() -> Path:
    """Get work directory from environment or use default."""
    # Check environment variable first
    work_dir_env = os.environ.get('GOTOJOB_WORK_DIR')
    if work_dir_env:
        return Path(work_dir_env).expanduser()
    
    # Check config file
    config_file = Path.home() / '.go-to-job.conf'
    if config_file.exists():
        try:
            config_content = config_file.read_text().strip()
            for line in config_content.split('\n'):
                if line.startswith('work_dir='):
                    config_dir = line.split('=', 1)[1].strip()
                    return Path(config_dir).expanduser()
        except Exception:
            pass  # Ignore config file errors
    
    # Default to ~/temp
    return Path.home() / 'temp'


def display_projects(projects: List[ProjectInfo]) -> None:
    """Display available projects to user."""
    if not projects:
        print("No projects found in work directory.")
        return
    
    print(f"\n📂 Available projects ({len(projects)}):")
    print("=" * 40)
    
    for i, project in enumerate(projects, 1):
        venv_indicator = "🐍" if project.has_venv else "📁"
        print(f"{i:2d}. {venv_indicator} {project.name}")
    
    print("\n🐍 = Has virtual environment")
    print("📁 = No virtual environment")


def get_user_choice(projects: List[ProjectInfo]) -> Optional[ProjectInfo]:
    """Get user's project selection."""
    while True:
        try:
            choice = input(f"\nSelect project (1-{len(projects)}, or 'q' to quit): ").strip()
            
            if choice.lower() == 'q':
                return None
            
            project_index = int(choice) - 1
            if 0 <= project_index < len(projects):
                return projects[project_index]
            else:
                print(f"Please enter a number between 1 and {len(projects)}")
                
        except ValueError:
            print("Please enter a valid number or 'q' to quit")
        except KeyboardInterrupt:
            print("\n\nBye! 👋")
            return None


def navigate_to_project(tool: GoToJobTool, project: ProjectInfo) -> None:
    """Navigate to selected project and activate venv if available."""
    print(f"\n🔄 Navigating to {project.name}...")
    
    # Navigate to project
    if not tool.navigate_to_project(project.name):
        print(f"❌ Failed to navigate to {project.name}")
        return
    
    print(f"📂 Changed directory to: {project.path}")
    
    # Try to activate virtual environment
    if project.has_venv:
        print("🐍 Activating virtual environment...")
        if tool.activate_venv_if_exists(project.path):
            print("✅ Virtual environment activated!")
            print(f"💡 Run: cd {project.path} && source venv/bin/activate")
        else:
            print("⚠️  Could not activate virtual environment")
    else:
        print("📁 No virtual environment found")
        print(f"💡 Run: cd {project.path}")
    
    print(f"\n🚀 Ready to work on {project.name}!")


def main() -> None:
    """Main CLI entry point."""
    print("🔧 Go-to-Job - Quick Project Navigation")
    print("=====================================")
    
    try:
        # Get work directory
        work_dir = get_work_directory()
        print(f"📁 Work directory: {work_dir}")
        
        if not work_dir.exists():
            print(f"❌ Work directory does not exist: {work_dir}")
            print("💡 Create the directory or set GOTOJOB_WORK_DIR environment variable")
            sys.exit(1)
        
        # Initialize tool
        tool = GoToJobTool(str(work_dir))
        
        # List projects
        print("\n🔍 Scanning for projects...")
        projects = tool.list_projects()
        
        if not projects:
            print(f"No projects found in {work_dir}")
            print("💡 Create some project directories in your work directory")
            sys.exit(0)
        
        # Display projects and get user choice
        display_projects(projects)
        selected_project = get_user_choice(projects)
        
        if selected_project:
            navigate_to_project(tool, selected_project)
        else:
            print("No project selected. Goodbye! 👋")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()