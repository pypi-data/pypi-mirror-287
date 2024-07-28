from setuptools import setup, find_packages
from src.cli import __name__, __version__

setup(
    name=f'{__name__}',
    version=f'{__version__}',
    description='pip libraries tree',
    author='liuhf',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'piptree = src.piptree.cli:main',
        ]
    },
    install_requires=[
        # Required libraries
        'pip'
    ]
)
