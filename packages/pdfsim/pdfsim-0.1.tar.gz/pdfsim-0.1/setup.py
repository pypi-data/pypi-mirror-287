# setup.py
from setuptools import setup, find_packages

setup(
    name='pdfsim',
    version='0.1',
    packages=find_packages(),
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
    description='A CLI tool to find similar PDF.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/invoice_similarity',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
