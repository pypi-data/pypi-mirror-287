from setuptools import setup, find_packages

setup(
    name='dsprg',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ds_program_package': ['dsprg.txt'],
    },
    description='A package to read and print specific programs from a text file for data structures.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='your_name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)