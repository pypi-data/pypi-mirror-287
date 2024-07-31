from setuptools import setup, find_packages

setup(
    name='artifact_client',
    version='1.0.6',
    description='Python client for the Artifact API',
    author='Artifact Dev Team',
    author_email='contact@useartifact.ai',
    packages=find_packages(),
    install_requires=[
        'requests',
        'openapi-client'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)