from setuptools import setup,find_packages

setup(
    name='ShauryaWarrior-STT',
    version='0.1',
    author='Shaurya',
    author_email='minecraft1212121212121213@gmail.com',
    description='A Python package for Speech-to-Text conversion',
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager',
]
