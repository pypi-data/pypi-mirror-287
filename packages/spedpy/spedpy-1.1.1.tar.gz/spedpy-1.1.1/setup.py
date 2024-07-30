from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='spedpy',
    version='1.1.1',
    license='MIT License',
    author='Ismael Nascimento',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ismaelnjr@icloud.com',
    keywords='sped fiscal',
    description=u'Biblioteca SPED em Python',
    packages=find_packages(exclude=['etc', 'test']),
    include_package_data=True,
    install_requires=['six'],)