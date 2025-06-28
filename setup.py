from setuptools import setup, find_packages

setup(
    name='ai-risk-scoring',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'faker',
        'matplotlib',
    ],
    author='Johnnie',
    description='Risk scoring and visualization framework for synthetic login events',
)

