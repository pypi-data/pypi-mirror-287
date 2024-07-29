#pylint: disable-all
from setuptools import setup

setup(
    name='co_simulations',
    version='0.1.0',
    description='A package containing the necessary simulations for Common Optima',
    author='HZ-9000',
    license='MIT',
    packages=['co_simulations','co_simulations.factory'],
    install_requires=[],
    python_requires='>=3.8',
    extras_require={
        'linting': [
            "pylint",
            "ruff"
        ],
        'testing': [
            "pytest"
        ]
    },
    include_package_data=True
)
