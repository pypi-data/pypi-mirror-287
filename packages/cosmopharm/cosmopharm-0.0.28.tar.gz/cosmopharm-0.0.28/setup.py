from setuptools import setup, find_packages
import subprocess

def get_version_from_git():
    try:
        version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip().decode('utf-8')
        return version
    except Exception as e:
        print(f"Error getting version from git: {e}")
        return "0.0.0"  # Default or fallback version

# Dynamically set the long_description from readme_pypi.md, if available
try:
    with open('./docs/README_pypi.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = None

if __name__ == "__main__":
    setup(
        version=get_version_from_git(),
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
    )
