from setuptools import setup, find_packages

setup(
    name='py-tool-set-testing',
    version='0.0.1',
    packages=find_packages(),
    description='A simple library with some useful functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abhinav Kumar',
    author_email='abhinavkumar2369@outlook.com',
    url='https://github.com/abhinavkumar2369/py-tool-kit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
