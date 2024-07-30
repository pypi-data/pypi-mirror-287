from setuptools import setup,find_packages

setup(
    name = 'GILL-STT',
    version = '0.1',
    author = 'Navi Gill',
    email = 'gillnavi210@gmail.com',
    description = 'This is speech to text package'
)
packages = find_packages()
install_requirements = [
    'selenium',
    'webdriver_manager'
]
