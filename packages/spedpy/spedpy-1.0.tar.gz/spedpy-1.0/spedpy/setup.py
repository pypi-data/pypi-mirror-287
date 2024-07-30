from setuptools import setup, find_packages
from setuptools.command.test import test as test_command

class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # doctest
        import sys
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='spedpy',
    include_package_data=True,
    version="1.00",
    description='Biblioteca SPED em Python',
    long_description='Biblioteca SPED em Python',
    author='Ismael Nascimento',
    author_email='ismaelnjr@icloud.com',
    license='MIT',
    keywords='sped fiscal',
    packages=['spedpy'],
    install_requires=['six'],
)
