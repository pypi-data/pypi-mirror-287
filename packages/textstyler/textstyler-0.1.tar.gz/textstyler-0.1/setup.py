from setuptools import setup, find_packages

setup(
    name='textstyler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'termcolor',
        'pyfiglet',
    ],
    author='Your Name',
    author_email='dexterawesome16@gmail.com',
    description='A package for styling text and creating text banners',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PrestigeOcean1/textstyler',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
