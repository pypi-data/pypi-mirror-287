from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='OhMyDecorators',
    version='0.1.0',
    author='A-Boring-Square',
    author_email='aboringsquare@gmail.com',
    description='A Python library that provides lots of decorators for simple tasks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/A-Boring-Square/OhMyDecorators',  # Replace with your actual URL
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'tensorflow'
    ],
)
