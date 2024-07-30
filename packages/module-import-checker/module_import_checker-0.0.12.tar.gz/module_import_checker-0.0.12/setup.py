from setuptools import setup

setup(
    name='module_import_checker',
    version='0.0.12',
    packages=['module_import_checker'],
    author="Abiola Adeshina",
    author_email="abiolaadeshinaadedayo@gmail.com",
    description="An utility tool to check for inappropriate imports between modules in a Python project.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Abiorh001/module_import_checker.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'import_module_checker=module_import_checker.cli:main',
        ],
    },
)
