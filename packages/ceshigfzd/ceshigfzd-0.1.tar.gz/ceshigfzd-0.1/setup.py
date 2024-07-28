# genedist/setup.py

from setuptools import setup, find_packages

setup(
    name='ceshigfzd',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'calculate_dist=genedist.calculate:calculate_dist',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to calculate genetic distance between sequences',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
