from setuptools import setup, find_packages

setup(
    name='societyai',
    version='0.1.3',
    author='Hezi Aharon',
    author_email='hezi@societyai.com',
    description='Utilities for working with Society AI Hub',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://docs.societyai.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'tqdm',
    ],
)
