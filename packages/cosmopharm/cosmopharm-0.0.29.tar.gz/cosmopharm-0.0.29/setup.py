from setuptools import setup, find_packages

# Dynamically set the long_description from readme_pypi.md, if available
try:
    with open('./docs/README_pypi.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = None

setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)