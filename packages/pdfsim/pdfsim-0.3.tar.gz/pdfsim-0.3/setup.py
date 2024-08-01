# setup.py
from setuptools import setup, find_packages

setup(
    name='pdfsim',
    version='0.3',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'pdfsim=main:main',
        ],
    },
    install_requires=[
        # Add your dependencies here
        # 'some_dependency',
    ],
    author='Krishav Raj Singh',
    author_email='krishavrajsingh@example.com',
    description='A CLI tool to find similar PDF in a given directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KrishavRajSingh/pdfsim',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
