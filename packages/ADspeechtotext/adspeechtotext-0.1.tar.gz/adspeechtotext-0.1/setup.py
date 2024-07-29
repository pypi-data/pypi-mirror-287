from setuptools import setup,find_packages

setup(
    name = 'ADspeechtotext',
    version = '0.1',
    author = 'Aditya Pratap Singh',
    author_email = 'aditya.singh2021@sait.ac.in',
    description = 'This is a speech to text package, you can use it to covert your speech into text.'
)
packages = find_packages(),
install_requirement = [
    'selenium',
    'webdriver_manager'
]