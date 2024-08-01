from setuptools import setup,find_packages

setup(
    name='Durrani-SMAKD',
    version='0.3',
    author='Mohsin Durrani',
    author_email='mohsindurrani01@gmail.com',
    description = 'This is Speech To Text Package Created By Mohsin Durrani'
)
packages = find_packages(),
install_reuirements = [
    'selenium',
    'webdriver_manager'
]


