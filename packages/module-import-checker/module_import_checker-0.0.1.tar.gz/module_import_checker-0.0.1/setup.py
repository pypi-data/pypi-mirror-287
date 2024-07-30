from setuptools import setup

setup(
    name='module_import_checker',
    version='0.0.1',
    packages=['module_import_checker'],
    entry_points={
        'console_scripts': [
            'import_module_checker=module_import_checker.cli:main',
        ],
    },
)
