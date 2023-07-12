from setuptools import setup, find_packages

setup(
    name="Hello",
    version="0.1",
    author="Student",
    packages=find_packages(),
    long_description= open("README.md").read(),
)

# запустить команду в терминале из той папки где находится setup.py
# python setup.py sdist - создаём пакет
