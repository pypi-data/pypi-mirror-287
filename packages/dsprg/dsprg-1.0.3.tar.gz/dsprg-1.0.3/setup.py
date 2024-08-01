from setuptools import setup, find_packages

setup(
    name='dsprg',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['dsprg.py', 'data.txt'],  # Include both files
    },
    description='A package for nothing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='petteer1',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
