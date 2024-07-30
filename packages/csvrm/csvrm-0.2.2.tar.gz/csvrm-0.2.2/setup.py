from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='csvrm',
    version='0.2.2',
    packages=find_packages(),
    requires=[

    ],
    long_description=description,
    long_description_content_type='text/markdown',
)
