from setuptools import setup, find_packages

def parse_requirements(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

install_requires = parse_requirements('requirements.txt')

setup(
    name='admetica',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'admetica_predict = cli.cli:main',
        ],
    },
)