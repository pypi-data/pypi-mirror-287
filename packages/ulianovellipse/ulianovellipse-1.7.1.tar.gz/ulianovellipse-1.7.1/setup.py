from setuptools import setup, find_packages

# Ler o conteúdo do README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ulianovellipse',
    version='1.7.1',
    description='Library for handling Ulianov elliptical functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Policarpo Yoshin Ulianov',
    author_email='poliyu77@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    setup_requires=[
        'numpy',
    ],
    package_data={
        # Inclua todos os arquivos .png na pasta images e na pasta examples
        '': ['images/*.png', 'examples/*.py'],
    },
    include_package_data=True,
)
