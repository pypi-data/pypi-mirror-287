from setuptools import setup, find_packages

setup(
    name='HashLevenMatch',
    version='0.1.3',
    description='Library to utilize inexact matching.',
    packages=find_packages(),
    author_email='davislspradling@gmail.com',
    zip_safe=False,
    install_requires=[
        'python-Levenshtein',
        'matplotlib',
        'pandas',
        'numpy'
    ]
)
