from setuptools import setup, find_packages

setup(
    name="go-to-job",
    version="0.1.0",
    description="Quick project navigation tool with automatic virtual environment activation",
    author="Developer Team",
    author_email="developer@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["go_to_job", "go_to_job_cli"],
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies for go-to-job functionality
    ],
    extras_require={
        "test": [
            "pytest==8.4.1",
            "pytest-asyncio==1.1.0",
            "pytest-bdd==8.1.0",
        ],
        "dev": [
            "pytest==8.4.1",
            "pytest-asyncio==1.1.0",
            "pytest-bdd==8.1.0",
            "black==25.1.0",
            "flake8==7.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "go-to-job=go_to_job_cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)