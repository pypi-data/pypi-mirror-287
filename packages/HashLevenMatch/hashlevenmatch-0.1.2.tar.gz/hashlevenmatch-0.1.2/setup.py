from setuptools import setup

setup(
    name='HashLevenMatch',                   
    version='0.1.2',                           
    description='Library to utilize inexact matching.',  
    packages=['HashLevenMatch'],             
    author_email='davislspradling@gmail.com',
    zip_safe=False,
    install_requires=[
        'python-Levenshtein',
        'matplotlib',
        'pandas',
        'numpy'
    ]
)
