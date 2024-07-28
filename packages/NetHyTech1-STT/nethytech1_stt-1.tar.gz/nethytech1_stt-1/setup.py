from setuptools import setup, find_packages 

setup(
    name='NetHyTech1-STT',
    version='1',
    author='NetHy',
    author_email='nethy@pm.me',
    discription='STT for NetHyTech1',
)
packages = find_packages()
install_requires = [
    'selenium',
    'webdriver-manager',
]

