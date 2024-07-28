# setup.py
from setuptools import setup, find_packages

setup(
    name='cebtp',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'mne',
        'PyWavelets',
        'nolds',
        'antropy',
        'tensorflow',
        'google-cloud-storage',
        'cryptography',
        'keras'
    ],
    python_requires='>=3.9',  # Specify compatible Python versions
    author='ZENIHTH',
    author_email='chainloop3@mail.com',
    description='Package for cebtp EEG and feature data preprocessing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ZENITH-Intelligence',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

