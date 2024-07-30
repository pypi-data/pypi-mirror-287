from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()
setup(
    name='spedpy',
    include_package_data=True,
    version="1.01",
    description='Biblioteca SPED em Python',
    long_description='Biblioteca SPED em Python',
    author='Ismael Nascimento',
    author_email='ismaelnjr@icloud.com',
    license='MIT',
    keywords='sped fiscal',
    packages=['sped'],
    install_requires=['six'],
)
